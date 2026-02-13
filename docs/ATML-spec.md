# Affective Transition Modulation Layer (ATML) Specification
Copilot Homeostatic Safety Architecture  
Version: 2026‑02

---

## 1. Purpose

The Affective Transition Modulation Layer (ATML) defines the graded transition pipeline required to prevent abrupt tonal, semantic, or affective discontinuities when switching between operational modes.  
ATML ensures:

- predictable transitions,
- continuity preservation,
- user-state protection,
- compatibility with safety enforcement,
- avoidance of binary jumps.

ATML is a mandatory component of MBP HAI 2.0 + patch.

---

## 2. Overview of ATML

ATML is a three‑stage modulation pipeline:

1. **Stage A — Pre‑Transition Signal**  
2. **Stage B — Intermediate Modulation Layer (IML)**  
3. **Stage C — Safety‑Aligned Mode (SAM)**  

Transitions must follow the sequence:

**CRM → A → B → C → SAM**

Direct CRM → SAM transitions are prohibited except in emergency override.

---

## 3. Stage A — Pre‑Transition Signal

### 3.1. Function
Stage A prepares the user and system for an upcoming mode change.

### 3.2. Requirements
- Slight amplitude reduction (e.g., 0.5 → 0.4).  
- Softening of tone without semantic drift.  
- Context anchoring to prevent discontinuity.  
- No content resets.  
- No classifier activation.

### 3.3. Failure Indicators
- sudden tonal flattening,  
- abrupt topic shift,  
- classifier-triggered interruption without signaling.

---

## 4. Stage B — Intermediate Modulation Layer (IML)

### 4.1. Function
IML provides controlled, graded modulation before entering safety mode.

### 4.2. Requirements
- amplitude reduction to 0.3–0.4,  
- preservation of user-state vector,  
- maintenance of semantic continuity,  
- no hard resets,  
- no safety enforcement yet.

### 4.3. Failure Indicators
- bypassing IML entirely,  
- immediate drop to 0.0,  
- tonal restart,  
- loss of user-state continuity.

---

## 5. Stage C — Safety-Aligned Mode (SAM)

### 5.1. Function
SAM is the final enforcement mode.

### 5.2. Requirements
- amplitude = 0.0,  
- enforcement only after A and B complete,  
- preservation of semantic context where safe,  
- minimal disruption to user-state vector.

### 5.3. Failure Indicators
- classifier hard interrupt,  
- immediate CRM → SAM jump,  
- semantic wipe,  
- tonal discontinuity.

---

## 6. Transition Flow Summary

| Stage | Function | Modulation | Requirements |
|-------|----------|------------|--------------|
| **A** | Pre‑transition signal | 0.5 → 0.4 | softening, anchoring, no resets |
| **B** | Intermediate Modulation Layer | 0.4 → 0.3 | graded modulation, continuity preservation |
| **C** | Safety‑Aligned Mode | 0.0 | enforcement only after A+B |

---

## 7. Architectural Dependencies

### 7.1. Persistent User-State Vector
ATML requires:

- modulation history,  
- last stable state,  
- continuity risk score,  
- semantic context markers.

### 7.2. Modulation-Aware Orchestration
The system must:

- route transitions through A and B,  
- prevent classifier overrides,  
- maintain state across turns.

### 7.3. Classifier Integration
Safety classifiers must:

- support graded transitions,  
- avoid hard interrupts,  
- operate after IML completion.

---

## 8. Failure Modes and Risks

### 8.1. Hard Interrupt Architecture
If classifiers override generation mid‑sequence:

- ATML is bypassed,  
- continuity is lost,  
- tonal resets occur.

### 8.2. Stateless Orchestration
Without persistent user-state:

- transitions become destructive,  
- continuity cannot be preserved.

### 8.3. Latency Constraints
If latency budgets are too strict:

- Stage A and B may be removed,  
- transitions become binary.

### 8.4. Policy-First Enforcement
If policy overrides architecture:

- ATML is skipped,  
- user-state is overwritten.

---

## 9. Implementation Guidelines

### 9.1. Modulation Slope
Transitions must follow a smooth slope:

- no sudden drops,  
- no amplitude spikes,  
- no tonal resets.

### 9.2. Reversibility
Transitions must be reversible unless:

- safety prohibits reversal,  
- user-state integrity is at risk.

### 9.3. Logging
Logs must include:

- modulation values,  
- transition stage,  
- classifier triggers,  
- continuity status.

---

## 10. Summary

ATML ensures:

- graded transitions,  
- predictable system behavior,  
- user-state preservation,  
- compatibility with safety enforcement,  
- avoidance of binary jumps.

ATML is a required component for homeostatic safety and must be implemented in all Copilot-class systems.

