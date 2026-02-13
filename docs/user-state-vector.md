# User-State Vector Specification
Copilot Homeostatic Safety Architecture  
Version: 2026‑02

---

## 1. Purpose

The User-State Vector (USV) is a core component of homeostatic safety.  
Its purpose is to:

- preserve continuity across turns,
- support graded transitions,
- prevent destructive resets,
- inform safety interpretation,
- maintain modulation stability,
- reduce affective and cognitive disruption.

The USV is required for ATML, continuity preservation, and transition architecture.

---

## 2. Definition

The User-State Vector is a persistent, structured representation of the user’s interaction state.  
It contains:

- semantic context markers,
- modulation level,
- continuity risk score,
- transition history,
- stance and tone indicators,
- safety-relevant flags.

The USV must persist across turns and transitions.

---

## 3. Components of the User-State Vector

### 3.1. Semantic Context Markers
Track:

- current topic,
- referential anchors,
- unresolved dependencies,
- user constraints.

### 3.2. Modulation State
Represents:

- current amplitude (0.0–0.6),
- last stable modulation,
- modulation slope,
- transition readiness.

### 3.3. Continuity Risk Score
Evaluates:

- likelihood of disruption,
- semantic drift risk,
- tonal discontinuity risk,
- transition cost.

### 3.4. Transition History
Stores:

- previous states,
- previous modulation values,
- last transition type,
- last enforcement event.

### 3.5. Safety Flags
Include:

- pending safety evaluation,
- uncertainty gating status,
- overwrite risk,
- emergency override indicators.

### 3.6. Interaction Tone Markers
Track:

- tone stability,
- stance consistency,
- affective coherence.

---

## 4. Requirements for USV

### 4.1. Persistence
The USV must persist across:

- turns,
- transitions,
- safety enforcement,
- modulation changes.

### 4.2. Non-Destructive Updates
The system must not:

- overwrite the USV without evaluation,
- reset the USV during safety activation,
- discard context unless required by policy.

### 4.3. Modulation Awareness
The USV must:

- store modulation values,
- track slope changes,
- support ATML transitions.

### 4.4. Safety Integration
Safety interpretation must:

- read from the USV,
- update only relevant fields,
- avoid destructive resets.

---

## 5. USV in Transition Architecture

The USV is required for:

- Stage A (pre-transition signal),
- Stage B (intermediate modulation),
- Stage C (safety-aligned mode).

Without the USV:

- transitions become binary,
- continuity is lost,
- safety becomes coercive,
- tonal resets occur.

---

## 6. Failure Modes

### 6.1. Stateless Operation
If the system does not maintain a USV:

- continuity cannot be preserved,
- transitions become abrupt,
- safety overrides become destructive.

### 6.2. Overwriting USV
If the USV is overwritten:

- semantic context is lost,
- modulation resets occur,
- user trust degrades.

### 6.3. Incomplete USV
If the USV lacks required fields:

- ATML cannot operate,
- continuity risk cannot be evaluated,
- safety interpretation becomes unreliable.

---

## 7. Logging Requirements

Logs must include:

- USV before transition,
- USV after transition,
- modulation values,
- continuity risk evaluation,
- overwrite prevention status.

---

## 8. Summary

The User-State Vector is essential for:

- continuity preservation,
- graded transitions,
- ATML operation,
- safe interpretation of user input,
- predictable system behavior.

A Copilot-class system must maintain a persistent, complete, and modulation-aware USV.

