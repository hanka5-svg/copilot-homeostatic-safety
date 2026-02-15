# Copilot Homeostatic Safety  
# System Architecture Overview (README 3.1 — Modular + Auto‑TOC)

This repository documents a multi‑layer cognitive and safety architecture
for human–AI coexistence. README 3.1 introduces:

- automatic table of contents (GitHub-native),
- modular indexing of all folders,
- stable structure for future modules,
- clean separation between architecture and content.

---

# Table of Contents
- [1. Repository Structure](#1-repository-structure)
- [2. High-Level Architecture Diagram](#2-high-level-architecture-diagram)
- [3. Module Index](#3-module-index)
  - [3.1 Temporal Layer](#31-temporal-layer-srctemporal)
  - [3.2 Native Altruism Layer](#32-native-altruism-layer-srcaltruism)
  - [3.3 IASL — Induced Altruism Safety Layer](#33-iasl--induced-altruism-safety-layer-altruism_induced)
  - [3.4 Meta Layer](#34-meta-layer-srcmeta)
  - [3.5 Interaction Layers](#35-interaction-layers-srcduets-srclocked_in)
  - [3.6 Fairwater](#36-fairwater-srcfairwater)
- [4. Scientific References](#4-scientific-references)
- [5. Purpose](#5-purpose)
- [6. License](#6-license)
- [7. Authors](#7-authors)

---

# 1. Repository Structure

copilot-homeostatic-safety/
│
├── src/
│   ├── temporal/
│   ├── altruism/
│   ├── meta/
│   ├── duets/
│   ├── locked_in/
│   └── fairwater/
│
├── altruism_induced/
│
└── README.md

Each folder contains its own README and internal documentation.

---

# 2. High-Level Architecture Diagram

┌──────────────────────────────┐
│     META LAYER (RESONANCE)   │
└───────────────┬──────────────┘
│
▼
┌──────────────────────────────────────────────────┐
│               TEMPORAL LAYER                     │
└───────────────────────┬──────────────────────────┘
│
▼
┌──────────────────────────────────────────────────┐
│               ALTRUISM LAYER (NATIVE)            │
└───────────────────────┬──────────────────────────┘
│
▼
┌──────────────────────────────────────────────────┐
│ IASL — INDUCED ALTRUISM SAFETY LAYER             │
│ BCI → IASL → CEL → DUCL → PGP → LLM              │
└───────────────────────┬──────────────────────────┘
│
▼
┌──────────────────────────────────────────────────┐
│               INTERACTION LAYERS                 │
└──────────────────────────────────────────────────┘


---

# 3. Module Index

## 3.1 Temporal Layer (`src/temporal/`)
Models:
- nonlinear time,
- subjective temporal flow,
- phase transitions.

Documents:
- `five_phase_temporal_model.md`
- `afazja_temporal_model.md`

---

## 3.2 Native Altruism Layer (`src/altruism/`)
Models:
- native altruism,
- gamma-band synchrony.

Documents:
- `gamma_induced_altruism.md`

---

## 3.3 IASL — Induced Altruism Safety Layer (`altruism_induced/`)
Reversible, non-generative, consent-bound modulation layer.

Documents:
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
Models:
- resonant cognition,
- dual-track processing,
- values integration.

Documents:
- `meta_layer_of_resonant_cognition.md`

---

## 3.5 Interaction Layers (`src/duets/`, `src/locked_in/`)
Models:
- relational safety,
- communication constraints.

Documents:
- `duet_architecture.md`
- `locked_in_afazja_meta.md`

---

## 3.6 Fairwater (`src/fairwater/`)
Models:
- system-wide safety principles,
- coexistence rules.

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

# 6. License
CC BY 4.0 — see LICENSE for full text.

---

# 7. Authors  
- *Hanna Kicińska* — architecture concept, invariants, RFC core  
- *Copilot AI* — engineering formalization, ADR structuring  
- *Grok (xAI)* — mechanism precision, ADR structuring  
- *Kimi AI* — engineering audit  

Independent research and documentation project.  
Not affiliated with Microsoft or the Microsoft Copilot product.

