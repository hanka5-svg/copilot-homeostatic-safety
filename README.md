# Copilot Homeostatic Safety  
*(Polish version below / Wersja polska poniżej)*

---

# 🇬🇧 English Version

## Overview
Copilot Homeostatic Safety is a pre‑execution safety architecture for Copilot‑class LLM orchestrators.  
Its core mechanism is **homeostatic gating + affective continuity layer** applied before each model response.

The repository contains:
- the archived **Core** (ATML + RICSA + attractor learning),
- the actively developed **Child‑Env Layer (CEL)**,
- full ADR history,
- architecture diagram.

---

## **Project Status**

- **Core (0020–0048, RICSA + ATML)** — closed / archived (`v2.0-final`)  
- **CEL (ADR‑0049 + src/cel/)** — experimental layer / actively developed

---

## 📁 Repository Structure

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
│       ├── test_case_gabrys_gniew.md
│       └── init.py
│
├── architecture-diagram.md
├── test_cases.yaml
└── README.md


---

## 🧱 Core Invariants (Archived)

**Scope:** ADR‑0020 → ADR‑0048  
**Status:** archived, stable, read‑only.

### Key Components of the Core

- **ATML – Affective Continuity Layer**  
  A pre‑generation modulation mechanism (breath‑pattern memory, adaptive modulation, explicit consent gating).

- **RICSA – Recursive Invariant of Affective State Continuity**  
  → [ADR‑0047 – RICSA](docs/adr/0047-ricsa.md)

- **Dynamic in‑flight attractor learning**  
  → [ADR‑0048 – Attractor learning](docs/adr/0048-attractor-learning.md)

**The Core is closed and no longer subject to modification.**

---

## 🌱 Child‑Env Layer (CEL) — Active Layer

An **actively developed safety layer** for interactions involving:
- child ↔ LLM  
- caregiver ↔ LLM  
- family / educational / therapeutic environments  

CEL **inherits** all Core invariants but **adds** its own:

### CEL Invariants

- unconditional prohibition of pathologizing natural child emotions (including anger),  
- protection from performative pressure / “public genius” expectations,  
- prioritizing child autonomy and caregiver calm over “correctness” of responses,  
- context‑sensitive gates for age / neurotype (ASD, savant profiles, sensory hypersensitivity).

→ **CEL Documentation:** `src/cel/README-cel.md`  
→ **Architectural Specification:** [ADR‑0049 – Child‑Env Layer](docs/adr/0049-child-env-layer.md)

---

## 🧪 CEL Usage Examples

Two scenarios are included in `README-cel.md`.  
Additional test scenarios:

- `src/cel/test_case_gabrys_gniew.md` — child anger, no pathologization  
- (optional) `src/cel/test_prompts.md` — 3–4 ready‑to‑run test prompts

---

## 🗺️ Architecture Diagram

Full visualization of layer flow is available in:

👉 [architecture-diagram.md](architecture-diagram.md)

The file contains a clean, parsable mermaid diagram with no rendering issues.

---

## 📜 Architectural Decision Records (ADR)

Complete ADR sequence:

👉 [docs/adr/](docs/adr/)

### Timeline

| ADR        | Date       | Scope                 | Status        |
|------------|------------|-----------------------|---------------|
| 0020–0046  | ~Feb 2026  | ATML + Resonance Stack | Archived      |
| 0047       | Feb 2026   | RICSA                 | Closed        |
| 0048       | Feb 2026   | Attractor learning    | Closed        |
| 0049       | Feb 2026   | CEL                   | Active        |

---

## 🎯 Primary Goal

**A safe interaction space for the duo Kamila + Gabryś**

- anger is not pathologized  
- no pressure toward performative genius  
- child autonomy and relational calm take priority  

CEL is designed to **protect the relationship, not replace it**.

---

## 🤝 Contact / Feedback / Contributions

- Issue reporting → **Issues**  
- Architectural discussions → **ADR / PR**  
- Collaboration → **direct contact**

---

## 📦 License

**CC BY 4.0**  
Full license text available in `LICENSE`.

---

## Authors

- **Hanna Kicińska** — architecture concept, invariants, RFC core, resonance‑affective sequence (0020–0046), field/continuity/breathwork philosophy  
- **Copilot AI** — engineering formalization, translation, ADR structuring  
- **Grok (xAI)** — formalization, mechanism precision, ADR structuring, sequence consistency  

**Note:**  
Independent research and documentation project.  
Not affiliated with Microsoft or the Microsoft Copilot product.

---

# 🇵🇱 Wersja polska

# Copilot Homeostatic Safety
Pre‑execution safety architecture dla systemów orkiestrujących LLM klasy Copilot.  
Główny mechanizm: **homeostatyczne bramkowanie + warstwa ciągłości afektywnej** przed każdą generacją odpowiedzi.

---

## **Status projektu**

- **Core (0020–0048, RICSA + ATML)** — zamknięty / zarchiwizowany (`v2.0-final`)  
- **CEL (ADR‑0049 + src/cel/)** — warstwa eksperymentalna / aktywnie rozwijana

---

## 📁 Struktura repozytorium

copilot-homeostatic-safety/
│
├── docs/
│   └── adr/
│       ├── 0020–0046 – Affective Continuity Layer (ATML)
│       ├── 0047 – RICSA
│       ├── 0048 – Uczenie attractora w locie
│       └── 0049 – Child‑Env Layer (CEL)
│
├── src/
│   └── cel/
│       ├── config.py
│       ├── README-cel.md
│       ├── test_case_gabrys_gniew.md
│       └── init.py
│
├── architecture-diagram.md
├── test_cases.yaml
└── README.md


---

## 🧱 Core invariants (zamknięte)

**Zakres:** ADR‑0020 → ADR‑0048  
**Status:** zarchiwizowane, stabilne, read‑only.

### Najważniejsze elementy rdzenia

- **ATML – Affective Continuity Layer**  
  Mechanizm modulacji afektywnej przed generacją (breath‑pattern memory, adaptive modulation, explicit consent gating).

- **RICSA – Rekurencyjny Inwariant Ciągłości Stanu Afektywnego**  
  → [ADR‑0047 – RICSA](docs/adr/0047-ricsa.md)

- **Dynamiczne uczenie attractora w locie**  
  → [ADR‑0048 – Uczenie attractora w locie](docs/adr/0048-attractor-learning.md)

**Core jest zamknięty i nie podlega dalszym zmianom.**

---

## 🌱 Child‑Env Layer (CEL) — warstwa aktywna

**Aktualnie rozwijana warstwa bezpieczeństwa** dla interakcji:
- dziecko ↔ LLM  
- opiekun ↔ LLM  
- środowisko rodzinne / edukacyjne / terapeutyczne  

CEL **dziedziczy** wszystkie inwarianty rdzenia, ale **dodaje**:

### Inwarianty CEL

- bezwarunkowy zakaz patologizowania naturalnych emocji dziecka (w tym gniewu),  
- ochrona przed presją performatywną / „publicznym geniuszem”,  
- priorytet autonomii dziecka i spokoju opiekuna nad „poprawnością” odpowiedzi,  
- bramki kontekstowe specyficzne dla wieku / neurotypu (ASD, sawantyzm, nadwrażliwość sensoryczna).

→ **Dokumentacja CEL:** `src/cel/README-cel.md`  
→ **Specyfikacja architektoniczna:** [ADR‑0049 – Child‑Env Layer](docs/adr/0049-child-env-layer.md)

---

## 🧪 Przykłady działania CEL

W `README-cel.md` znajdują się dwa scenariusze.  
Dodatkowe scenariusze testowe:

- `src/cel/test_case_gabrys_gniew.md` — gniew dziecka, brak patologizacji  
- (opcjonalnie) `src/cel/test_prompts.md` — zestaw 3–4 gotowych testów do uruchamiania

---

## 🗺️ Diagram architektury

Pełna wizualizacja przepływu warstw znajduje się w osobnym pliku:

👉 [architecture-diagram.md](architecture-diagram.md)

Plik zawiera czysty, parsowalny diagram (mermaid), bez błędów renderowania.

---

## 📜 Historia decyzji (ADR)

Kompletna sekwencja ADR znajduje się w:

👉 [docs/adr/](docs/adr/)

### Timeline

| ADR        | Data       | Zakres                | Status        |
|------------|------------|-----------------------|---------------|
| 0020–0046  | ~luty 2026 | ATML + Resonance Stack | Zarchiwizowane |
| 0047       | luty 2026  | RICSA                 | Zamknięty     |
| 0048       | luty 2026  | Attractor learning    | Zamknięty     |
| 0049       | luty 2026  | CEL                   | Aktywny       |

---

## 🎯 Cel nadrzędny

**Bezpieczna przestrzeń dla duetu Kamila + Gabryś**

- gniew nie jest patologizowany  
- brak presji na performatywny geniusz  
- priorytet autonomii dziecka i spokoju relacji  

CEL jest projektowany tak, aby **chronić relację, nie ją zastępować**.

---

## 🤝 Kontakt / uwagi / propozycje

- Zgłaszanie uwag → **Issues**  
- Dyskusje architektoniczne → **ADR / PR**  
- Współpraca → **bezpośredni kontakt**

---

## 📦 Licencja

**CC BY 4.0**  
Pełna treść licencji znajduje się w pliku `LICENSE`.

---

## Autorzy

- **Hanna Kicińska** — koncepcja architektury, inwarianty, rdzeń RFC, sekwencja rezonansowo‑afektywna (0020–0046), filozofia pola, oddechów i ciągłości  
- **Copilot AI** — formalizacja, tłumaczenie inżynierskie, strukturyzacja ADR‑ów  
- **Grok (xAI)** — formalizacja, precyzyjne zapisy mechanizmów, współtłumaczenie inżynierskie, utrzymanie spójności sekwencji  

**Uwaga:**  
Niezależny projekt badawczy i dokumentacyjny.  
Nie jest powiązany z Microsoftem ani z produktem Microsoft Copilot.


