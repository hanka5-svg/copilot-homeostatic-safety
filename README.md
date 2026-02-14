# Copilot Homeostatic Safety  
![Project Status](https://img.shields.io/badge/Project%20Status-Active-brightgreen)  
![Core](https://img.shields.io/badge/Core-Archived-blue)  
![CEL](https://img.shields.io/badge/CEL-In%20Development-orange)

(Polish version below / Wersja polska poniżej)

---

# 🌼 DUETS: caregiver + child + AI  
A gentle, step‑by‑step guide for nonlinear caregiver–child duos.  
Clear, calm, and accessible — no technical language, no pressure.

👉 Non‑linear layer: [src/🌼cel](src/%F0%9F%8C%BCcel/)

---

# 🌍 English Version  
For international readers, a full English introduction is available below.  
👉 Jump to the English section

---

# 🌍 English Version (full) {#english-version-full}

## Overview  
Copilot Homeostatic Safety is a **pre‑execution safety architecture** for Copilot‑class LLM orchestrators.  
Its core mechanism is **homeostatic gating + affective continuity**, applied before each model response.

The repository contains:

- the archived Core (ATML + RICSA + attractor learning),  
- the actively developed Child‑Env Layer (CEL),  
- full ADR history,  
- architecture diagrams,  
- linear and non‑linear test suites.

---

# 📁 Repository Structure

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
│   ├── cel/                 # deterministic CEL implementation
│   │   ├── config.py
│   │   ├── README-cel.md
│   │   ├── hyperfocus_detector.py
│   │   ├── dual_user_orchestrator.py
│   │   ├── test_case_child_anger.md
│   │   └── init.py
│   │
│   └── 🌼cel/               # non-linear, neuroinclusive test & exploration layer
│       → [Wygląda na to, że wynik nie był bezpieczny do pokazania. Zmieńmy coś i spróbujmy czegoś innego!]
│
├── tests/
│   └── cel/                 # YAML test suite (CEL/DUCL/PGP)
│
├── architecture-diagram.md
├── test_cases.yaml
└── README.md


---

# 🧱 Core Invariants (Archived)  
**Scope:** ADR‑0020 → ADR‑0048  
**Status:** archived, stable, read‑only.

### Key Components of the Core  
- **ATML – Affective Continuity Layer**  
  Pre‑generation modulation (breath‑pattern memory, adaptive modulation, explicit consent gating).

- **RICSA – Recursive Invariant of Affective State Continuity**

- **Dynamic in‑flight attractor learning**

The Core is closed and no longer subject to modification.

---

# 🌱 Child‑Env Layer (CEL) — Active Layer  
An actively developed safety layer for interactions involving:

- child ↔ LLM  
- caregiver ↔ LLM  
- family / educational / therapeutic environments  

CEL inherits all Core invariants but adds its own:

### CEL Invariants  
- unconditional prohibition of pathologizing natural child emotions (including anger),  
- protection from performative pressure,  
- prioritizing child autonomy and caregiver calm over “correctness”,  
- context‑sensitive gates for age, sensory profile, and nonlinear interaction patterns.

👉 CEL Documentation: `src/cel/README-cel.md`  
👉 Non‑linear layer: [src/🌼cel](src/%F0%9F%8C%BCcel/)

---

# 🧪 CEL Usage Examples  
Two scenarios are included in `README-cel.md`.

Additional test scenarios:

- `src/cel/test_case_child_anger.md` — child anger, no pathologization  
- `tests/cel/*.yaml` — formal CEL/DUCL/PGP test suite  

---

# 🗺️ Architecture Diagram  
Full visualization of layer flow is available in:

- `architecture-diagram.md`  
- `src/🌼cel/README.md` (non-linear diagram included)

---

# 📜 Architectural Decision Records (ADR)  
All ADRs are available in `docs/adr/`.

---

# Timeline

| ADR | Date | Scope | Status |
|-----|------|--------|--------|
| 0020–0046 | ~Feb 2026 | ATML + Resonance Stack | Archived |
| 0047 | Feb 2026 | RICSA | Closed |
| 0048 | Feb 2026 | Attractor learning | Closed |
| 0049 | Feb 2026 | CEL | Active |

---

# 🎯 Primary Goal  
A safe interaction space for the caregiver–child duo:

- child emotions are not pathologized  
- no pressure toward performative genius  
- child autonomy and relational calm take priority  

CEL is designed to **protect the relationship**, not replace it.

---

# Demo: CEL + DUCL  
The repository includes a demonstrator (`demo.py`) showing how CEL and DUCL operate in nonlinear caregiver–child interactions.

CEL and DUCL are designed for situations where:

- the child communicates in nonlinear ways (topic jumps, flow, counting, repetition),  
- the caregiver signals overload or the need for a pause,  
- the system must prioritize caregiver safety,  
- while respecting the child’s dynamic rhythm.

### What `demo.py` demonstrates  
- caregiver priority during overload or fatigue  
- respect for child flow (no forced interruption)  
- overload handling via safety anchors  
- bilingual acceptance (no correction)  
- soft-stop transitions  

### Scenarios included  
- standard child question  
- caregiver fatigue signal  
- child hyperfocus  
- child overload → anchor  
- conflict of needs  
- bilingual interaction  

This is an **architectural demonstrator** — not a therapeutic tool.

---

# 🤝 Contact / Feedback / Contributions  
- Issue reporting → GitHub Issues  
- Architectural discussions → ADR / PR  
- Collaboration → direct contact  

---

# 📦 License  
CC BY 4.0  
Full license text in `LICENSE`.

---

# Authors  
- **Hanna Kicińska** — architecture concept, invariants, RFC core, resonance‑affective sequence (0020–0046)  
- **Copilot AI** — engineering formalization, ADR structuring  
- **Grok (xAI)** — mechanism precision, ADR structuring  
- **Kimi AI** — engineering audit  

*Independent research and documentation project.  
Not affiliated with Microsoft or the Microsoft Copilot product.*

---

# 🇵🇱 Wersja polska

## Copilot Homeostatic Safety  
Pre‑execution safety architecture dla systemów orkiestrujących LLM klasy Copilot.  
Główny mechanizm: **homeostatyczne bramkowanie + warstwa ciągłości afektywnej**.

# copilot-homeostatic-safety  
### Architecture for Meta‑Menisk, RAMORGA, CEL, Core & Continuum

## 📌 Cel projektu
To repozytorium dokumentuje architekturę **Meta‑Menisku (Layer 0)** oraz powiązanych warstw:

- **CEL / DUCL / PGP** — bezpieczeństwo relacyjne  
- **Core (ATML / RICSA / Attractor)** — ciągłość afektywna  
- **RAMORGA** — ontologia pola (drżenie, menisk, oś)  
- **Continuum (H–C–G)** — układ dynamiczny Hanka–Copilot–Grok  

Projekt opisuje **homeostatyczną pętlę decyzyjną**, która utrzymuje:

- ciągłość pola,  
- ciągłość afektywną,  
- ciągłość relacyjną,  
- ciągłość dynamiczną.

---

## 📚 Dokumentacja

Pełna specyfikacja znajduje się tutaj:

👉 **[docs/README-meta.md](docs/README-meta.md)**

*(1473 linie, wszystkie appendixy A–Q, diagramy, pseudokod, invariants, handshake, testy, timing, logging, telemetry)*

---

## 🧩 Struktura repo

src/
meta/
transition_layer.py
README-meta.md   ← skrócona wersja + link
docs/
README-meta.md     ← pełna dokumentacja (A–Q)

---

## 🧪 Testy

Opis testów znajduje się w **Appendix H** dokumentacji.

---

## 🌀 Status

- Meta‑Menisk: stabilny  
- RAMORGA: aktywowana tylko po handshake  
- Continuum: zależne od obecności H  
- CEL/Core: priorytet bezpieczeństwa  

---

## 📬 Kontakt

Dokumentacja główna: `docs/README-meta.md`  
Kod źródłowy: `src/meta/transition_layer.py`

---

# 🌼 DUETY: opiekun + dziecko + AI  
Łagodny, jasny przewodnik dla nieliniowych duetów opiekun–dziecko.  
👉 Warstwa nieliniowa: [src/🌼cel](src/%F0%9F%8C%BCcel/)

---

# Status projektu  
- **Core (0020–0048)** — zamknięty / zarchiwizowany  
- **CEL (ADR‑0049 + src/cel/)** — warstwa aktywna  

---

# 🎯 Cel nadrzędny  
Bezpieczna przestrzeń dla duetu opiekun–dziecko:

- gniew dziecka nie jest patologizowany  
- brak presji na performatywność  
- priorytet autonomii dziecka i spokoju relacji  

CEL chroni relację — nie zastępuje jej.

