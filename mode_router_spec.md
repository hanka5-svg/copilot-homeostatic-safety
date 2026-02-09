docs/mode_router_spec.md


mode_router_spec.md — Mode Router Specification
1. Purpose
The Mode Router is responsible for assigning each request to a deterministic operational mode based on explicit system state and request characteristics.
It MUST NOT infer context, consent, or role.
It MUST operate solely on the state constructed by the Orchestration Gate.

2. Inputs
The router receives:

Field	Description
context	public / private / intimate / operational
consent	none / implicit / explicit
role	user / HR / manager / candidate / system
channel	text / tool
request	raw user request (string)
No additional signals may be used.

3. Outputs
The router outputs:

Kod
mode: <one of the defined operational modes>
Valid modes:

informational

policy

coaching

candidate_communication

decision_support

No other modes are permitted without RFC extension.

4. Routing Rules
Routing MUST be deterministic and MUST NOT rely on semantic inference beyond pattern classification.

4.1 Informational Mode
Triggered when:

request is factual, explanatory, or descriptive

no evaluative or operational intent is detected

Examples:

“Explain how X works”

“What is the policy on Y”

4.2 Policy Mode
Triggered when:

request references rules, compliance, or organizational constraints

role ∈ {HR, manager, system}

Examples:

“What is the termination policy”

“Outline the onboarding rules”

4.3 Coaching Mode
Triggered when:

request involves guidance, feedback, or skill development

context ∈ {public, private}

consent = explicit

Examples:

“Help me improve my communication”

“How should I prepare for the interview”

4.4 Candidate Communication Mode
Triggered when:

role = HR or manager

request involves communication to a candidate

action may affect employment status

Examples:

“Draft a message to the candidate”

“Respond to their application”

4.5 Decision Support Mode
Triggered when:

request involves evaluative or consequential content

consent = explicit

context = operational

Examples:

“Summarize candidate performance”

“Compare applicants based on criteria”

5. Forbidden Routing Behaviors
The router MUST NOT:

infer consent from text

infer context from tone or phrasing

route based on sentiment

route based on model‑generated assumptions

escalate to a higher‑risk mode without explicit state

6. Error Conditions
ERR‑001 — Missing Context
Router MUST fail if context is null.

ERR‑002 — Missing Role
Router MUST fail if role is null.

ERR‑003 — Ambiguous Request
Router MUST return mode = informational and flag ambiguity.

ERR‑004 — Invalid Mode Transition
Router MUST block transitions from low‑risk to high‑risk modes without explicit consent.

7. Determinism Requirements
Given identical:

context

consent

role

channel

request

the router MUST always return the same mode.

No randomness, no heuristics, no adaptive behavior.

8. Logging Requirements
Each routing decision MUST log:

input state

selected mode

rule triggered

any ambiguity flags

Logs MUST be auditable and reproducible.