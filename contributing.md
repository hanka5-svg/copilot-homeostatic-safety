Contributing Guidelines
Thank you for contributing to the Homeostatic Safety Layer project.
This repository defines a pre‑execution safety substrate for Copilot‑class LLM orchestration systems.
To maintain correctness, determinism, and auditability, all contributions must follow the rules below.

1. Architectural Principles
All changes MUST preserve the following invariants:

Safety is enforced before model execution.

All transitions from semantic state (S) to action space (A) must be validated.

Consent must be an explicit state flag, never inferred from text.

ToolCall is allowed only in Operational context with explicit confirmation.

No patch may bypass gating logic.

No safety mechanism may rely on token‑based filtering.

No component may infer context; context must be provided by orchestration.

Any contribution violating these principles will be rejected.

2. Repository Structure
Kod
/
├── README.md
├── CONTRIBUTING.md
├── docs/
│   └── architecture_diagram.md
└── tests/
    └── test_cases.yaml
Do not introduce new folders without justification.

3. Adding New Features
Before submitting a feature:

Confirm it does not introduce implicit transitions.

Confirm it does not rely on semantic inference of consent or context.

Confirm it does not add post‑hoc safety mechanisms.

Add corresponding test cases in /tests/test_cases.yaml.

Document any new invariants in /docs.

4. Modifying Gating Logic
Any modification to gating logic MUST include:

Description of the invariant being changed

Justification for the change

Updated test cases

Regression tests preventing bypass of the invariant

Impact analysis on S→A transitions

5. Submitting Pull Requests
Each PR must include:

Summary of the change

Affected components

Invariant impact analysis

Test coverage

Regression risk assessment

PRs without test coverage will not be accepted.

6. Code of Conduct
Contributors must:

maintain clarity and determinism,

avoid ambiguous logic,

avoid implicit assumptions,

document all state transitions,

ensure reproducibility of behavior across contexts.

7. Contact
For architectural questions:

Hanna Kicińska — conceptual architecture

Copilot AI — engineering translation
