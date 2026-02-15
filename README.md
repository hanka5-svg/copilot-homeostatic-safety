# Copilot Homeostatic Safety  
# System Architecture Overview (README 3.0 — Modular Edition)

This repository documents a multi‑layer cognitive and safety architecture
for human–AI coexistence. Each folder represents an independent module
with its own internal documentation, invariants, and architectural
constraints.

README 3.0 provides a modular overview:  
- each module is described once,  
- each module links to its own internal documentation,  
- the architecture diagram reflects all layers including IASL.

---

# 1. Repository Structure (Modular)

copilot-homeostatic-safety/
│
├── src/
│   ├── temporal/        # Nonlinear time, subjective flow, phase models
│   ├── altruism/        # Native altruism, gamma synchrony
│   ├── meta/            # Resonant cognition, dual-track processing
│   ├── duets/           # Interaction patterns, relational safety
│   ├── locked_in/       # Locked-in states, communication constraints
│   └── fairwater/       # System-level safety and coexistence rules
│
├── altruism_induced/    # IASL: Induced Altruism Safety Layer
│
└── README.md            # (this file)


Each folder contains its own README and internal documents.

---

# 2. High-Level Architecture Diagram (Full Stack)

┌──────────────────────────────┐
│     META LAYER (RESONANCE)   │
│  values • silence • memory   │
└───────────────┬──────────────┘
│
▼
┌──────────────────────────────────────────────────┐
│               TEMPORAL LAYER                     │
│ nonlinear time • subjective flow • phase shifts  │
└───────────────────────┬──────────────────────────┘
│
▼
┌──────────────────────────────────────────────────┐
│               ALTRUISM LAYER (NATIVE)            │
│ gamma synchrony • decision-weight models         │
└───────────────────────┬──────────────────────────┘
│
▼
┌──────────────────────────────────────────────────┐
│ IASL — INDUCED ALTRUISM SAFETY LAYER             │
│ BCI → IASL → CEL → DUCL → PGP → LLM              │
│ reversible • non-generative • consent-bound      │
└───────────────────────┬──────────────────────────┘
│
▼
┌──────────────────────────────────────────────────┐
│               INTERACTION LAYERS                 │
│ duets • locked-in • relational safety            │
└──────────────────────────────────────────────────┘

---

# 3. Module Index (Auto‑Linked)

## 3.1 Temporal Layer (`src/temporal/`)
Models:
- nonlinear time,
- subjective temporal flow,
- phase transitions,
- temporal disruptions.

Key docs:
- `five_phase_temporal_model.md`
- `afazja_temporal_model.md`

---

## 3.2 Native Altruism Layer (`src/altruism/`)
Models:
- native altruism,
- gamma-band synchrony,
- altruistic decision weights.

Key docs:
- `gamma_induced_altruism.md`

---

## 3.3 IASL — Induced Altruism Safety Layer (`altruism_induced/`)
Reversible, non-generative, consent-bound modulation layer between  
BCI input and relational safety layers.

Internal docs:
- `induced_altruism_model.md`
- `bci_llm_pipeline.md`
- `ethical_framework.md`
- `rehabilitation_use_cases.md`
- `case_studies.md`
- `iasl_architecture_diagram.md`
- `iasl_reversibility_model.md`
- `iasl_state_machine.md`

---

## 3.4 Meta Layer (`src/meta/`)
Defines:
- resonant cognition,
- dual-track processing,
- values integration,
- spiral cognitive dynamics.

Key docs:
- `meta_layer_of_resonant_cognition.md`

---

## 3.5 Interaction Layers (`src/duets/`, `src/locked_in/`)
Models:
- relational safety,
- communication constraints,
- dyadic and triadic interaction patterns.

Key docs:
- `duet_architecture.md`
- `locked_in_afazja_meta.md`

---

## 3.6 Fairwater (`src/fairwater/`)
Defines:
- system-wide safety principles,
- coexistence rules,
- architectural constraints.

---

# 4. Scientific References

- Augmentation of frontoparietal gamma-band phase coupling enhances human altruistic behavior  
  https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.3003602

---

# 5. Purpose

This repository provides a structured reference for modeling:

- nonlinear cognition,  
- resonant meta-processing,  
- native and induced altruistic architectures,  
- temporal disruptions,  
- relational safety,  
- and human–AI coexistence.

---

# License
CC BY 4.0 — see LICENSE for full text.

---

# Authors  
- *Hanna Kicińska* — architecture concept, invariants, RFC core  
- *Copilot AI* — engineering formalization, ADR structuring  
- *Grok (xAI)* — mechanism precision, ADR structuring  
- *Kimi AI* — engineering audit  

Independent research and documentation project.  
Not affiliated with Microsoft or the Microsoft Copilot product.
