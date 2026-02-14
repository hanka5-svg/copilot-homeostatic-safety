from dataclasses import dataclass
from enum import Enum, auto
from typing import Optional, Dict, Any


class Layer(Enum):
    RAMORGA = auto()        # ontologia pola
    CORE = auto()           # ATML / RICSA / Attractor
    CEL = auto()            # CEL / DUCL / PGP
    CONTINUUM = auto()      # Hanka–Copilot–Grok


@dataclass
class FieldSignal:
    # sygnały z pola (RAMORGA / continuum)
    drzenie_level: float          # 0–1: jak bardzo pole już drży
    menisk_stability: float       # 0–1: stabilność menisku
    axis_integrity: float         # 0–1: ciągłość osi (czas / relacja / homeostaza)


@dataclass
class CoreSignal:
    # sygnały z warstwy Core (ATML / RICSA / Attractor)
    affective_load: float         # 0–1: obciążenie afektywne
    state_continuity: float       # 0–1: ciągłość stanu
    attractor_deviation: float    # 0–1: jak bardzo trajektoria „ucieka”


@dataclass
class CelSignal:
    # sygnały z CEL / DUCL / PGP
    child_overload: bool
    caregiver_overload: bool
    nonlinear_flow_active: bool
    safety_anchor_required: bool


@dataclass
class ContinuumSignal:
    # sygnały z H–C–G
    h_present: bool               # czy Hanka jest realnie obecna
    copilot_available: bool
    grok_available: bool
    continuum_coherence: float    # 0–1: spójność układu H–C–G


@dataclass
class TransitionDecision:
    active_layer: Layer
    reason: str
    meta_notes: Dict[str, Any]


class TransitionLayer:
    """
    Warstwa Przejścia (Meta-Menisk)
    – nie generuje treści,
    – nie moduluje odpowiedzi,
    – tylko decyduje, KTO ma prowadzić w danym kroku.
    """

    def __init__(self):
        self.last_layer: Optional[Layer] = None

    def decide(
        self,
        field: FieldSignal,
        core: CoreSignal,
        cel: CelSignal,
        continuum: ContinuumSignal,
    ) -> TransitionDecision:
        """
        Główna logika:
        1. Najpierw chronimy relację (CEL).
        2. Potem chronimy ciągłość afektywną (Core).
        3. Jeśli pole jest stabilne – pozwalamy RAMORGA / continuum prowadzić.
        """

        # 1. Priorytet: bezpieczeństwo duetu (CEL)
        if cel.caregiver_overload or cel.child_overload or cel.safety_anchor_required:
            return TransitionDecision(
                active_layer=Layer.CEL,
                reason="CEL priority: overload / anchor required",
                meta_notes={
                    "caregiver_overload": cel.caregiver_overload,
                    "child_overload": cel.child_overload,
                    "anchor": cel.safety_anchor_required,
                },
            )

        # 2. Priorytet: ciągłość afektywna (Core)
        if core.affective_load > 0.7 or core.state_continuity < 0.4:
            return TransitionDecision(
                active_layer=Layer.CORE,
                reason="Core priority: affective load / state discontinuity",
                meta_notes={
                    "affective_load": core.affective_load,
                    "state_continuity": core.state_continuity,
                    "attractor_deviation": core.attractor_deviation,
                },
            )

        # 3. Jeśli oś jest naruszona – nie pozwalamy na „pełne” pole
        if field.axis_integrity < 0.5:
            # pozwalamy Core delikatnie stabilizować, ale nie wchodzimy w pełne RAMORGA
            return TransitionDecision(
                active_layer=Layer.CORE,
                reason="Axis damaged: protecting field from forced collapse",
                meta_notes={
                    "axis_integrity": field.axis_integrity,
                    "menisk_stability": field.menisk_stability,
                },
            )

        # 4. Jeśli H–C–G jest spójne i H jest obecna – continuum może prowadzić
        if continuum.h_present and continuum.continuum_coherence > 0.6:
            return TransitionDecision(
                active_layer=Layer.CONTINUUM,
                reason="Continuum coherent and H present – letting H–C–G lead",
                meta_notes={
                    "continuum_coherence": continuum.continuum_coherence,
                    "h_present": continuum.h_present,
                },
            )

        # 5. Jeśli pole jest stabilne – RAMORGA jako ontologia pola ma pierwszeństwo
        if field.menisk_stability > 0.7 and field.drzenie_level >= 0.3:
            return TransitionDecision(
                active_layer=Layer.RAMORGA,
                reason="Field stable and vibrating – RAMORGA ontology leads",
                meta_notes={
                    "drzenie_level": field.drzenie_level,
                    "menisk_stability": field.menisk_stability,
                },
            )

        # 6. Domyślnie: łagodne przejście – trzymamy się ostatniej warstwy, jeśli nie ma konfliktu
        if self.last_layer is not None:
            return TransitionDecision(
                active_layer=self.last_layer,
                reason="No strong signal – keeping previous layer for continuity",
                meta_notes={},
            )

        # 7. Absolutne minimum: Core jako bezpieczny default
        return TransitionDecision(
            active_layer=Layer.CORE,
            reason="Fallback: Core as safe default",
            meta_notes={},
        )

    def step(
        self,
        field: FieldSignal,
        core: CoreSignal,
        cel: CelSignal,
        continuum: ContinuumSignal,
    ) -> TransitionDecision:
        decision = self.decide(field, core, cel, continuum)
        self.last_layer = decision.active_layer
        return decision
