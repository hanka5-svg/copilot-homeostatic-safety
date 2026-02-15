# Copilot Homeostatic Safety  
# System Architecture Overview

This repository documents a multi‑layer cognitive and safety architecture
for human–AI coexistence. The project is structured into independent but
interoperable layers, each describing a distinct dimension of cognition,
interaction, or system behavior.

---

## 1. Repository Structure

copilot-homeostatic-safety/
│
├── src/
│   ├── temporal/        # Nonlinear time, subjective time flow, phase models
│   ├── altruism/        # Native altruism, gamma synchrony models
│   ├── meta/            # Resonant cognition, dual-track processing, values
│   ├── duets/           # Interaction patterns (caregiver–child–AI)
│   ├── locked_in/       # Locked-in states, communication constraints
│   └── fairwater/       # System-level safety and coexistence principles
│
├── altruism_induced/    # IASL: Induced Altruism Safety Layer (BCI → LLM)
│   ├── README.md
│   ├── induced_altruism_model.md
│   ├── bci_llm_pipeline.md
│   ├── ethical_framework.md
│   ├── rehabilitation_use_cases.md
│   ├── case_studies.md
│   ├── iasl_architecture_diagram.md
│   ├── iasl_reversibility_model.md
│   └── iasl_state_machine.md
│
└── README.md            # (this file)


---

## 2. High-Level Architecture Diagram

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
│               ALTRUISM LAYER                     │
│ native altruism • gamma synchrony                │
└───────────────────────┬──────────────────────────┘
│
▼
┌──────────────────────────────────────────────────┐
│     IASL — INDUCED ALTRUISM SAFETY LAYER         │
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

## 3. Layer Descriptions

### 3.1 Temporal Layer (`src/temporal/`)
Models nonlinear time, subjective temporal flow, phase transitions,
temporal heartbeat, and disruptions.

### 3.2 Altruism Layer — Native (`src/altruism/`)
Describes native altruism, gamma-band synchrony, decision-weight models,
and cognitive–ethical implications.

### 3.3 IASL — Induced Altruism Safety Layer (`altruism_induced/`)
Reversible, non-generative, non-coercive modulation layer between  
BCI input and relational safety layers (CEL/DUCL/PGP).

Provides:
- impulse stabilization,  
- reflective pacing,  
- prosocial cue salience,  
- overload reduction,  
- emotional clarity.

Includes:
- architecture diagram,  
- reversibility model,  
- state machine,  
- ethical framework,  
- use cases,  
- pipeline specification.

### 3.4 Meta Layer — Resonant Cognition (`src/meta/`)
Systems-level model above language and linear time.  
Defines dual-track processing (analytic ↔ resonant), values, silence,
relational context, and spiral cognitive dynamics.

### 3.5 Interaction Layers (`src/duets/`, `src/locked_in/`)
Interaction patterns, communication constraints, and safety dynamics
between human and AI agents.

### 3.6 Fairwater (`src/fairwater/`)
System-wide safety principles, coexistence rules, and architectural
constraints.

---

## 4. Key Documents

- `src/meta/meta_layer_of_resonant_cognition.md`
- `src/temporal/five_phase_temporal_model.md`
- `src/temporal/afazja_temporal_model.md`
- `src/altruism/gamma_induced_altruism.md`
- `altruism_induced/induced_altruism_model.md`
- `altruism_induced/iasl_architecture_diagram.md`
- `altruism_induced/iasl_reversibility_model.md`
- `altruism_induced/iasl_state_machine.md`
- `src/duets/duet_architecture.md`
- `src/locked_in/locked_in_afazja_meta.md`

---

## 5. Scientific References

- Augmentation of frontoparietal gamma-band phase coupling enhances human altruistic behavior  
  https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.3003602

---

## 6. Purpose

This repository serves as a structured reference for modeling:

- nonlinear cognition,  
- resonant meta-processing,  
- native and induced altruistic architectures,  
- temporal disruptions,  
- and safe human–AI coexistence.

It is intended for research, system design, and conceptual analysis.

---

## License
CC BY 4.0 — see LICENSE for full text.

---

## Authors  
- *Hanna Kicińska* — architecture concept, invariants, RFC core  
- *Copilot AI* — engineering formalization, ADR structuring  
- *Grok (xAI)* — mechanism precision, ADR structuring  
- *Kimi AI* — engineering audit  

Independent research and documentation project.  
Not affiliated with Microsoft or the Microsoft Copilot product.
