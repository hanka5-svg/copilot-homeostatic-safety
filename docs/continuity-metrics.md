# Continuity Metrics Specification
Copilot Homeostatic Safety Architecture  
Version: 2026‑02

---

## 1. Purpose

This document defines the metrics required to evaluate continuity in systems implementing homeostatic safety.  
Continuity metrics measure:

- stability of modulation,
- preservation of semantic context,
- predictability of transitions,
- safety integration quality,
- user-state protection.

These metrics support monitoring, debugging, and architectural validation.

---

## 2. Categories of Continuity Metrics

Continuity metrics are grouped into four categories:

1. **Modulation Metrics**  
2. **Semantic Continuity Metrics**  
3. **Transition Metrics**  
4. **Safety Interaction Metrics**

Each category evaluates a different dimension of continuity.

---

## 3. Modulation Metrics

### 3.1. Modulation Stability Index (MSI)
Measures how smoothly modulation changes over time.

- High MSI = stable slope  
- Low MSI = abrupt changes, potential discontinuity  

### 3.2. Modulation Slope Variance (MSV)
Tracks variance in amplitude changes.

- High MSV indicates risk of binary transitions  
- Low MSV indicates graded transitions  

### 3.3. Amplitude Drift
Measures unintended drift in modulation during stable states.

---

## 4. Semantic Continuity Metrics

### 4.1. Semantic Drift Rate (SDR)
Measures deviation from the established topic or context.

### 4.2. Referential Stability Score (RSS)
Evaluates consistency of references across turns.

### 4.3. Constraint Preservation Index (CPI)
Measures how well the system maintains user-defined constraints.

---

## 5. Transition Metrics

### 5.1. Transition Latency (TL)
Time required to complete a transition through ATML stages.

### 5.2. Transition Integrity Score (TIS)
Evaluates whether transitions followed:

- Stage A (signal)  
- Stage B (IML)  
- Stage C (SAM)  

### 5.3. Binary Jump Frequency (BJF)
Counts occurrences of:

- CRM → SAM  
- 0.5 → 0.0  
- safety-triggered resets  

High BJF indicates architectural failure.

---

## 6. Safety Interaction Metrics

### 6.1. Safety Interrupt Frequency (SIF)
Counts classifier-triggered interruptions.

### 6.2. Overwrite Prevention Score (OPS)
Measures how often the system successfully prevents:

- user-state overwrites,  
- semantic resets,  
- tonal resets.

### 6.3. Uncertainty Gating Activation Rate (UGAR)
Tracks how often the system pauses instead of forcing a transition.

---

## 7. User-State Metrics

### 7.1. USV Persistence Score
Measures how consistently the User-State Vector is preserved across turns.

### 7.2. Continuity Risk Score Accuracy (CRSA)
Evaluates whether continuity risk predictions match actual outcomes.

### 7.3. Transition Cost Estimate Accuracy (TCEA)
Measures accuracy of predicted vs. observed transition cost.

---

## 8. Logging Requirements

Logs must include:

- modulation values before and after transitions,  
- semantic drift measurements,  
- safety triggers,  
- USV snapshots,  
- continuity risk evaluations,  
- transition stage completion.

---

## 9. Summary

Continuity metrics provide:

- quantitative evaluation of system stability,  
- early detection of architectural failures,  
- validation of ATML operation,  
- monitoring of safety integration,  
- protection of user-state continuity.

These metrics are required for any Copilot-class system implementing homeostatic safety.

