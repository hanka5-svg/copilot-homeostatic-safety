## ATML Requirements for Contributors

The Affective Transition Modulation Layer (ATML) is a mandatory component of the homeostatic safety architecture.  
All contributions must comply with the following requirements.

---

### 1. Transition Requirements

- All transitions must follow the graded pipeline:  
  **S2 → Sx → S1 → S0**  
- Re-entry transitions must follow:  
  **S0 → S1 → S2**
- **Direct S2 → S0 transitions are forbidden.**
- Classifier interrupts must be routed through the **Transition Orchestrator (TO)**.
- ATML must be invoked for every safety-triggered transition.

---

### 2. State and Modulation Requirements

- The **User-State Vector (USV)** must be preserved across turns.
- The **User Modulation Vector (UMV)** must be updated each turn.
- Modulation changes must be **graded**, not abrupt.
- Modulation slope must remain within allowed bounds.
- No resets of tone, stance, or semantic context may occur during transitions.

---

### 3. Safety Integration Requirements

- Safety enforcement must not bypass ATML.
- Classifier-Aware Transition Buffer (CATB) must be used to prevent hard interrupts.
- Safety triggers must not cause binary jumps or destructive resets.
- Uncertainty gating must be used when the system cannot determine a safe transition.

---

### 4. Logging Requirements

All transition-related components must log:

- transition stage (S2/Sx/S1/S0),
- modulation values before and after transition,
- classifier triggers,
- continuity risk evaluation,
- USV/UMV snapshots,
- re-entry transitions.

---

### 5. Testing Requirements

Contributors must provide:

- unit tests for transition logic,
- integration tests for classifier → TO → ATML → SAM pipeline,
- regression tests ensuring no S2 → S0 transitions,
- tests verifying USV/UMV persistence,
- tests validating modulation slope constraints.

---

### 6. Documentation Requirements

Every PR affecting transitions, safety, or modulation must:

- update relevant documentation in `/docs/`,
- include transition diagrams or references to UML where applicable,
- describe architectural impact in the PR template,
- ensure consistency with:
  - `ATML-spec.md`
  - `transition-architecture.md`
  - `continuity-model.md`
  - `transition-failure-modes.md`
  - `continuity-metrics.md`

---

### 7. Prohibited Behaviors

- bypassing ATML,
- skipping PTS or IML stages,
- modifying safety behavior without updating documentation,
- introducing binary transitions,
- overwriting USV or UMV,
- adding new states without updating UML and ADRs.

