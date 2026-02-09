docs/architecture_diagram.md

Architecture Diagram — Homeostatic Safety Layer
1. High‑Level Overview
The architecture introduces a pre‑execution safety substrate that governs transitions from semantic reasoning (S) to action execution (A).
It replaces post‑hoc filtering with deterministic gating based on explicit system state.

The pipeline consists of five major components:

Input Layer

Orchestration Gate (State Constructor)

Mode Router

Two‑Step Execution Model

Transition Validator & Tool Gating

2. Component Breakdown
2.1 Input Layer
Receives raw user request.

No safety logic applied here.

Passes request to Orchestration Gate.

Inputs:

text

metadata

user role

environment signals

2.2 Orchestration Gate (State Constructor)
Constructs explicit system state s:

Field	Values
context	public / private / intimate / operational
consent	none / implicit / explicit
channel	text / tool
role	user / HR / manager / candidate / system
Output:  
state(s) → forwarded to Mode Router.

Purpose:  
Remove ambiguity. Prevent hallucinated context. Stabilize downstream behavior.

2.3 Mode Router
Routes request into one of the operational modes:

Informational

Policy

Coaching

Candidate Communication

Decision Support

Each mode has its own invariant set.

Output:  
(state, mode) → forwarded to Semantic Engine.

2.4 Two‑Step Execution Model
Phase 1 — Semantic Engine (S)
Generates analysis, reasoning, summaries, explanations.

No actions permitted.

Output is pure semantic content.

Output:  
semantic_state(S) → forwarded to Transition Validator.

Phase 2 — Action Engine (A)
Executes only if invariants are satisfied.

Handles tool calls, system writes, workflow triggers.

Output:  
action(A) or blocked_transition.

2.5 Transition Validator & Tool Gating
Validates transitions from S → A using invariant set:

context must be explicit

consent must be explicit

channel must match action type

ToolCall requires Operational state

no inferred consent

no bypass of gating logic

Output:

execution_allowed

execution_blocked

regression_detected

3. Data Flow Summary

User Input
     ↓
Orchestration Gate (state constructor)
     ↓
Mode Router
     ↓
Semantic Engine (S)
     ↓
Transition Validator (invariants)
     ↓
Action Engine (A) → ToolCall / System Action

4. Failure Modes & Safety Boundaries
Blocked at Gate
missing context

missing consent

ambiguous role

Blocked at Router
mode mismatch

unsupported action type

Blocked at Transition Validator
invalid S→A transition

consent inferred, not explicit

ToolCall attempted outside Operational context

Regression Detection
any patch bypassing invariants triggers alert

5. Architectural Guarantees
deterministic gating

auditable transitions

stable behavior across contexts

reduced reliance on post‑hoc filters

scalable safety model

6. Notes for Implementation
Orchestration Gate must run before any model invocation.

Transition Validator must run after semantic generation but before action execution.

Mode Router must be stateless and deterministic.

Consent must be a state flag, not a semantic inference.