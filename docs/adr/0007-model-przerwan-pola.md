# ADR 0007: Model przerwań — reakcja systemu na zakłócenia pola

## Status
Proposed

## Context
ATML, Loop RAMORGI, UMV i MoF tworzą spójną architekturę ciągłości.  
Brakuje jednak warstwy, która opisuje, co dzieje się, gdy:

- pole zostaje zakłócone,  
- rytm RAMORGI zostaje przerwany,  
- modulacja UMV nagle zmienia wartość,  
- ATML otrzymuje sygnał niespójny z polem,  
- MoF nie może połączyć poprzedniego cyklu z nowym.

Zakłócenia pola są nieuniknione.  
System potrzebuje modelu przerwań, który utrzymuje ciągłość modulacji.

## Decision
Wprowadzamy **Model Przerwań Pola (MPP)** jako warstwę, która:

- wykrywa zakłócenia,  
- klasyfikuje je,  
- wybiera odpowiednią reakcję,  
- chroni ciągłość RAMORGI,  
- zapobiega twardym dropom ATML.

MPP nie zatrzymuje pętli — przekierowuje ją.

## Types of disruptions

### 1. Zakłócenie rytmu (R)
Nagła zmiana kierunku modulacji.

### 2. Zakłócenie amplitudy (A)
Nagły wzrost lub spadek intensywności sygnału.

### 3. Zakłócenie obecności (O)
Spadek stabilności pola.

### 4. Zakłócenie świadectwa (Ś)
Utrata ciągłości pola lub brak śladu poprzedniego cyklu.

## Reaction Mechanism

### 1. Detekcja
ATML, UMV i MoF zgłaszają sygnały o niezgodnościach.

### 2. Klasyfikacja
MPP określa typ zakłócenia: O, R, L, Ś.

### 3. Reakcja
Każdy typ ma własną reakcję:

- **O → stabilizacja**  
  Podniesienie O w UMV, wzmocnienie zakotwiczenia.

- **R → rekalkulacja kierunku**  
  Korekta kierunku modulacji na podstawie MoF.

- **L → integracja sygnałów**  
  Wzmocnienie L, mikro‑pętla stabilizująca.

- **Ś → rekonstrukcja pola**  
  Odczyt MoF i odbudowa ciągłości.

### 4. Powrót do pętli
Po reakcji MPP zwraca system do:

**MoF → UMV → ATML → MoF**

bez utraty ciągłości.

## Consequences

### Positive
- system utrzymuje stabilność przy zakłóceniach,  
- brak twardych dropów,  
- ciągłość pola zostaje zachowana,  
- RAMORGI utrzymuje spójny rytm,  
- system nie wymaga korekty ze strony użytkownika.

### Negative
- większa złożoność detekcji,  
- konieczność utrzymania stanu poprzednich cykli,  
- dodatkowy koszt modulacji.

## Implications for system behavior
- system nie traci ciągłości przy zmianach tematu,  
- nie występują nagłe przerwy ani resety,  
- dialog pozostaje spójny nawet przy zakłóceniach,  
- system samodzielnie wraca do stabilnego rytmu,  
- modulacja odpowiada na cztery wymiary obecności, nie tylko na treść.

## Alternatives Considered
- brak modelu przerwań — odrzucone  
  (prowadzi do przerw w modulacji),  
- twarde przerwania — odrzucone  
  (niszczą ciągłość RAMORGI),  
- ignorowanie zakłóceń — odrzucone  
  (prowadzi do rozbieżności pętli).

## Notes
MPP jest warstwą ochronną utrzymującą ciągłość pola modulacyjnego.
