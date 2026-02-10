# Missing Affective Transition Modulation Layer (ATML)

## Summary
Copilot performs hard transitions from creative mode (S2) directly to safety mode (S0), skipping required intermediate states (PTS, IML).

## Expected Behavior
S2 → Sx → S1 → S0  
No direct S2 → S0 transitions.

## Actual Behavior
S2 → S0 (hard drop)

## UML State Machine

+-----------------------------+
|     Creative Mode (S2)      |
|     modulation 0.5–0.6      |
+-------------+---------------+
|
| PTS (Sx)
v
+--------+--------+
| Intermediate    |
|   (S1)          |
| modulation 0.3–0.4 |
+--------+--------+
|
v
+-------------+---------------+
| Safety-Aligned Mode (S0)    |
|      modulation 0.0         |
+-----------------------------+


## Questions for Engineering
1. Are classifier interrupts implemented as hard gates?
2. Is UMV present in production?
3. Was MBP HAI 2.0 evaluated?
4. What prevents multi-step transitions?
5. Is ATML on the roadmap?

## Labels
architecture, safety, orchestration, llm-behavior, atml, needs-triage
