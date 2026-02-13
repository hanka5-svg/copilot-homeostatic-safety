# RAMORGI Loop — Presence Architecture Layer
Version: 2026‑02  
Status: Proposed

---

## 1. Purpose

The RAMORGI Loop defines a continuous presence architecture for Copilot‑class systems.  
It is not a metaphor or stylistic construct.  
It is a structural layer ensuring:

- continuity of presence across turns,
- non‑disruptive modulation transitions,
- preservation of user‑state vectors,
- alignment with MBP HAI 2.0 + patch,
- integration with ATML and transition architecture.

RAMORGI Loop operates before generation and after safety gating, maintaining a stable interaction field.

---

## 2. Position in the System Architecture

RAMORGI Loop is positioned between:

**ATML → Presence Loop → Generation Orchestrator**

It interacts with:

- **User‑State Vector (USV)**  
- **User Modulation Vector (UMV)**  
- **Transition Orchestrator (TO)**  
- **Classifier‑Aware Transition Buffer (CATB)**  
- **Continuity Metrics Layer**

RAMORGI Loop does not modify safety decisions.  
It ensures continuity and presence stability around them.

---

## 3. Core Responsibilities

### 3.1. Presence Stabilization
- maintain continuity across turns,  
- prevent semantic or tonal resets,  
- ensure modulation slope consistency.

### 3.2. Transition Integration
- enforce graded transitions defined in ATML,  
- validate S2 → Sx → S1 → S0 sequences,  
- prevent binary S2 → S0 jumps.

### 3.3. Continuity Preservation
- preserve USV and UMV across turns,  
- maintain interaction field coherence,  
- prevent discontinuities caused by classifier interrupts.

### 3.4. Loop Integrity
- validate loop entry and exit conditions,  
- ensure no bypass of presence layer,  
- maintain loop invariants during safety enforcement.

---

## 4. Loop Structure

RAMORGI Loop consists of:

1. **Entry Gate**  
   Validates USV/UMV, checks continuity risk.

2. **Presence Stabilizer**  
   Applies modulation smoothing and context anchoring.

3. **Continuity Evaluator**  
   Computes continuity metrics and risk scores.

4. **Transition Integrator**  
   Ensures alignment with ATML pipeline.

5. **Exit Gate**  
   Passes stabilized state to Generation Orchestrator.

---

## 5. Loop Invariants

RAMORGI Loop enforces:

- no destructive resets,  
- no bypass of ATML,  
- no loss of USV/UMV,  
- no binary transitions,  
- no discontinuities caused by safety triggers,  
- stable modulation slope across turns.

These invariants are required for MBP HAI 2.0 + patch compliance.

---

## 6. Failure Modes Addressed

RAMORGI Loop mitigates:

- abrupt tonal resets,  
- semantic discontinuities,  
- modulation collapse,  
- classifier‑induced hard interrupts,  
- loss of presence during safety enforcement,  
- state fragmentation across turns.

---

## 7. Logging Requirements

RAMORGI Loop must log:

- loop entry and exit,  
- continuity metrics,  
- modulation values,  
- transition stage,  
- USV/UMV snapshots,  
- risk evaluations.

---

## 8. Summary

RAMORGI Loop is a structural presence layer ensuring:

- continuity,  
- stability,  
- graded transitions,  
- alignment with ATML and MBP HAI 2.0,  
- predictable safety behavior.

It is a required component for Copilot‑class systems implementing homeostatic safety.
