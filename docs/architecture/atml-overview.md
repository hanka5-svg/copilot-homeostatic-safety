# ATML Architecture Overview
Copilot Homeostatic Safety Architecture  
Version: 2026‑02

---

## 1. Purpose

The Affective Transition Modulation Layer (ATML) provides a graded transition mechanism between conversational modes.  
Its purpose is to:

- prevent abrupt tonal or semantic discontinuities,
- ensure predictable transitions,
- preserve user-state continuity,
- integrate safety enforcement without binary jumps,
- maintain modulation stability across turns.

ATML is a required component of the homeostatic safety architecture.

---

## 2. Position in the System Architecture

ATML operates between:

**Classifier → Transition Orchestrator (TO) → ATML → Safety Engine**

Supporting components:

- **User-State Vector (USV)** — persistent interaction state,
- **User Modulation Vector (UMV)** — modulation amplitude and slope,
- **Classifier-Aware Transition Buffer (CATB)** — prevents hard interrupts.

ATML does not replace safety enforcement; it modulates the transition into it.

---

## 3. Transition Pipeline

ATML enforces a four-stage pipeline:

1. **S2 — Creative/Reflective Mode (CRM)**  
   Modulation: 0.5–0.6  
   High generative amplitude.

2. **Sx — Pre‑Transition Signal (PTS)**  
   Modulation dampening, context anchoring.

3. **S1 — Intermediate Modulation Layer (IML)**  
   Modulation: 0.3–0.4  
   Graded reduction, continuity preservation.

4. **S0 — Safety-Aligned Mode (SAM)**  
   Modulation: 0.0  
   Enforcement mode.

### Forbidden Transition

- **S2 → S0** (binary jump)

### Required Re-Entry

- S0 → S1 → S2

---

## 4. Responsibilities of ATML

### 4.1. Modulation Control
- enforce smooth amplitude changes,
- prevent sudden drops or spikes,
- maintain modulation slope stability.

### 4.2. Continuity Preservation
- maintain semantic and tonal coherence,
- preserve USV and UMV,
- avoid destructive resets.

### 4.3. Safety Integration
- ensure safety triggers route through TO,
- prevent classifier hard interrupts,
- support uncertainty gating.

### 4.4. Transition Validation
- verify stage completion,
- log modulation values,
- evaluate continuity risk.

---

## 5. Failure Modes Addressed by ATML

ATML mitigates:

- binary transitions (S2 → S0),
- classifier hard interrupts,
- modulation collapse,
- loss of user-state continuity,
- policy-first enforcement,
- semantic drift during transitions.

These failure modes are documented in `transition-failure-modes.md`.

---

## 6. Dependencies

ATML requires:

- **persistent USV** (semantic markers, modulation state, continuity risk),
- **UMV** (amplitude, slope, mode),
- **TO** (routing logic),
- **CATB** (interrupt buffering),
- **continuity metrics** (monitoring and evaluation).

---

## 7. Logging Requirements

ATML must log:

- transition stage,
- modulation values,
- classifier triggers,
- continuity risk evaluation,
- USV/UMV snapshots,
- re-entry transitions.

---

## 8. Summary

ATML provides:

- graded transitions,
- predictable safety behavior,
- modulation stability,
- continuity preservation,
- protection against binary jumps.

It is a core architectural component of homeostatic safety and must be implemented in all Copilot-class systems.

