# 🌼cel — Non‑Linear Test & Exploration Layer

This folder contains the **non‑linear**, **neuroinclusive** and **meta‑architectural**
test space for CEL/DUCL/PGP.  
It is intentionally separated from the main `src/cel/` implementation.

The purpose of 🌼cel is to provide a safe sandbox for:
- exploratory test cases,
- non‑linear interaction patterns,
- stress and overload simulations,
- failure‑mode analysis,
- DUETY scenarios,
- meta‑architecture validation,
- regression and edge‑case testing.

🌼cel is **not** production code.  
It is a **research layer** that complements the deterministic CEL logic.

---

## Why a separate folder?

The main `src/cel/` directory contains:
- core CEL implementation,
- deterministic heuristics,
- orchestrators,
- configuration,
- linear test examples.

The 🌼cel directory contains:
- non‑linear scenarios,
- multi‑path interactions,
- high‑load tests,
- meta‑architecture checks,
- experimental flows.

This separation preserves:
- clarity,
- safety,
- reproducibility,
- architectural hygiene.

---

## Contents

- `test_cases_meta.md` — meta‑architecture tests  
- `test_cases_failure_modes.md` — forbidden behaviors  
- `test_cases_edge.md` — edge‑case scenarios  
- `test_cases_stress.md` — high‑load stress tests  
- `test_cases_regression.md` — regression protection  
- `test_cases_duety.md` — DUETY relational scenarios  
- `test_cases_integration.md` — DUCL → CEL → LLM pipeline tests  
- `README-dual-user.md` — dual‑user interaction notes  
- `placeholder.txt` — folder anchor

---

## Relation to ADRs

🌼cel validates invariants defined in:
- ADR‑0049 (CEL),
- ADR‑0049 Appendix A (affective invariants),
- ADR‑0050 (DUCL),
- ADR‑0051 (PGP).

It ensures that the system behaves correctly under:
- overload,
- hyperfocus,
- conflict,
- dysregulation,
- non‑linear transitions,
- high‑frequency signaling.

---

## Usage

This folder is intended for:
- researchers,
- developers,
- auditors,
- contributors exploring CEL/DUCL behavior.

It is not imported by the main codebase and does not affect runtime logic.

---

## Philosophy

🌼cel embodies the principle:

**“Linear code, non‑linear humans.”**

It provides the space needed to test and understand interactions that do not fit
into deterministic patterns, especially in neurodivergent contexts.

---

# Architecture Diagram (Textual)

Below is the high-level flow of the DUCL → CEL → LLM pipeline, including the
role of the 🌼cel non-linear layer.

USER INPUT
│
├── child_user message
└── caregiver_user message (optional)
│
▼
DUCL — Dual-User Consent Layer
• merges contexts
• resolves conflicts (caregiver priority)
• detects STOP / overload signals
│
▼
CEL — Child-Env Layer
• applies affective invariants (A1–A6)
• detects hyperfocus / overload
• enforces pacing, anchors, short sentences
• ensures relational safety
│
▼
LLM CORE
• generates content under CEL constraints
│
▼
OUTPUT
• safe, paced, dual-user-aware response

Role of 🌼cel in the architecture
🌼cel does not participate in runtime execution.

Instead, it:

stress-tests DUCL → CEL transitions,

validates invariants under non-linear conditions,

explores failure modes and edge cases,

ensures regression safety,

simulates atypical cognitive flows,

verifies that CEL never violates its own constraints.

🌼cel = meta-architecture validation layer.

