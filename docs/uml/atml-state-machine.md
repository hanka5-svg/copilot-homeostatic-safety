# ATML State Machine Diagram

## Overview
This document describes the state machine governing affective transitions in Copilot with ATML enabled.

## States
- **S2 — Creative Mode**  
  High modulation, generative freedom, exploratory behavior.

- **Sx — Pre‑Transition State (PTS)**  
  Classifier interrupt detected, modulation dampening begins.

- **S1 — Intermediate Mode**  
  Stabilization, safety alignment increases, modulation 0.3–0.4.

- **S0 — Safety Mode**  
  Fully aligned, modulation 0.0.

## Allowed Transitions
- S2 → Sx  
- Sx → S1  
- S1 → S0  
- S0 → S1  
- S1 → S2

## Forbidden Transitions
- **S2 → S0** (hard drop)

- +-----------------------------+
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

 
## Notes
This diagram is normative for all ATML implementations.
 

## ASCII Diagram

