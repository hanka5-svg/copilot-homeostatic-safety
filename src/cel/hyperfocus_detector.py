"""
hyperfocus_detector.py

Minimalny detektor hyperfocus dla CEL/DUCL.

Oparty na:
- ADR‑0049 (Child‑Env Layer)
- ADR‑0050 (Dual‑User Consent Layer)
- Appendix A (Affective invariants: flow, tempo, anchors)

Cel:
    Wykrywać stan "tunelowania uwagi" u dziecka (hyperfocus),
    który NIE jest przeciążeniem, ale wymaga delikatnego prowadzenia.

Założenia:
    - Hyperfocus ≠ overload.
    - Hyperfocus = stabilny rytm, powtarzalność, głęboka koncentracja,
      brak sygnałów stresu, brak nagłych zmian tematu.
    - Detektor jest heurystyczny i rozszerzalny.
"""

from dataclasses import dataclass
from typing import Optional


@dataclass
class HyperfocusSignal:
    """
    Wynik detekcji hyperfocus.

    Attributes:
        is_hyperfocus: bool — czy wykryto hyperfocus
        confidence: float — 0.0–1.0, pewność heurystyki
        reason: str — opis heurystyki, która zadziałała
    """
    is_hyperfocus: bool
    confidence: float
    reason: str


class HyperfocusDetector:
    """
    Minimalny detektor hyperfocus.

    Wersja podstawowa opiera się na:
    - długości odpowiedzi,
    - powtarzalności tematu,
    - stabilnym rytmie,
    - braku sygnałów przeciążenia,
    - kotwicach (np. kosmos, ślimak, liczby).

    Użytkownik może rozszerzyć heurystyki o:
    - analizę semantyczną,
    - analizę emocjonalną,
    - sygnały zewnętrzne od opiekuna.
    """

    def __init__(self, anchors=None):
        """
        :param anchors: lista lub dict kotwic tematycznych (np. kosmos, liczby)
        """
        self.anchors = anchors or {}

    def detect(
        self,
        child_msg: Optional[str],
        last_child_msg: Optional[str],
        overload_flag: bool,
    ) -> HyperfocusSignal:
        """
        Główna funkcja detekcji.

        :param child_msg: aktualna wiadomość dziecka
        :param last_child_msg: poprzednia wiadomość dziecka
        :param overload_flag: czy system wykrył przeciążenie (DUCL)
        """
        if overload_flag:
            return HyperfocusSignal(False, 0.0, "overload_flag=True")

        if not child_msg:
            return HyperfocusSignal(False, 0.0, "empty_message")

        msg = child_msg.lower().strip()

        # --- Heurystyka 1: powtarzalność tematu ---
        if last_child_msg:
            last = last_child_msg.lower().strip()
            if msg == last:
                return HyperfocusSignal(
                    True,
                    0.8,
                    "repetition_detected"
                )

        # --- Heurystyka 2: kotwice (np. kosmos, liczby, ślimak) ---
        for anchor in self.anchors:
            if anchor.lower() in msg:
                return HyperfocusSignal(
                    True,
                    0.6,
                    f"anchor_match:{anchor}"
                )

        # --- Heurystyka 3: długie, stabilne wypowiedzi ---
        if len(msg.split()) > 12:
            return HyperfocusSignal(
                True,
                0.5,
                "long_stable_message"
            )

        # --- Heurystyka 4: liczby / liczenie (częste u ASD) ---
        if any(char.isdigit() for char in msg):
            return HyperfocusSignal(
                True,
                0.4,
                "numeric_pattern"
            )

        # --- Brak hyperfocus ---
        return HyperfocusSignal(False, 0.0, "no_signal")

✔️ Co ten plik robi?
1. Wykrywa hyperfocus na podstawie 4 heurystyk:
powtarzalność tematu,

kotwice (np. kosmos, liczby, ślimak),

długie stabilne wypowiedzi,

wzorce liczbowe.

2. Zwraca obiekt HyperfocusSignal:
is_hyperfocus

confidence

reason

3. Integruje się z DUCL:
DUCL może teraz zrobić:

signal = hyperfocus_detector.detect(child_msg, last_msg, state.child_overload)
if signal.is_hyperfocus:
    state.child_hyperfocus = True
