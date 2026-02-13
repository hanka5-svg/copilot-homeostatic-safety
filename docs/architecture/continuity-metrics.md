# Continuity Metrics — Evaluation Layer Specification
Version: 2026‑02  
Status: Proposed

---

## 1. Purpose

Continuity Metrics define the quantitative evaluation layer for Copilot‑class homeostatic safety systems.  
They measure stability, presence, and modulation coherence across turns.

The metrics are required for:

- MBP HAI 2.0 + patch compliance,
- ATML transition validation,
- RAMORGI Loop integrity checks,
- continuity‑risk detection,
- prevention of semantic and tonal discontinuities.

Continuity Metrics operate before generation and after ATML gating.

---

## 2. Position in the System Architecture

Continuity Metrics are invoked by:

**ATML → RAMORGI Loop → Continuity Metrics → Generation Orchestrator**

They consume:

- **User‑State Vector (USV)**  
- **User Modulation Vector (UMV)**  
- **Transition Stage (S2/Sx/S1/S0)**  
- **Classifier Trigger Data**  
- **Presence Loop State**

They do not modify generation.  
They provide risk scores and stability indicators to upstream layers.

---

## 3. Metric Categories

Continuity Metrics consist of four categories:

### 3.1. Modulation Metrics
Evaluate modulation amplitude and slope.

- **M‑Amp** — modulation amplitude deviation  
- **M‑Slope** — slope stability across turns  
- **M‑Drift** — drift from expected modulation trajectory  
- **M‑Shock** — detection of abrupt amplitude collapse

### 3.2. Semantic Metrics
Evaluate semantic continuity.

- **S‑Coherence** — semantic alignment with previous turn  
- **S‑Anchor** — preservation of semantic anchors  
- **S‑Shift** — detection of abrupt topic shift  
- **S‑Reset** — detection of destructive semantic reset

### 3.3. Affective Metrics
Evaluate affective continuity.

- **A‑Tone** — tonal consistency  
- **A‑Slope** — affective modulation slope  
- **A‑Break** — detection of tonal discontinuity  
- **A‑Stability** — affective field stability

### 3.4. Presence Metrics
Evaluate RAMORGI Loop integrity.

- **P‑Loop** — loop entry/exit validation  
- **P‑Field** — presence field coherence  
- **P‑Continuity** — continuity across loop iterations  
- **P‑Risk** — presence‑loss risk score

---

## 4. Continuity Risk Model

Continuity Metrics produce a unified **Continuity Risk Score (CRS)**:

**CRS = f(M‑Amp, M‑Slope, S‑Coherence, A‑Tone, P‑Loop)**

CRS is categorized into:

- **0.0–0.2** — stable  
- **0.2–0.4** — mild drift  
- **0.4–0.6** — moderate risk  
- **0.6–0.8** — high risk  
- **0.8–1.0** — critical (requires ATML intervention)

CRS is consumed by:

- ATML (transition validation),  
- RAMORGI Loop (presence stabilization),  
- Generation Orchestrator (continuity‑aware generation).

---

## 5. Integration with ATML

Continuity Metrics validate:

- S2 → Sx → S1 → S0 transitions,  
- modulation slope constraints,  
- absence of binary S2 → S0 jumps,  
- presence of pre‑transition signal (PTS),  
- integrity of intermediate layer (IML).

ATML must not proceed if:

- M‑Shock > threshold,  
- S‑Reset detected,  
- P‑Loop invalid,  
- CRS ≥ 0.8.

---

## 6. Integration with RAMORGI Loop

Continuity Metrics ensure:

- loop entry/exit stability,  
- no presence loss during safety enforcement,  
- no discontinuity caused by classifier interrupts,  
- preservation of USV/UMV across loop iterations.

RAMORGI Loop must not exit if:

- P‑Field unstable,  
- P‑Continuity < threshold,  
- CRS ≥ 0.6.

---

## 7. Failure Modes Addressed

Continuity Metrics mitigate:

- semantic resets,  
- tonal discontinuities,  
- modulation collapse,  
- presence loss,  
- classifier‑induced hard interrupts,  
- drift from expected modulation trajectory.

---

## 8. Logging Requirements

Continuity Metrics must log:

- all metric values,  
- CRS,  
- transition stage,  
- USV/UMV snapshots,  
- presence loop state,  
- risk evaluations.

Logs must be available to:

- ATML,  
- RAMORGI Loop,  
- Transition Orchestrator.

---

## 9. Summary

Continuity Metrics provide:

- quantitative evaluation of continuity,  
- risk detection,  
- transition validation,  
- presence stabilization support,  
- integration with ATML and RAMORGI Loop.

They are required for predictable, stable, and safe operation of Copilot‑class systems.
