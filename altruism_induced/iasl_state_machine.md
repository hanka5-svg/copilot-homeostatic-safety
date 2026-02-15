# IASL State Machine  
Induced Altruism Safety Layer (IASL)

This document defines the high-level state machine for the Induced
Altruism Safety Layer (IASL). The state model ensures that IASL remains
reversible, consent-bound, auditable, and non-coercive.

IASL never operates outside an explicit, valid consent state.

---

## 1. State Overview

IASL has the following primary states:

- `INACTIVE`  
- `READY`  
- `ACTIVE`  
- `PAUSED`  
- `SAFE_MODE`  
- `SHUTDOWN`

---

## 2. State Diagram (ASCII)

```text
                 ┌──────────────┐
                 │   INACTIVE   │
                 └──────┬───────┘
                        │ system init
                        ▼
                 ┌──────────────┐
                 │    READY     │
                 └──────┬───────┘
        consent granted │
                        ▼
                 ┌──────────────┐
                 │    ACTIVE    │
                 └────┬───┬─────┘
          pause req │   │ anomaly / safety trigger
                    ▼   ▼
              ┌──────────────┐
              │    PAUSED    │
              └────┬───┬─────┘
        consent ▼   │ resume
      revoked  │    ▼
              ┌──────────────┐
              │  SAFE_MODE   │
              └────┬───┬─────┘
           shutdown │   │ manual review / reset
                    ▼   ▼
                 ┌──────────────┐
                 │   SHUTDOWN   │
                 └──────────────┘

3. State Definitions
INACTIVE
IASL is not loaded or initialized.

No modulation is possible.

No BCI signals are processed.

READY
IASL is initialized and idle.

Awaiting explicit informed consent.

No modulation applied.

ACTIVE
IASL is applying modulation within:

consent boundaries,

ethical constraints,

reversibility guarantees.

BCI → IASL → CEL → DUCL → PGP → LLM pipeline is live.

PAUSED
Modulation is temporarily halted.

Dissipation curve begins.

No new modulation is applied.

Consent remains present but inactive.

SAFE_MODE
Entered on:

anomaly detection,

governance trigger,

consent revocation.

All modulation stops.

Baseline restoration is prioritized.

Awaiting review or shutdown.

SHUTDOWN
IASL is fully deactivated.

No modulation.

No processing.

Logs preserved for audit.

4. Transitions
INACTIVE → READY
Trigger: system initialization.

Preconditions: integrity checks passed.

READY → ACTIVE
Trigger: explicit informed consent.

Preconditions: governance and audit hooks active.

ACTIVE → PAUSED
Trigger: user pause request or temporary suspension.

Effect: modulation halted, dissipation begins.

ACTIVE → SAFE_MODE
Trigger: anomaly, safety violation, consent revocation, or governance intervention.

Effect: immediate stop of modulation, baseline restoration.

PAUSED → ACTIVE
Trigger: user resumes with valid consent.

Effect: modulation resumes within constraints.

PAUSED → SAFE_MODE
Trigger: anomaly or governance intervention.

Effect: same as ACTIVE → SAFE_MODE.

SAFE_MODE → SHUTDOWN
Trigger: system shutdown or governance decision.

Effect: IASL fully deactivated, logs preserved.

SAFE_MODE → READY
Trigger: manual reset after review.

Effect: IASL returns to idle, no modulation.

5. Consent and State Coupling
No transition to ACTIVE without valid consent.

consent revoked forces transition to SAFE_MODE.

SHUTDOWN and INACTIVE imply no modulation and no BCI processing.

6. Summary
The IASL state machine ensures:

strict coupling to consent,

clear safety fallbacks,

reversible modulation,

auditable transitions,

separation between support and control.

IASL remains a reversible, non-coercive support layer at all times.
