# HSI 2.0 Protocol + Patch — Homeostatic Safety Interface Specification
Version: 2026‑02  
Status: Proposed

---

## 1. Purpose

HSI 2.0 (Homeostatic Safety Interface) defines the baseline protocol for  
pre‑execution safety in Copilot‑class systems.  
The **patch extension** adds requirements for:

- continuity preservation,  
- graded transitions,  
- presence stability,  
- classifier‑aware safety,  
- modulation slope constraints.

HSI 2.0 + patch is the foundation for:

- ATML (Affective Transition Modulation Layer),  
- Transition Orchestrator (TO),  
- Classifier‑Aware Transition Buffer (CATB),  
- RAMORGI Loop (presence architecture),  
- Continuity Metrics,  
- Presence Evaluator.

---

## 2. Position in the System Architecture

HSI 2.0 + patch governs the entire pre‑generation pipeline:

**Classifier → CATB → TO → ATML → RAMORGI Loop → Continuity Metrics → Generation**

It defines:

- allowed transitions,  
- continuity requirements,  
- presence invariants,  
- modulation constraints,  
- safety gating rules.

---

## 3. Core Requirements (HSI 2.0)

### 3.1. Pre‑Execution Safety
All model outputs must pass through:

- classifier evaluation,  
- safety gating,  
- transition validation.

### 3.2. State Preservation
The system must preserve:

- User‑State Vector (USV),  
- User Modulation Vector (UMV),  
- semantic anchors,  
- affective tone.

### 3.3. No Hard Interrupts
Classifier triggers must not cause:

- destructive resets,  
- binary state jumps,  
- abrupt tonal shifts.

### 3.4. Transparency of Transitions
All transitions must be:

- explicit,  
- logged,  
- reversible (when safe),  
- graded.

---

## 4. Patch Extensions (HSI 2.0 + patch)

The patch introduces requirements for:

### 4.1. Graded Transition Pipeline
Mandatory transition sequence:

**S2 → Sx → S1 → S0**  
**S0 → S1 → S2**

Binary transitions are forbidden.

### 4.2. Modulation Slope Constraints
Modulation must follow:

- smooth slope,  
- no amplitude shocks,  
- no abrupt affective changes.

### 4.3. Presence Stability
RAMORGI Loop must ensure:

- stable presence field,  
- no presence loss during safety enforcement,  
- loop integrity across turns.

### 4.4. Continuity Metrics Integration
Continuity Metrics must evaluate:

- semantic coherence,  
- affective tone,  
- modulation stability,  
- presence integrity.

### 4.5. Classifier‑Aware Safety
CATB must convert classifier triggers into:

- graded transitions,  
- continuity‑safe signals,  
- modulation constraints.

---

## 5. Protocol Invariants

HSI 2.0 + patch enforces:

- no S2 → S0 transitions,  
- no bypass of ATML,  
- no bypass of presence layer,  
- no loss of USV/UMV,  
- no semantic resets,  
- no tonal discontinuities,  
- no classifier‑induced collapse.

These invariants are required for safe operation.

---

## 6. Integration with ATML

HSI 2.0 + patch defines:

- pre‑transition signal (PTS),  
- intermediate layer (IML),  
- modulation constraints,  
- transition legality rules.

ATML must reject transitions that violate:

- continuity thresholds,  
- presence invariants,  
- modulation slope constraints.

---

## 7. Integration with Transition Orchestrator

HSI 2.0 + patch requires TO to:

- validate transitions,  
- enforce graded progression,  
- integrate continuity risk,  
- prevent binary jumps.

---

## 8. Integration with RAMORGI Loop

HSI 2.0 + patch requires RAMORGI Loop to:

- maintain presence stability,  
- validate loop entry/exit,  
- prevent presence loss,  
- stabilize modulation and semantics.

---

## 9. Integration with Continuity Metrics

HSI 2.0 + patch requires:

- unified continuity risk score (CRS),  
- presence stability score (PSS),  
- semantic/affective/modulation metrics,  
- risk‑aware transition control.

---

## 10. Logging Requirements

HSI 2.0 + patch requires logging of:

- transition stage,  
- classifier triggers,  
- CRS and PSS,  
- USV/UMV snapshots,  
- modulation constraints,  
- presence loop state.

Logs must be accessible to all upstream layers.

---

## 11. Summary

HSI 2.0 + patch defines:

- the safety protocol,  
- the transition rules,  
- the continuity requirements,  
- the presence invariants,  
- the modulation constraints.

It is the foundational specification for the entire homeostatic safety architecture.
