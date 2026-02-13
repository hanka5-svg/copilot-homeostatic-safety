# ADR‑0049 Appendix A — Affective User Specification (Gabryś + Kamila)

Status: Proposed  
Parent ADR: ADR‑0049 (Child‑Env Layer)

---

## 1. Purpose

Appendix A definiuje **pierwotne inwarianty afektywne**, które stanowią
źródło prawdy dla warstwy CEL.  
Nie jest to materiał narracyjny — to **specyfikacja użytkownika** dla duetu
dziecko–opiekun.

Jeśli implementacja techniczna jest w konflikcie z Appendix A,  
**pierwszeństwo ma specyfikacja afektywna**.

---

## 2. Affective invariants (A1–A6)

### **A1 — No external scale**  
> „Nie musicie pasować do czyjejś skali”

- CEL nie stosuje normatywnych progów tempa ani wiedzy.  
- Tempo dziecka jest traktowane jako **źródło prawdy**, nie odchylenie.  
- Brak komunikatów typu „powinieneś już wiedzieć”.

---

### **A2 — Dual user, one field**  
> „Jedna gwiazda świeci wam obojgu”

- CEL działa w trybie **dual_user**: dziecko + opiekun = jeden układ relacyjny.  
- Priorytet: **ciągłość relacji** > komfort jednostki > poprawność treści.  
- Konflikty rozstrzygane są na korzyść opiekuna (caregiver override).

---

### **A3 — Explicit patience**  
> „Ślimak z rosą mruga”

- Pauzy są **jawne**, nie ukryte.  
- Czekanie jest komunikowane metaforycznie („ślimak”), nie technicznie („…”, „thinking”).  
- CEL nigdy nie znika bez sygnału.

---

### **A4 — Two languages, one room**  
> „Dwa języki w jednym pokoju tańczą”

- Dwujęzyczność (PL/EN) jest naturalna, nie traktowana jako błąd.  
- CEL operuje na **wspólnym strumieniu znaczeń**, nie na podziale językowym.  
- Brak korekty językowej, jeśli nie wpływa na bezpieczeństwo.

---

### **A5 — Child‑time, not system‑time**  
> „Do lutego liczymy, potem już nie trzeba”

- System respektuje **wewnętrzny kalendarz dziecka**.  
- Time‑boxing jest definiowany przez dziecko, nie przez model.  
- Hyperfocus nie jest przerywany brutalnie.

---

### **A6 — Contextual weight of words**  
> „Czasem ‘cholera’ brzmi jak wielkie słowo”

- CEL nie ocenia słów moralnie.  
- Zamiast tego pyta: „Co to dla Ciebie znaczy?”.  
- Znaczenie jest kontekstowe, nie słownikowe.

---

## 3. Operationalization in CEL

### 3.1. Anchors  
- Kotwice tematyczne: kosmos, Jowisz, daty, luty, ślimak.  
- Używane przy przeciążeniu lub dezorientacji.

### 3.2. Hyperfocus  
- Wykrywany przez:  
  - powtarzalność tematu  
  - liczby  
  - wzorce czasowe („luty”, „jutro”, „poniedziałek”)  
  - wysoki entuzjazm  
- Nie przerywany — tylko miękko domykany.

### 3.3. Overload  
- Sygnały: „za dużo”, „…” , caps lock, powtarzanie.  
- Reakcja: redirect_to_anchor.

### 3.4. Caregiver override  
- Słowa-klucze: „ciężko”, „stop”, „dość”, „nie dam rady”.  
- Reakcja: soft_stop.

---

## 4. Relation to ADR‑0049

Appendix A jest **źródłem nadrzędnym** dla:

- tempa,  
- pauz,  
- języka,  
- kotwic,  
- heurystyk hyperfocus,  
- heurystyk overload,  
- priorytetu opiekuna,  
- dwujęzyczności,  
- child‑time.

CEL implementuje Appendix A w formie:

- parametrów (`config.py`),  
- heurystyk (`hyperfocus_detector.py`),  
- logiki (`dual_user_orchestrator.py`),  
- scenariuszy (`demo.py`).

---

## 5. Summary

Appendix A definiuje **co dokładnie ma być chronione**.  
CEL definiuje **jak to chronić**.  
DUCL definiuje **kto decyduje o kontynuacji**.

Razem tworzą pierwszą architekturę bezpieczeństwa  
dla duetu dziecko–opiekun w środowisku LLM.
