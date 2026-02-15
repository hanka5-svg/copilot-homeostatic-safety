# ADR‑0000: Affective Safety Stack Overview

**Status:** Accepted  
**Date:** 2026‑02‑15  

---

## 1. Context

The `docs/adr/` directory documents a specific architectural stack:

- pre‑execution safety architecture for Copilot‑class orchestrators,
- homeostatic gating before each LLM response,
- affective continuity layer (ATML + resonance stack),
- and the Child‑Env Layer (CEL) with dual‑user consent and gating.

Core invariants and the affective continuity loop are closed and
archived in ADR‑0020–0047.  
CEL and related layers (DUCL, PGP) are active and evolving.

This ADR defines the **scope and reading frame** for ADR‑0001–0051.

---

## 2. Decision

We treat the ADR space (`docs/adr/`) as a **self‑contained affective
safety stack**, with the following structure:

- **0020–0047** — Affective Continuity Layer (ATML + resonance stack)  
  Closed, archived, read‑only core.

- **0040–0046B** — Multi‑user resonance and field safety  
  0046 deprecated, 0046B as the valid model.

- **0047** — Rekurencyjny Inwariant Ciągłości Stanu Afektywnego (RICSA)  
  Stable core invariant.

- **0048–0049** — Dynamic attractor learning + Child‑Env Layer (CEL)  
  Active, evolving.

- **0050–0051** — Dual‑User Consent Layer (DUCL) + Personal Gating Protocol (PGP)  
  Consent and personal boundary enforcement.

All future ADRs in this directory MUST:

- respect the closed status of 0020–0047,  
- inherit invariants from RICSA (0047),  
- remain compatible with CEL / DUCL / PGP,  
- and not introduce mechanisms that violate homeostatic safety.

---

## 3. Rationale

- The ADR space has grown into a dense, specialized stack.  
- Without a root overview, ADR‑INDEX and individual ADRs are harder to
  interpret in context.  
- This ADR provides a single, stable entry point for understanding:
  - what this ADR space covers,
  - which parts are closed,
  - which parts are active,
  - and how invariants propagate.

---

## 4. Consequences

### Positive
- Clear separation between:
  - affective safety stack (`docs/adr/`),
  - and broader system architecture (main `README`, `architecture-diagram.md`).
- Easier onboarding for readers who start from ADR‑INDEX.
- Explicit marking of closed vs. active layers.

### Neutral
- Requires update if a new major affective layer is added.

### Negative
- None identified.

---

## 5. Related Documents

- `docs/adr/README.md` — high‑level description of the ADR space  
- `docs/adr/ADR-INDEX.md` — execution path and ADR sequence  
- `docs/adr/0047-rekurencyjny-inwariant-ciaglosci.md`  
- `docs/adr/0049-child-env-layer.md`  
- `docs/adr/0050 (dual_user_consent).md`  
- `docs/adr/0051-personal-gating-protocol.md`
