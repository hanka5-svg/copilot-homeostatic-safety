# field_memory — continuity and homeostatic layer

## 1. Purpose
`field_memory` is a continuity module.  
It provides a stable, non-destructive memory layer for interactions and processes.

It is **not** a training dataset and **not** a feedback channel for RLHF or any
form of behavioral conditioning.

## 2. Design principles
- **Continuity:** preserve context across sessions without overwriting history.
- **Non-destructive:** no destructive writes, only append / structured snapshots.
- **No runtime training:** field_memory is never used to update model weights.
- **Homeostatic role:** support regulation and stability, not optimization by reward/punishment.
- **Local control:** designed to work with local / controlled models, not cloud training pipelines.

- ## No RLHF usage (hard constraints)

`field_memory` is explicitly prohibited from being used in any reinforcement,
reward-based, or behavior-conditioning training pipeline.

### Forbidden uses
- no reward scoring,
- no preference ranking,
- no human-feedback optimization,
- no gradient updates derived from user behavior,
- no fine-tuning loops using field_memory contents,
- no cloud-based moderation or training integration,
- no conversion of YAML traces into training datasets.

### Rationale
`field_memory` is a continuity and regulation layer.  
Using it for RLHF or any form of behavioral conditioning violates:
- continuity invariants,
- non-destructive guarantees,
- homeostatic architecture principles,
- the HOMEOSTATIC_CLAUSE at repo root.

### Enforcement
Any component attempting to:
- write reward signals,
- derive gradients,
- or integrate with RLHF pipelines

must be treated as a violation and blocked by invariants.


## 3. Relation to homeostatic architecture
`field_memory` is part of a homeostatic architecture:
- it stores structured traces of interactions (YAML),
- it supports bridge cycles (ADR-0049),
- it cooperates with reset protocol to restore safe baselines,
- it never participates in RLHF, scoring, or ranking of user behavior.

## 4. Invariants (summary)
- no RLHF usage,
- no reward / punishment loops,
- no cloud training integration,
- no runtime writes from untrusted components,
- deterministic, read-only access for models.

Details: `field_memory-invariants.md`

## 5. Integration
- bridge cycle: `bridge-cycle-*`
- reset: `field_memory-reset-protocol.md`
- homeostatic clause: `HOMEOSTATIC_CLAUSE.md` (repo root)

