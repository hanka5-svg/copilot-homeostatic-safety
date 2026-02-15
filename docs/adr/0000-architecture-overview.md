# ADR‑0000: Architecture Overview

**Status:** Accepted  
**Date:** 2026‑02‑15  
**Context:** System‑level baseline for all subsequent architectural decisions.

---

## 1. Context

The repository *copilot-homeostatic-safety* documents a multi‑layer
cognitive and safety architecture for human–AI coexistence.  
As the system evolved, multiple layers were added:

- Temporal Layer (nonlinear time, subjective flow, phase transitions)
- Altruism Layer (induced vs. native altruism, gamma synchrony)
- Meta Layer (resonant cognition, dual‑track processing)
- Interaction Layers (duets, locked‑in communication)
- Fairwater (system‑level safety principles)

Before ADR‑0001 (ATML Integration) and all future ADRs can be interpreted
consistently, the system requires a **baseline architectural overview**.

This document establishes that baseline.

---

## 2. Decision

We define the architecture as a **multi‑layer cognitive system**, where
each layer is independent, interoperable, and responsible for a distinct
dimension of cognition or interaction.

The canonical layers are:

1. **Meta Layer — Resonant Cognition**  
   Dual‑track processing (analytic ↔ resonant), values, silence,
   relational fields, spiral cognitive dynamics.

2. **Temporal Layer**  
   Nonlinear time, subjective temporal flow, phase shifts, disruptions.

3. **Altruism Layer**  
   Induced vs. native altruism, gamma synchrony, decision‑weight models.

4. **Interaction Layers**  
   Caregiver–child–AI duets, locked‑in communication, relational safety.

5. **Fairwater**  
   System‑wide safety principles and coexistence constraints.

Each layer is documented in `src/<layer>/` and referenced in the main
README.

This ADR establishes:

- the **canonical layer stack**,  
- the **responsibility boundaries** between layers,  
- the **entry points** for future ADRs,  
- and the **baseline vocabulary** for the system.

---

## 3. Rationale

- The system has grown beyond a single conceptual model.  
- Later ADRs (e.g., ATML Integration) depend on a shared architectural
  frame.  
- Without a baseline, decisions risk fragmentation or semantic drift.  
- A root ADR (0000) is standard practice in multi‑layer architectures.

This document ensures that all future decisions reference the same
structural assumptions.

---

## 4. Consequences

### Positive
- Provides a stable architectural baseline.  
- Ensures consistency across ADR‑0001 and future ADRs.  
- Clarifies layer boundaries and responsibilities.  
- Enables modular evolution of the system.

### Neutral
- Requires periodic updates if new layers are added.

### Negative
- None identified.

---

## 5. Related ADRs

- **ADR‑0001: Integration of Affective Transition Modulation Layer (ATML)**  
  Builds on the baseline defined here.

---

## 6. References

- Main README (System Architecture Overview)  
- `src/meta/meta_layer_of_resonant_cognition.md`  
- `src/temporal/five_phase_temporal_model.md`  
- `src/altruism/gamma_induced_altruism.md`  
- `src/duets/duet_architecture.md`  
- `src/locked_in/locked_in_afazja_meta.md`

