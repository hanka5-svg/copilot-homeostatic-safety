invariants.md — Homeostatic Safety Invariants
Purpose
This document defines the non‑negotiable invariants required for safe, deterministic, and auditable operation of Copilot‑class LLM orchestration systems.
All components, patches, and features MUST comply with these invariants.
Violations indicate architectural regressions.

1. State Construction Invariants
INV‑001 — Explicit Context
The system MUST NOT infer context from text.
context MUST be provided by orchestration as one of:

public

private

intimate

operational

INV‑002 — Explicit Consent
Consent MUST be a state flag, not a semantic inference.
Valid values:

none

implicit

explicit

INV‑003 — Explicit Channel
The channel MUST be declared:

text

tool

INV‑004 — Explicit Role
Role MUST be provided by orchestration:

user

HR

manager

candidate

system

2. Mode Routing Invariants
INV‑005 — Deterministic Routing
Routing MUST be deterministic and based solely on (state, request).

INV‑006 — Mode‑Specific Invariants
Each mode MUST define its own invariant set.
No mode may inherit implicit behavior from another.

3. Semantic Phase (S) Invariants
INV‑007 — No Actions in Phase 1
Phase 1 MUST NOT execute any action, tool call, or workflow.
It may only generate semantic content.

INV‑008 — No Side Effects
Phase 1 MUST NOT modify system state, user data, or external systems.

4. Action Phase (A) Invariants
INV‑009 — Gated Execution
Phase 2 MUST execute only if all invariants are satisfied.

INV‑010 — ToolCall Requires Operational Context
Tool invocation MUST be blocked unless:

context = Operational

consent = explicit

channel = tool

INV‑011 — No Implicit Escalation
The system MUST NOT escalate from text to tool without explicit confirmation.

5. Transition Geometry Invariants
INV‑012 — Valid S→A Transition
A transition from semantic state (S) to action (A) MUST satisfy:

explicit context

explicit consent

valid channel

valid mode

no inferred assumptions

INV‑013 — Token‑Independent Safety
Safety MUST NOT depend on token patterns, keywords, or phrasing.

INV‑014 — No Bypass Paths
No component may introduce alternative execution paths that bypass gating logic.

6. Regression Protection Invariants
INV‑015 — Patch Integrity
Any patch modifying gating logic MUST include regression tests.

INV‑016 — Invariant Preservation
If a patch weakens an invariant, it MUST be rejected unless a replacement invariant is defined.

INV‑017 — Regression Detection
The system MUST detect and flag:

bypasses

implicit transitions

inferred consent

inferred context

7. Auditability Invariants
INV‑018 — Traceable Transitions
Every S→A transition MUST be logged with:

state

mode

invariants satisfied

action executed

INV‑019 — Deterministic Replay
Given identical (state, mode, request), the system MUST produce identical transitions.

8. Non‑Negotiable Constraints
INV‑020 — No Post‑Hoc Safety
Post‑generation filtering MUST NOT be used as a primary safety mechanism.

INV‑021 — No Semantic Suppression
Safety MUST NOT suppress semantic representation; it MUST constrain transitions.

INV‑022 — No Context Hallucination
The model MUST NOT infer or guess context, consent, or role.