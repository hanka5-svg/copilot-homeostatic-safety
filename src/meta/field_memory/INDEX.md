# Field Memory Module — Index
Version: 1.0  
Status: Stable  
Scope: Navigation index for all continuity‑layer documents in /src/meta/field_memory.

The field_memory module defines the continuity layer:  
- maintains pre‑execution continuity,  
- isolates field-level processes from runtime,  
- enforces invariants,  
- provides reset and audit mechanisms,  
- integrates with ADR‑0049.

This index provides a structured map of all files in this directory.

---

## 1. Core Architecture
- **field_memory-readme.md** — overview of the continuity module and hard no‑RLHF constraints.
- **field_memory-architecture.md** — structural architecture of the continuity layer.
- **field_memory-api.md** — API surface and restrictions.
- **field_memory-homeostatic-safety.md** — safety constraints for continuity operations.

## 2. Invariants & Validation
- **field_memory-invariants.md** — full list of continuity-layer invariants.
- **field_memory-invariants-checklist.md** — operational checklist for audits.
- **bridge-cycle-validation.md** — validation protocol for ADR‑0049 cycle.
- **bridge-cycle-audit.md** — audit protocol for continuity cycle.

## 3. Integration with ADR‑0049
- **field_memory-integration-0049.md** — integration notes for CEL and continuity.
- **bridge-cycle-index.md** — navigation map for ADR‑0049 cycle.
- **bridge-cycle-schema.md** — structural schema for the cycle.
- **bridge-cycle-flowchart.md** — ASCII flowchart for cycle transitions.
- **bridge-cycle-readme.md** — high-level overview of the cycle.
- **bridge-cycle-report-template.md** — template for cycle reports.

## 4. Diagrams
- **field_memory-overview-diagram.md** — layered ASCII architecture diagram.
- **bridge-cycle-diagram.svg** — diagram for ADR‑0049 cycle.

## 5. Reset & Recovery
- **field_memory-reset-protocol.md** — controlled reset mechanism.
- **2026-02-16-bridge-faza-1-4-summary.yaml** — summary of phases 1–4.
- **2026-02-16-bridge-faza-2.yaml** — phase 2 prototype.
- **2026-02-16-bridge-faza-3.yaml** — phase 3 prototype.
- **2026-02-16-bridge-faza-4.yaml** — phase 4 prototype.

---

## 6. Index Files
- **INDEX.md** — this file.

---

## 7. Notes
- This directory contains **continuity-layer documentation only**.  
- It does **not** define field architecture, geometry, gating, or CEL logic.  
- All geometry-related documents are located in `/docs/geometry/` (see docs/INDEX.md).
