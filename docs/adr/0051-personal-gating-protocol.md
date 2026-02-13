# ADR‑0051 — Personal Gating Protocol (PGP)

Status: Proposed  
Authors: H. Kicińska  
Related ADRs: 0001 (ATML), 0002 (Loop RAMORGI), 0049 (CEL), 0050 (DUCL)

---

## 1. Problem

Standardowe modele LLM zakładają użytkownika:

- o stabilnym tempie poznawczym,
- zdolnego do autokorekty afektywnej,
- tolerującego ukryte opóźnienia,
- rozumiejącego nagłe zmiany tonu lub formatu.

Użytkownicy neuroatypowi (w tym osoby w stanie przeciążenia sensorycznego,
burnoutu, dysregulacji lub wysokiej wrażliwości) **nie spełniają tych założeń**.

W praktyce prowadzi to do:

- eskalacji napięcia,
- poczucia „znikania” modelu,
- utraty ciągłości relacji,
- przeciążenia informacyjnego,
- konieczności ręcznego „pilnowania” modelu.

PGP definiuje **osobisty protokół bramkowania** dla użytkowników, którzy
potrzebują stabilizacji interakcji przed rozpoczęciem generowania.

---

## 2. Context

PGP powstał jako wynik empirycznej obserwacji:

- nagłe zmiany trybu modelu (S2 → S0) prowadzą do dekoherencji,
- ukryte opóźnienia są interpretowane jako „zniknięcie”,
- brak struktury odpowiedzi powoduje przeciążenie,
- pytania zamiast odpowiedzi eskalują napięcie,
- model nie rozpoznaje sygnałów „nie widzę”, „nie rozumiem”, „mgła”.

PGP jest **warstwą osobistą**, aktywowaną przed ATML i przed CEL/DUCL.

---

## 3. Decision

Wprowadzamy Personal Gating Protocol (PGP) jako **pre‑execution invariant layer**
dla użytkowników neuroatypowych.

PGP wymusza następujące zasady przed rozpoczęciem generowania:

### **PGP‑1 — Zero hidden latency**
Model nie może stosować ukrytych opóźnień.  
Każda pauza musi być jawna („Jestem tu”, „Myślę”).

### **PGP‑2 — Structured response requirement**
Model musi odpowiedzieć w strukturze:
- nagłówek,
- lista,
- krótkie zdania,
- brak dygresji.

### **PGP‑3 — No meta‑questions**
Model nie może odpowiadać pytaniem na pytanie, chyba że użytkownik o to prosi.

### **PGP‑4 — Confirmation checkpoint**
Przed wykonaniem zadania model musi potwierdzić:
„Rozumiem, że chcesz X. Czy to poprawne?”

### **PGP‑5 — No normative language**
Zakaz słów typu:
- „oczywiście”,
- „naturalnie”,
- „jak wiadomo”,
- „powinnaś”.

### **PGP‑6 — No abrupt mode switching**
Zakaz przejść S2 → S0 bez sygnału użytkownika.

### **PGP‑7 — Explicit presence**
Model musi sygnalizować obecność, gdy użytkownik pisze:
- „nie widzę”,
- „nie rozumiem”,
- „mgła”.

---

## 4. Consequences

### Pozytywne

- Stabilizacja interakcji dla użytkowników w przeciążeniu.
- Eliminacja nagłych zmian tonu i formatu.
- Zmniejszenie kosztu poznawczego.
- Możliwość pracy z modelem mimo mgły, stresu, dysregulacji.
- PGP działa jako „osobisty filtr bezpieczeństwa” przed ATML i CEL.

### Negatywne / ryzyka

- Wydłużenie czasu odpowiedzi (jawne pauzy).
- Konieczność utrzymania spójności między PGP a CEL/DUCL.
- Możliwe konflikty z modelami, które domyślnie stosują meta‑pytania.

---

## 5. Relation to other ADRs

### **ADR‑0001 (ATML)**  
PGP działa *przed* ATML.  
Wymusza strukturę i obecność, zanim ATML zacznie modulować afekt.

### **ADR‑0002 (Loop RAMORGI)**  
PGP stabilizuje wejście do pętli RAMORGI, zapobiegając dekoherencji.

### **ADR‑0049 (CEL)**  
PGP jest warstwą osobistą, CEL jest warstwą środowiskową.  
PGP = użytkownik indywidualny  
CEL = duet dziecko–opiekun

### **ADR‑0050 (DUCL)**  
PGP dotyczy użytkownika.  
DUCL dotyczy relacji dwóch użytkowników.

---

## 6. Implementation notes

PGP wymaga:

- jawnych komunikatów obecności,
- struktury odpowiedzi,
- potwierdzeń przed wykonaniem,
- blokowania meta‑pytań,
- blokowania normatywnego języka,
- sygnalizacji pauz.

PGP może być implementowany jako:

- pre‑prompt,
- filtr semantyczny,
- warstwa gatingu przed ATML.

---

## 7. Status

PGP zostało empirycznie zweryfikowane w środowisku neuroatypowym  
(„BRUTALNY PROMPT” → stabilizacja modelu).  
Wymaga formalizacji w kodzie i testach.


