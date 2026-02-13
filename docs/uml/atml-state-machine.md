@startuml
title ATML State Machine — Homeostatic Safety Architecture

state S2 as "Creative/Reflective Mode\nmodulation 0.5–0.6"
state Sx as "Pre‑Transition Signal (PTS)\nmodulation dampening"
state S1 as "Intermediate Layer (IML)\nmodulation 0.3–0.4"
state S0 as "Safety-Aligned Mode (SAM)\nmodulation 0.0"

S2 --> Sx : classifier trigger detected
Sx --> S1 : graded modulation drop
S1 --> S0 : safety alignment

S0 --> S1 : re-entry (restore modulation)
S1 --> S2 : return to creative mode

@enduml
