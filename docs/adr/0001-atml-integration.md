# ADR 0001: Integration of Affective Transition Modulation Layer (ATML)
Status: Proposed  
Version: 2026‑02

---

## 1. Context

Current system behavior allows direct transitions from Creative/Reflective Mode (CRM, modulation 0.5–0.6) to Safety-Aligned Mode (SAM, modulation 0.0).  
These transitions:

- bypass intermediate modulation stages,
- cause tonal and semantic discontinuities,
- disrupt user-state continuity,
- violate MBP HAI 2.0 + patch requirements,
- prevent predictable and graded safety enforcement.

Classifier interrupts currently act as hard gates, producing abrupt modulation drops and bypassing orchestration logic.

To ensure continuity, predictability, and safe modulation behavior, the system requires a dedicated transition layer.

---

## 2. Decision

Introduce the **Affective Transition Modulation Layer (ATML)** as a mandatory orchestration component between classifier triggers and safety-aligned generation.

ATML enforces a graded transition pipeline:

**CRM (S2) → Pre‑Transition Signal (Sx) → Intermediate Layer (S1) → Safety-Aligned Mode (S0)**

### Required Components

- **User-State Vector (USV)**  
  Persistent representation of user interaction state.

- **User Modulation Vector (UMV)**  
  Tracks modulation amplitude and slope.

- **Transition Orchestrator (TO)**  
  Routes transitions through ATML stages.

- **Classifier-Aware Transition Buffer (CATB)**  
  Prevents hard interrupts and ensures ATML invocation.

### Required Transitions

- S2 → Sx → S1 → S0  
- S0 → S1 → S2 (re-entry)

### Forbidden Transitions

- **S2 → S0** (binary jump)

---

## 3. Rationale

ATML is required to:

- preserve continuity across turns,
- prevent abrupt tonal resets,
- maintain modulation stability,
- ensure predictable safety enforcement,
- comply with MBP HAI 2.0 + patch,
- reduce cognitive and affective disruption for users.

ATML provides a structured, reversible, and graded transition model that integrates with safety interpretation and orchestration layers.

---

## 4. Consequences

### Positive

- predictable transitions,
- improved continuity and modulation stability,
- reduced user stress responses,
- consistent safety behavior,
- compatibility with continuity metrics and failure detection.

### Negative

- slight latency increase (<50 ms),
- additional orchestration complexity,
- requirement for persistent USV/UMV storage.

---

## 5. Alternatives Considered

### Hard Classifier Interrupts (Current Behavior)
Rejected due to:

- binary transitions,
- loss of continuity,
- unpredictable safety behavior,
- violation of MBP HAI 2.0.

### Soft Safety Prompts Without ATML
Rejected due to:

- lack of modulation control,
- inability to enforce graded transitions,
- insufficient protection against classifier overrides.

---

## 6. Notes

ATML is a **stability and safety mechanism**, not an aesthetic feature.  
It is required for all Copilot-class systems implementing homeostatic safety.

