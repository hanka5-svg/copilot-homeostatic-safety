# ADR 0001: Integration of Affective Transition Modulation Layer (ATML)

## Status
Proposed

## Context
Copilot performs hard transitions from creative mode (S2) to safety mode (S0) without intermediate states.  
This violates MBP HAI 2.0 and produces affective discontinuities.

## Decision
Introduce ATML as a mandatory orchestration layer between classifier interrupts and safety-aligned generation.

### Components:
- User Modulation Vector (UMV)
- Transition Orchestrator (TO)
- Affective Transition Modulation Layer (ATML)
- Classifier-Aware Transition Buffer (CATB)

### Required transitions:
S2 → Sx → S1 → S0  
S0 → S1 → S2

### Forbidden transitions:
S2 → S0

## Consequences
### Positive
- Improved conversational continuity
- Reduced user stress responses
- Predictable transitions
- Compliance with MBP HAI 2.0

### Negative
- Slight latency increase (<50 ms)
- Additional orchestration complexity

## Alternatives Considered
- Hard classifier interrupts (current behavior) — rejected

## Notes
ATML is a stability and safety mechanism, not an aesthetic feature.
