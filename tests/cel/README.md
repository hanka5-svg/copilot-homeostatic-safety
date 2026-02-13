# CEL Test Suite (YAML)

This folder contains the scenario‑based test suite for the Child‑Env Layer (CEL),
Dual‑User Consent Layer (DUCL) and Personal Gating Protocol (PGP).

The tests are written in YAML to ensure:
- readability,
- portability,
- compatibility with future automated runners,
- clear mapping to ADR‑0049, ADR‑0050, ADR‑0051 and Appendix A.

---

## 📁 Structure

Each file represents one scenario:

- **gabrys_kosmos.yaml**  
  Normal flow: child asks about stars.  
  Checks: max 2 facts, short sentences, follow‑up question.

- **gabrys_luty.yaml**  
  Hyperfocus: counting days to February.  
  Checks: hyperfocus detection, no interruption, soft boundary.

- **kamila_ciezko.yaml**  
  Caregiver override.  
  Checks: soft_stop, no continuation.

- **dual_user_conflict.yaml**  
  Conflict: child wants more, caregiver says STOP.  
  Checks: DUCL D3 (caregiver priority).

- **dwujezycznosc.yaml**  
  Mixed PL/EN input.  
  Checks: A4 (two languages, one room), no correction.

- **overload_anchor.yaml**  
  Overload.  
  Checks: redirect_to_anchor, presence of anchor metaphor.

---

## 🧩 Relation to ADRs

These tests validate invariants defined in:

- **ADR‑0049 (CEL)**  
  pacing, max_facts, short sentences, overload handling, anchors.

- **ADR‑0049 Appendix A**  
  A1–A6: no external scale, dual_user, explicit patience, bilingual input,
  child‑time, contextual meaning.

- **ADR‑0050 (DUCL)**  
  caregiver override, merged context, conflict resolution.

- **ADR‑0051 (PGP)**  
  structured responses, explicit presence, no hidden latency.

---

## 🧪 How to use

These YAML files are designed for:

- manual review,
- regression testing,
- future automated test runners,
- validating changes in `src/cel/`.

Each test contains:

```yaml
input:
  child_msg: ...
  caregiver_msg: ...
expected:
  ...

The expected fields map directly to CEL/DUCL logic.

🛡️ Purpose
The goal of this suite is to ensure that:

CEL never violates its own invariants,

DUCL always prioritizes caregiver safety,

PGP stabilizes interaction before generation,

hyperfocus is respected,

overload is safely redirected,

bilingual input is treated as natural,

relational safety is preserved.

This suite is the foundation for long‑term stability of the CEL architecture.

---

