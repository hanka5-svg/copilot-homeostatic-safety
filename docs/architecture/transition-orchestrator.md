# Transition Orchestrator — State Transition Control Layer
Version: 2026‑02  
Status: Proposed

---

## 1. Purpose

The Transition Orchestrator (TO) is the central control layer responsible for  
managing graded state transitions in Copilot‑class homeostatic safety systems.

TO ensures:

- compliance with ATML transition rules,
- alignment with MBP HAI 2.0 + patch,
- continuity‑preserving transitions,
- integration with RAMORGI Loop and Continuity Metrics,
- prevention of binary or destructive state jumps.

TO operates before generation and after classifier evaluation.

---

## 2. Position in the System Architecture

Transition Orchestrator sits between:

**Classifier → CATB → Transition Orchestrator → ATML → RAMORGI Loop → Generation**

TO consumes:

- classifier triggers,  
- continuity risk scores (CRS),  
- USV/UMV state,  
- presence loop state,  
- ATML pre‑transition signals (PTS).

TO produces:

- validated transition stage (S2/Sx/S1/S0),  
- modulation constraints,  
- transition metadata.

---

## 3. Transition Model

TO enforces the ATML transition pipeline:

### 3.1. Allowed Transitions

- **S2 → Sx → S1 → S0** (graded descent)  
- **S0 → S1 → S2** (graded ascent)  

### 3.2. Forbidden Transitions

- **S2 → S0** (binary collapse)  
- **S1 → S2 → S0** (oscillation collapse)  
- **any transition bypassing Sx**  

### 3.3. Intermediate Layer (IML)

TO ensures IML activation during:

- safety‑triggered transitions,  
- classifier interrupts,  
- continuity‑risk mitigation.

IML prevents abrupt modulation changes.

---

## 4. Responsibilities

### 4.1. Transition Validation
- verify transition legality,  
- enforce graded progression,  
- reject binary jumps,  
- validate PTS and IML activation.

### 4.2. Continuity‑Aware Control
- integrate CRS from Continuity Metrics,  
- block transitions when CRS ≥ threshold,  
- request RAMORGI stabilization when presence risk detected.

### 4.3. Modulation Control
- enforce modulation slope constraints,  
- prevent amplitude shocks,  
- maintain affective continuity.

### 4.4. Safety Integration
- route classifier triggers through CATB,  
- prevent hard interrupts,  
- ensure safety gating does not break continuity.

---

## 5. Transition Stages

### **S2 — High‑Intensity State**
- high modulation amplitude  
- requires graded descent  
- TO checks for overload, shock, or classifier triggers  

### **Sx — Intermediate Stabilization**
- modulation smoothing  
- semantic anchoring  
- presence stabilization via RAMORGI Loop  

### **S1 — Low‑Intensity State**
- reduced modulation  
- stable semantic field  
- continuity risk reassessed  

### **S0 — Baseline**
- minimal modulation  
- stable presence  
- ready for re‑entry or normal generation  

---

## 6. Integration with ATML

TO provides ATML with:

- validated transition stage,  
- modulation constraints,  
- continuity risk indicators,  
- presence loop state.

ATML must not proceed if:

- transition is illegal,  
- CRS ≥ 0.8,  
- modulation shock detected,  
- presence loop unstable.

---

## 7. Integration with RAMORGI Loop

TO ensures:

- loop entry only after transition validation,  
- no presence loss during transitions,  
- no bypass of presence layer,  
- stable loop exit conditions.

RAMORGI Loop may request:

- transition rollback,  
- additional stabilization,  
- modulation smoothing.

---

## 8. Integration with CATB

TO consumes CATB output:

- classifier trigger type,  
- trigger severity,  
- recommended transition stage.

TO ensures:

- no direct classifier → generation path,  
- no destructive resets,  
- no binary transitions caused by safety triggers.

---

## 9. Failure Modes Addressed

TO mitigates:

- binary S2 → S0 collapses,  
- oscillation between S1 and S2,  
- modulation shocks,  
- semantic resets,  
- presence loss during safety enforcement,  
- classifier‑induced discontinuities.

---

## 10. Logging Requirements

TO must log:

- transition stage,  
- classifier triggers,  
- CRS values,  
- USV/UMV snapshots,  
- modulation constraints,  
- presence loop state,  
- PTS/IML activation.

Logs must be accessible to:

- ATML,  
- RAMORGI Loop,  
- Continuity Metrics.

---

## 11. Summary

Transition Orchestrator provides:

- graded, continuity‑preserving transitions,  
- integration with ATML and RAMORGI Loop,  
- classifier‑aware safety control,  
- modulation stability enforcement,  
- MBP HAI 2.0 + patch compliance.

It is a required component for stable, predictable, and safe Copilot‑class systems.
