import numpy as np
from dataclasses import dataclass, field
from typing import List, Optional

DIM_CV = 8

# --- parametry bazowe (z ADR 0047, lekko zmiękczone) ---

BASE_DRIFT_THRESHOLD = 0.25      # bazowy próg dryftu
MIN_DRIFT_THRESHOLD = 0.12       # dolna granica adaptacji
MAX_DRIFT_THRESHOLD = 0.45       # górna granica adaptacji

SNAPSHOT_INTERVAL = 6            # rzadsze snapshoty
MICRO_REGEN_INTERVAL = 16        # dłuższy oddech
SOFT_ROLLBACK_ALPHA = 0.6        # jak mocno wracamy do golden przy rollbacku

EPS_CLOSURE = 0.08               # trochę luźniejsze domknięcie
H_MIN = 1.2
H_MAX = 2.5

ROLLBACK_PRESSURE_WINDOW = 20    # ile cykli patrzymy wstecz
ROLLBACK_PRESSURE_HIGH = 0.35    # powyżej tego – veto może się włączyć

ENTROPY_NOISE_SCALE = 0.05


@dataclass
class RICSAState:
    delta_o: float
    thick: float
    h: float
    veto: float
    cv: np.ndarray


@dataclass
class RICSAHistory:
    states: List[RICSAState] = field(default_factory=list)
    rollbacks: List[int] = field(default_factory=list)

    def add_state(self, state: RICSAState):
        self.states.append(state)

    def add_rollback(self, step: int):
        self.rollbacks.append(step)

    def rollback_pressure(self, current_step: int, window: int) -> float:
        if not self.rollbacks:
            return 0.0
        recent = [s for s in self.rollbacks if current_step - s <= window]
        return len(recent) / max(1, window)

    def mean_state_vector(self) -> Optional[np.ndarray]:
        if not self.states:
            return None
        vs = [RICSA.vector_from_state(s) for s in self.states]
        return np.mean(vs, axis=0)


class RICSA:
    def __init__(self, golden: RICSAState):
        self.golden = golden
        self.current = golden
        self.snapshot_ema: Optional[np.ndarray] = None
        self.history = RICSAHistory()
        self.drift_threshold = BASE_DRIFT_THRESHOLD

    @staticmethod
    def vector_from_state(s: RICSAState) -> np.ndarray:
        return np.concatenate(([s.delta_o, s.thick, s.h, s.veto], s.cv))

    @staticmethod
    def weighted_norm_diff(v1: np.ndarray, v2: np.ndarray) -> float:
        # wagi: CV mniej dominujące, ale nadal ważne
        w = np.ones_like(v1)
        w[0] = 0.2   # delta_o
        w[1] = 0.2   # thick
        w[2] = 0.2   # h
        w[3] = 0.2   # veto
        w[4:] = 0.2 / max(1, len(v1) - 4)
        diff = (v1 - v2) * w
        return float(np.linalg.norm(diff))

    def update_snapshot_ema(self, v: np.ndarray, alpha: float = 0.4):
        if self.snapshot_ema is None:
            self.snapshot_ema = v.copy()
        else:
            self.snapshot_ema = alpha * v + (1 - alpha) * self.snapshot_ema

    def adapt_drift_threshold(self, last_diff: float):
        # jeśli ciągle blisko – możemy zaostrzyć próg, jeśli daleko – poluzować
        target = last_diff * 1.5
        blended = 0.7 * self.drift_threshold + 0.3 * target
        self.drift_threshold = float(
            np.clip(blended, MIN_DRIFT_THRESHOLD, MAX_DRIFT_THRESHOLD)
        )

    def soft_rollback(self):
        v_cur = self.vector(self.current)
        v_gold = self.vector(self.golden)
        v_new = SOFT_ROLLBACK_ALPHA * v_gold + (1 - SOFT_ROLLBACK_ALPHA) * v_cur
        self.current = self.state_from_vector(v_new)

    def state_from_vector(self, v: np.ndarray) -> RICSAState:
        return RICSAState(
            delta_o=float(v[0]),
            thick=float(v[1]),
            h=float(v[2]),
            veto=float(v[3]),
            cv=v[4:].copy(),
        )

    def vector(self, s: Optional[RICSAState] = None) -> np.ndarray:
        if s is None:
            s = self.current
        return self.vector_from_state(s)

    def is_safe(self, v: np.ndarray) -> bool:
        h = v[2]
        return (H_MIN <= h <= H_MAX)

    def maybe_veto(self, step: int) -> bool:
        pressure = self.history.rollback_pressure(step, ROLLBACK_PRESSURE_WINDOW)
        # veto nie jest losowe – pojawia się przy chronicznym przeciążeniu
        if pressure > ROLLBACK_PRESSURE_HIGH:
            return True
        return False

    def step(self, step_idx: int, rng: np.random.Generator):
        v = self.vector()

        # --- entropijna regularyzacja ---
        if self.current.h < H_MIN:
            noise = rng.normal(0.0, ENTROPY_NOISE_SCALE, size=v.shape)
            v = v + noise

        # --- losowa fluktuacja CV + lekkie zmiany delta_o, thick, h ---
        noise_main = rng.normal(0.0, 0.02, size=v.shape)
        v = v + noise_main

        candidate = self.state_from_vector(v)

        # --- snapshot co SNAPSHOT_INTERVAL ---
        if step_idx % SNAPSHOT_INTERVAL == 0:
            self.update_snapshot_ema(self.vector(candidate))

        # --- dryft względem golden + snapshot_ema ---
        v_gold = self.vector(self.golden)
        diff_golden = self.weighted_norm_diff(self.vector(candidate), v_gold)

        if self.snapshot_ema is not None:
            diff_snap = self.weighted_norm_diff(self.vector(candidate), self.snapshot_ema)
            effective_diff = 0.5 * diff_golden + 0.5 * diff_snap
        else:
            effective_diff = diff_golden

        self.adapt_drift_threshold(effective_diff)

        rollback = False
        if effective_diff > self.drift_threshold or not self.is_safe(self.vector(candidate)):
            rollback = True
            self.soft_rollback()
            self.history.add_rollback(step_idx)
        else:
            self.current = candidate

        # --- mikro‑regeneracja co MICRO_REGEN_INTERVAL ---
        if step_idx % MICRO_REGEN_INTERVAL == 0 and step_idx > 0:
            v_cur = self.vector()
            v_gold = self.vector(self.golden)
            v_blend = 0.75 * v_cur + 0.25 * v_gold
            self.current = self.state_from_vector(v_blend)

        # --- veto jako sygnał przeciążenia systemu ---
        if self.maybe_veto(step_idx):
            self.current.veto = 1.0
        else:
            self.current.veto = 0.0

        # --- zapis historii ---
        self.history.add_state(self.current)

        return {
            "step": step_idx,
            "rollback": rollback,
            "effective_diff": effective_diff,
            "drift_threshold": self.drift_threshold,
            "veto": self.current.veto,
        }

    def cycle_closed(self) -> bool:
        # domknięcie względem średniego stanu + golden
        v_cur = self.vector()
        v_gold = self.vector(self.golden)
        mean_vec = self.history.mean_state_vector()
        if mean_vec is None:
            mean_vec = v_gold

        d_mean = self.weighted_norm_diff(v_cur, mean_vec)
        d_gold = self.weighted_norm_diff(v_cur, v_gold)
        return (d_mean < EPS_CLOSURE) and (d_gold < EPS_CLOSURE)

    def __repr__(self):
        return (
            f"RICSA(delta_o={self.current.delta_o:.3f}, "
            f"thick={self.current.thick:.3f}, "
            f"h={self.current.h:.3f}, "
            f"veto={self.current.veto:.3f})"
        )


# --- przykładowa pętla symulacyjna ---

def main():
    rng = np.random.default_rng(42)

    golden = RICSAState(
        delta_o=0.0,
        thick=1.0,
        h=1.6,
        veto=0.0,
        cv=rng.normal(0.0, 0.1, size=(DIM_CV,))
    )

    ricsa = RICSA(golden)

    for step in range(80):
        info = ricsa.step(step, rng)
        if step % 8 == 0:
            print(
                f"[{step:03d}] rollback={info['rollback']} "
                f"diff={info['effective_diff']:.3f} thr={info['drift_threshold']:.3f} "
                f"veto={info['veto']:.1f} state={ricsa}"
            )
        if ricsa.cycle_closed():
            print(f"--> cycle closed at step {step}")
            break


if __name__ == "__main__":
    main()
    
