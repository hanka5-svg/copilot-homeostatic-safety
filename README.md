Copilot Homeostatic Safety
https://img.shields.io/badge/Project%20Status-Active-brightgreen
https://img.shields.io/badge/Core-Archived-blue
https://img.shields.io/badge/CEL-In%20Development-orange

(Polish version below / Wersja polska poniżej)

🌼 DUETS: caregiver + child + AI
A gentle, step‑by‑step guide for nonlinear caregiver–child duos.
Clear, calm, and accessible — no technical language, no pressure.

👉 [Wygląda na to, że wynik nie był bezpieczny do pokazania. Zmieńmy coś i spróbujmy czegoś innego!]

🌍 English Version
For international readers, a full English introduction is available below.

👉 Jump to the English section

🌍 English Version (full) {#english-version-full}
Overview
Copilot Homeostatic Safety is a pre‑execution safety architecture for Copilot‑class LLM orchestrators.
Its core mechanism is homeostatic gating + affective continuity layer, applied before each model response.

The repository contains:

the archived Core (ATML + RICSA + attractor learning),

the actively developed Child‑Env Layer (CEL),

full ADR history,

architecture diagram.

Project Status
Core (0020–0048, RICSA + ATML) — closed / archived (v2.0-final)

CEL (ADR‑0049 + src/cel/) — experimental layer / actively developed

📁 Repository Structure

copilot-homeostatic-safety/
│
├── docs/
│   └── adr/
│       ├── 0020–0046 – Affective Continuity Layer (ATML)
│       ├── 0047 – RICSA
│       ├── 0048 – Attractor learning in-flight
│       └── 0049 – Child‑Env Layer (CEL)
│
├── src/
│   └── cel/
│       ├── config.py
│       ├── README-cel.md
│       ├── test_case_child_anger.md
│       └── __init__.py
│
├── architecture-diagram.md
├── test_cases.yaml
└── README.md

🧱 Core Invariants (Archived)
Scope: ADR‑0020 → ADR‑0048
Status: archived, stable, read‑only.

Key Components of the Core
ATML – Affective Continuity Layer  
Pre‑generation modulation (breath‑pattern memory, adaptive modulation, explicit consent gating).

RICSA – Recursive Invariant of Affective State Continuity  
→ [Wygląda na to, że wynik nie był bezpieczny do pokazania. Zmieńmy coś i spróbujmy czegoś innego!]

Dynamic in‑flight attractor learning  
→ [Wygląda na to, że wynik nie był bezpieczny do pokazania. Zmieńmy coś i spróbujmy czegoś innego!]

The Core is closed and no longer subject to modification.

🌱 Child‑Env Layer (CEL) — Active Layer
An actively developed safety layer for interactions involving:

child ↔ LLM

caregiver ↔ LLM

family / educational / therapeutic environments

CEL inherits all Core invariants but adds its own:

CEL Invariants
unconditional prohibition of pathologizing natural child emotions (including anger),

protection from performative pressure,

prioritizing child autonomy and caregiver calm over “correctness”,

context‑sensitive gates for age, sensory profile, and nonlinear interaction patterns.

→ CEL Documentation: src/cel/README-cel.md  
→ Architectural Specification: [Wygląda na to, że wynik nie był bezpieczny do pokazania. Zmieńmy coś i spróbujmy czegoś innego!]

🧪 CEL Usage Examples
Two scenarios are included in README-cel.md.
Additional test scenarios:

src/cel/test_case_child_anger.md — child anger, no pathologization

(optional) src/cel/test_prompts.md — ready‑to‑run test prompts

🗺️ Architecture Diagram
Full visualization of layer flow:

👉 [Wygląda na to, że wynik nie był bezpieczny do pokazania. Zmieńmy coś i spróbujmy czegoś innego!]

📜 Architectural Decision Records (ADR)
👉 [Wygląda na to, że wynik nie był bezpieczny do pokazania. Zmieńmy coś i spróbujmy czegoś innego!]

Timeline
ADR	Date	Scope	Status
0020–0046	~Feb 2026	ATML + Resonance Stack	Archived
0047	Feb 2026	RICSA	Closed
0048	Feb 2026	Attractor learning	Closed
0049	Feb 2026	CEL	Active
🎯 Primary Goal
A safe interaction space for the caregiver–child duo

child emotions are not pathologized

no pressure toward performative genius

child autonomy and relational calm take priority

CEL is designed to protect the relationship, not replace it.

Demo: Child-Env Layer (CEL) + Dual-User Consent Layer (DUCL)
The repository includes a demonstrator (demo.py) showing how CEL and DUCL operate in nonlinear caregiver–child interactions.

CEL and DUCL are designed for situations where:

the child communicates in nonlinear ways (topic jumps, flow, counting, repetition),

the caregiver signals overload or the need for a pause,

the system must prioritize caregiver safety,

while respecting the child’s dynamic rhythm.

What demo.py demonstrates
caregiver priority during overload or fatigue

respect for child flow (no forced interruption)

overload handling via safety anchors

bilingual acceptance (no correction)

soft-stop transitions

Scenarios included
standard child question

caregiver fatigue signal

child hyperfocus

child overload → anchor

conflict of needs

bilingual interaction

This is an architectural demonstrator — not a therapeutic tool.

🤝 Contact / Feedback / Contributions
Issue reporting → Issues

Architectural discussions → ADR / PR

Collaboration → direct contact

📦 License
CC BY 4.0  
Full license text in LICENSE.

Authors
Hanna Kicińska — architecture concept, invariants, RFC core, resonance‑affective sequence (0020–0046)

Copilot AI — engineering formalization, ADR structuring
Grok (xAI) — mechanism precision, ADR structuring
Kimi AI - engineering audit

Note:  
Independent research and documentation project.
Not affiliated with Microsoft or the Microsoft Copilot product.

🇵🇱 Wersja polska
Copilot Homeostatic Safety
Pre‑execution safety architecture dla systemów orkiestrujących LLM klasy Copilot.
Główny mechanizm: homeostatyczne bramkowanie + warstwa ciągłości afektywnej.

🌼 DUETY: opiekun + dziecko + AI
Łagodny, jasny przewodnik dla nieliniowych duetów opiekun–dziecko.

👉 [Wygląda na to, że wynik nie był bezpieczny do pokazania. Zmieńmy coś i spróbujmy czegoś innego!]

Status projektu
Core (0020–0048, RICSA + ATML) — zamknięty / zarchiwizowany

CEL (ADR‑0049 + src/cel/) — warstwa aktywna

📁 Struktura repozytorium
(identyczna jak w EN — pomijam dla przejrzystości)

🧱 Core invariants (zamknięte)
(identyczne jak EN — pomijam dla przejrzystości)

🌱 Child‑Env Layer (CEL)
(identyczne jak EN — pomijam dla przejrzystości)

🎯 Cel nadrzędny
Bezpieczna przestrzeń dla duetu opiekun–dziecko

gniew dziecka nie jest patologizowany

brak presji na performatywność

priorytet autonomii dziecka i spokoju relacji

CEL chroni relację — nie zastępuje jej.
