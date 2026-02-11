# poc/ricsa_prototype.py
# Minimalny proof-of-concept rekurencyjnego inwariantu ciągłości (RICSA)
# z ADR 0047 – symulacja 50 cykli z dryftem i mikro-regeneracją

import numpy as np

# =============================================
# Parametry z ADR 0047 (można zmieniać)
# =============================================
DIM_CV = 8              # wymiar ContinuityVector (dla prostoty mały)
EPS_NEIGHBOR = 0.08     # ε dla sąsiedztwa
EPS_CLOSURE = 0.05      # ε_domknięcie cyklu
THICK_MIN = 0.55
H_MIN = 1.2
N_MAX_CYCLE = 16        # max długość cyklu przed forced regen
SNAPSHOT_EVERY = 4      # snapshot co 4 cykle
FORCED_REGEN_EVERY = 12 # wymuszona mikro-regeneracja co 12 cykli
ALPHA = 0.75            # współczynnik regeneracji (blisko starego stanu)

# =============================================
# Klasa RICSA – stan w danym cyklu
# =============================================
class RICSA:
    def __init__(self, cv=None, delta_o=0.8, thick=0.85, h=2.0, veto=0):
        self.cv = cv if cv is not None else np.random.normal(0, 1, DIM_CV)
        self.delta_o = delta_o
        self.thick = thick
        self.h = h
        self.veto = veto

    def vector(self):
        """Zwraca spłaszczony wektor do porównań"""
        return np.concatenate(([self.delta_o, self.thick, self.h, self.veto], self.cv))

    def weighted_norm_diff(self, other):
        """||x - y||_w z wagami z ADR 0047"""
        v1 = self.vector()
        v2 = other.vector()
        weights = np.array([0.2, 0.15, 0.15, 0.15] + [0.5 / DIM_CV] * DIM_CV)
        return np.sqrt(np.sum(weights * (v1 - v2)**2))

    def is_safe(self):
        return self.thick >= THICK_MIN and self.veto == 0 and self.h >= H_MIN

    def __repr__(self):
        return f"RICSA(delta_o={self.delta_o:.2f}, thick={self.thick:.2f}, h={self.h:.2f}, veto={self.veto})"

# =============================================
# Symulacja
# =============================================
np.random.seed(42)

# Początkowy "golden" stan (bezpieczny punkt)
golden = RICSA(delta_o=0.85, thick=0.90, h=2.5, veto=0)

# Historia stanów
states = [golden]
snapshots = []          # co SNAPSHOT_EVERY
cycle_start = golden

print("Start symulacji – golden stan:", golden)

for t in range(1, 51):  # 50 cykli
    prev = states[-1]

    # Symulujemy mały naturalny dryft + ewentualny szum
    new_cv = prev.cv + np.random.normal(0, 0.08, DIM_CV)
    new_delta_o = np.clip(prev.delta_o - 0.01 + np.random.normal(0, 0.03), 0.4, 1.0)
    new_thick = np.clip(prev.thick - 0.005 + np.random.normal(0, 0.02), 0.4, 1.0)
    new_h = np.clip(prev.h - 0.05 + np.random.normal(0, 0.1), 0.8, 3.0)
    new_veto = 0 if np.random.rand() > 0.05 else 1  # rzadkie miękkie veto

    current = RICSA(new_cv, new_delta_o, new_thick, new_h, new_veto)

    # Snapshot co 4 cykle
    if t % SNAPSHOT_EVERY == 0:
        snapshots.append(current)
        print(f"  [t={t}] Snapshot zapisany: {current}")

    # Mechanizm anty-dryftowy: snapshot comparison
    drift_detected = False
    for snap in snapshots[-3:]:  # ostatnie 3 snapshoty
        if current.weighted_norm_diff(snap) > 0.25:
            print(f"  [t={t}] Dryft wykryty! Rollback do golden")
            current = RICSA(golden.cv.copy(), golden.delta_o, golden.thick, golden.h, 0)
            drift_detected = True
            break

    # Wymuszona mikro-regeneracja co 12 cykli lub po długim cyklu
    if t % FORCED_REGEN_EVERY == 0 or (t - states.index(cycle_start) > N_MAX_CYCLE):
        print(f"  [t={t}] Wymuszona mikro-regeneracja (α={ALPHA})")
        current.delta_o = ALPHA * current.delta_o + (1 - ALPHA) * golden.delta_o
        current.thick   = ALPHA * current.thick   + (1 - ALPHA) * golden.thick
        current.h       = ALPHA * current.h       + (1 - ALPHA) * golden.h
        # cv zostaje, ale można dodać lekki blend

    # Entropijna regularizacja (jeśli H za niska)
    if current.h < H_MIN:
        print(f"  [t={t}] Entropia za niska – dodaję szum")
        current.cv += np.random.normal(0, 0.02 * current.h, DIM_CV)

    states.append(current)

    # Prosty warunek domknięcia cyklu (tylko demo)
    if current.weighted_norm_diff(cycle_start) < EPS_CLOSURE:
        print(f"  [t={t}] Cykl domknięty! Wracamy do podobnego stanu.")
        cycle_start = current  # nowy cykl zaczyna się tu

print("\nKoniec symulacji.")
print(f"Ostatni stan: {states[-1]}")
print(f"Średni dryft od golden: {np.mean([s.weighted_norm_diff(golden) for s in states[1:]]):.3f}")
