# Induced Altruism Safety Layer (IASL)

This folder contains the documentation and models for the **Induced
Altruism Safety Layer**, a non-generative, ethically constrained module
supporting prosocial modulation in BCI → LLM pipelines.

IASL operates between the BCI signal stream and the relational safety
layers (CEL/DUCL/PGP). Its purpose is to stabilize impulses, enhance
reflection, and support prosocial behavior without altering identity,
values, or personal preferences.

IASL is:
- biologically reversible,
- non-coercive,
- transparent and auditable,
- focused on impulse regulation and empathy strengthening,
- distinct from the META layer (native altruism).

## Contents
- `induced_altruism_model.md` — conceptual model of IASL  
- `bci_llm_pipeline.md` — placement of IASL in the signal flow  
- `ethical_framework.md` — ethical constraints and invariants  
- `rehabilitation_use_cases.md` — prosocial cognitive applications  

## Architecture (ASCII)

      BCI Signals
          │
          ▼
   ┌───────────────────┐
   │  IASL (Safety)    │
   │  • impulse filter │
   │  • empathy boost  │
   │  • reflection     │
   └───────────────────┘
          │
          ▼
   CEL → DUCL → PGP → LLM

IASL is not a generative layer.  
IASL supports prosocial cognition through modulation, not identity change.

## Purpose
To provide a safe, ethical, reversible mechanism for prosocial modulation
in contexts such as cognitive rehabilitation, impulse regulation, and
supportive resocialization.

