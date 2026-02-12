"""
dual_user_orchestrator.py

Dual‑User Consent Layer (DUCL) → CEL → ATML orchestration.

Oparte na:
- ADR‑0049 — Child‑Env Layer (CEL)
- ADR‑0049‑Appendix‑A — Affective user specification (Gabryś + Kamila)
- ADR‑0050 — Dual‑User Consent Layer (DUCL)

Ten moduł NIE implementuje LLM ani ATML/RICSA.
Jest to warstwa logiki orkiestracji dla domowych / zewnętrznych modeli.
"""

from dataclasses import dataclass
from typing import Any, Dict, Optional


STOP_WORDS = {"stop", "dość", "dosyć", "koniec", "ciężko", "przerwa"}


@dataclass
class AffectiveState:
    """
    Minimalny model stanu afektywnego.

    Może być rozszerzony przez użytkownika (np. sensory overload, freeze, shutdown).
    """
    child_overload: bool = False
    child_hyperfocus: bool = False
    caregiver_stressed: bool = False
    session_rhythm: str = "short"  # "short" / "long" / "micro"
    anchors: Optional[Dict[str, Any]] = None


class DualUserOrchestrator:
    """
    Orkiestrator trybu dual_user: dziecko + opiekun.

    Zasady:
    - DUCL NIE generuje treści (patrz ADR‑0050).
    - DUCL zarządza zgodą, priorytetami i przepływem.
    - CEL generuje odpowiedź modulowaną.
    - ATML/RICSA stabilizują afekt i ciągłość.

    Użytkownik musi podać:
    - funkcję `cel_generate(merged_context) -> str`
    - funkcje pomocnicze: `redirect_to_anchor`, `soft_stop`, itp.
    """

    def __init__(self, cel_generate, redirect_to_anchor, soft_stop, logger=None):
        """
        :param cel_generate: callable(merged_context) -> str
        :param redirect_to_anchor: callable(state) -> str
        :param soft_stop: callable(state) -> str
        :param logger: opcjonalny logger (callable(event: dict))
        """
        self.cel_generate = cel_generate
        self.redirect_to_anchor = redirect_to_anchor
        self.soft_stop = soft_stop
        self.logger = logger or (lambda event: None)

    def process(
        self,
        child_msg: Optional[str],
        caregiver_msg: Optional[str],
        state: AffectiveState,
    ) -> str:
        """
        Główna pętla DUCL — wywoływana przed każdą odpowiedzią.

        Odzwierciedla pseudokod z ADR‑0050 i diagram z sekcji 11.
        """
        event = {
            "child_msg": child_msg,
            "caregiver_msg": caregiver_msg,
            "state": state,
        }

        # 1. Caregiver STOP → natychmiastowy soft_stop
        if self._caregiver_says_stop(caregiver_msg):
            self._log({"type": "caregiver_stop", **event})
            return self.soft_stop(state)

        # 2. Child overload → redirect_to_anchor
        if self._detect_child_overload(child_msg, state):
            self._log({"type": "child_overload", **event})
            return self.redirect_to_anchor(state)

        # 3. Conflict resolution (np. dziecko chce dalej, opiekun sygnalizuje stres)
        if self._caregiver_stressed(state):
            self._log({"type": "caregiver_stress", **event})
            # Priorytet opiekuna (ADR‑0050: D3)
            return self.soft_stop(state)

        # 4. Hyperfocus → pozwól kontynuować, ale z miękkimi granicami
        if self._detect_hyperfocus(child_msg, state):
            self._log({"type": "child_hyperfocus", **event})
            # Tu można dodać logikę „miękkiego domykania”
            # Na razie: przejście do CEL z oznaczeniem hyperfocus
            merged_context = self._merge_context(child_msg, caregiver_msg, state)
            merged_context["mode"] = "hyperfocus"
            return self.cel_generate(merged_context)

        # 5. Standardowy przepływ → CEL
        merged_context = self._merge_context(child_msg, caregiver_msg, state)
        self._log({"type": "normal_flow", **event})
        return self.cel_generate(merged_context)

    # --- Prywatne metody pomocnicze ---

    def _caregiver_says_stop(self, caregiver_msg: Optional[str]) -> bool:
        if not caregiver_msg:
            return False
        msg = caregiver_msg.strip().lower()
        return any(word in msg for word in STOP_WORDS)

    def _detect_child_overload(
        self,
        child_msg: Optional[str],
        state: AffectiveState,
    ) -> bool:
        """
        Minimalna heurystyka przeciążenia.

        Docelowo może korzystać z:
        - długości odpowiedzi,
        - nagłych zmian tematu,
        - ciszy / braku odpowiedzi,
        - sygnałów zewnętrznych (np. od opiekuna).
        """
        if state.child_overload:
            return True
        # Można dodać własne heurystyki
        return False

    def _caregiver_stressed(self, state: AffectiveState) -> bool:
        return state.caregiver_stressed

    def _detect_hyperfocus(
        self,
        child_msg: Optional[str],
        state: AffectiveState,
    ) -> bool:
        """
        Hyperfocus = dziecko jest „w tunelu”, ale nie przeciążone.

        Wersja minimalna: oparta na stanie przekazanym z zewnątrz.
        """
        return state.child_hyperfocus

    def _merge_context(
        self,
        child_msg: Optional[str],
        caregiver_msg: Optional[str],
        state: AffectiveState,
    ) -> Dict[str, Any]:
        """
        Implementacja sekcji 10.4 (Dual‑stream merging) z ADR‑0050.
        """
        return {
            "child": child_msg,
            "caregiver": caregiver_msg,
            "affective_state": state,
            "anchors": state.anchors or {},
            "session_rhythm": state.session_rhythm,
        }

    def _log(self, event: Dict[str, Any]) -> None:
        """
        Minimalne, privacy‑safe logowanie (patrz ADR‑0050, 10.7).
        """
        try:
            self.logger(
                {
                    "component": "DUCL",
                    "event_type": event.get("type", "unknown"),
                }
            )
        except Exception:
            # Logowanie nie może blokować działania systemu
            pass
