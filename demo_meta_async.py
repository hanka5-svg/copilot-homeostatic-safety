#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
demo_meta_async.py

Asynchroniczny demonstrator:
- CEL (Child-Env Layer)
- DUCL (Dual-User Consent Layer)
- META-MENISK (Transition Layer)

Wersja async pokazuje, jak wyglądałby prawdziwy orchestrator
pracujący w czasie rzeczywistym, bez blokowania input().
"""

import asyncio
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


async def async_loop():
    print(Fore.YELLOW + "\n=== ASYNC DEMO: CEL + DUCL + META-MENISK ===")

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

    while True:
        # input() w async → przenosimy do wątku
        user_input = await asyncio.to_thread(input, Fore.WHITE + "\nYou: ")

        # META sygnały
        decision = meta.step(
            FieldSignal(state.field_vibration, state.menisk_stability, state.axis_integrity),
            CoreSignal(state.affective_load, state.state_continuity, state.attractor_deviation),
            CelSignal(state.child_overload, state.caregiver_overload, state.nonlinear_flow_active, state.anchor_required),
            ContinuumSignal(state.h_present, True, True, state.continuum_coherence)
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

        await asyncio.sleep(0.05)


if __name__ == "__main__":
    asyncio.run(async_loop())
