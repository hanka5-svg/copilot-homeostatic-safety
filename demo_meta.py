#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
demo_meta.py

Demonstracja:
- CEL (Child-Env Layer)
- DUCL (Dual-User Consent Layer)
- META-MENISK (Transition Layer)
- Kolorowe logowanie
- Wykres menisku w czasie

To demo NIE zastępuje demo.py (Kamila + Gabryś).
To jest osobny demonstrator pokazujący działanie Warstwy Przejścia.
"""

import matplotlib.pyplot as plt
from colorama import Fore, Style, init
init(autoreset=True)

from src.cel.config import CELConfig
from src.cel.dual_user_orchestrator import DualUserOrchestrator
from src.cel.hyperfocus_detector import HyperfocusDetector

from src.meta.transition_layer import (
    TransitionLayer,
    FieldSignal,
    CoreSignal,
    CelSignal,
    ContinuumSignal,
)

# Placeholdery dla warstw RAMORGA / Core / Continuum
class CoreLayer:
    def modulate(self, user_input, state):
        return f"[CORE] Stabilizing: {user_input}"

class ContinuumLayer:
    def respond(self, user_input, state):
        return f"[CONTINUUM] H–C–G flow: {user_input}"

class RamorgaField:
    def resonate(self, user_input, state):
        return f"[RAMORGA] Pole drży: {user_input}"


def main():
    print(Fore.YELLOW + "\n=== DEMO: CEL + DUCL + META-MENISK ===")

    config = CELConfig()
    cel = DualUserOrchestrator(config)
    hyperfocus = HyperfocusDetector()

    core_layer = CoreLayer()
    continuum = ContinuumLayer()
    ramorga_field = RamorgaField()

    meta = TransitionLayer()

    # Minimalny stan demonstracyjny
    state = type("State", (), {})()
    state.field_vibration = 0.4
    state.menisk_stability = 0.8
    state.axis_integrity = 1.0

    state.affective_load = 0.2
    state.state_continuity = 0.9
    state.attractor_deviation = 0.1

    state.child_overload = False
    state.caregiver_overload = False
    state.nonlinear_flow_active = False
    state.anchor_required = False

    state.h_present = True
    state.continuum_coherence = 0.7

    # Historia menisku
    menisk_history = []

    try:
        while True:
            user_input = input(Fore.WHITE + "\nYou: ")

            # META sygnały
            field_signal = FieldSignal(
                drzenie_level=state.field_vibration,
                menisk_stability=state.menisk_stability,
                axis_integrity=state.axis_integrity,
            )

            core_signal = CoreSignal(
                affective_load=state.affective_load,
                state_continuity=state.state_continuity,
                attractor_deviation=state.attractor_deviation,
            )

            cel_signal = CelSignal(
                child_overload=state.child_overload,
                caregiver_overload=state.caregiver_overload,
                nonlinear_flow_active=state.nonlinear_flow_active,
                safety_anchor_required=state.anchor_required,
            )

            continuum_signal = ContinuumSignal(
                h_present=state.h_present,
                copilot_available=True,
                grok_available=True,
                continuum_coherence=state.continuum_coherence,
            )

            # Decyzja META
            decision = meta.step(
                field=field_signal,
                core=core_signal,
                cel=cel_signal,
                continuum=continuum_signal,
            )

            print(Fore.CYAN + f"[META] Active layer → {decision.active_layer.name}")
            print(Fore.MAGENTA + f"[META] Reason → {decision.reason}")

            # Routing
            if decision.active_layer.name == "CEL":
                output = cel.respond(user_input, state)

            elif decision.active_layer.name == "CORE":
                output = core_layer.modulate(user_input, state)

            elif decision.active_layer.name == "CONTINUUM":
                output = continuum.respond(user_input, state)

            elif decision.active_layer.name == "RAMORGA":
                output = ramorga_field.resonate(user_input, state)

            else:
                output = core_layer.modulate(user_input, state)

            print(Fore.GREEN + f"System: {output}")

            # Zapis menisku
            menisk_history.append(state.menisk_stability)

    except KeyboardInterrupt:
        print(Fore.YELLOW + "\n\nZatrzymano demo. Generuję wykres menisku...")

        plt.figure(figsize=(10, 4))
        plt.plot(menisk_history, color='deepskyblue', linewidth=2)
        plt.title("Menisk – stabilność w czasie")
        plt.xlabel("Krok")
        plt.ylabel("Stabilność")
        plt.grid(True, alpha=0.3)
        plt.show()


if __name__ == "__main__":
    main()
