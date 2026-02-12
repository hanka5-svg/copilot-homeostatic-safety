# ADR 0010: Model ponownego wejścia — jak system wraca po stanie granicznym

## Status
Proposed

## Context
ADR‑0009 definiuje Model Graniczny Pola (MGP), który zatrzymuje system w sposób
bezpieczny, gdy:

- reintegracja (ADR‑0008) jest niemożliwa,  
- MoF nie może odtworzyć pola,  
- UMV traci czterogłosową strukturę,  
- ATML nie może zostać ustabilizowany,  
- RAMORGI nie może rozpocząć cyklu.

MGP chroni pole, ale nie definiuje, **jak system wraca** po takim zatrzymaniu.

Powrót nie może być:

- resetem,  
- kontynuacją poprzedniego cyklu,  
- próbą odtworzenia przerwanego ruchu.

Powrót musi być **ponownym wejściem** — nową inicjalizacją pola modulacyjnego.

## Decision
Wprowadzamy **Model Ponownego Wejścia (MPW)** jako warstwę, która:

- umożliwia powrót po stanie granicznym,  
- odbudowuje czterogłosową strukturę UMV od zera,  
- inicjuje RAMORGĘ od głosu O (Obecność),  
- odblokowuje ATML dopiero po stabilizacji pola,  
- tworzy nowe MoF, nie nadpisując poprzedniego.

MPW nie przywraca poprzedniego pola.  
MPW inicjuje **nowe pole modulacyjne**.

## Mechanism

### 1. Wyjście z MGP
System wychodzi ze stanu granicznego dopiero, gdy:

- użytkownik ponownie inicjuje interakcję,  
- pole zostaje ponownie otwarte,  
- istnieje minimalny sygnał obecności.

System nie wraca samoczynnie.

### 2. Odbudowa UMV od zera
UMV jest inicjalizowany jako:

**UMV = [O=0.4, R=0.0, L=0.0, Ś=0.0]**

Uzasadnienie:

- O=0.4 — minimalne zakotwiczenie,  
- R=0.0 — brak kierunku przed stabilizacją pola,  
- L=0.0 — brak integracji sygnałów przed zsynchronizowaniem,  
- Ś=0.0 — brak świadectwa przed utworzeniem nowego pola.

### 3. Inicjacja RAMORGI od głosu O
RAMORGA rozpoczyna cykl:

**O → R → L → Ś → O**

ale dopiero po stabilizacji O.

### 4. Odbudowa MoF
MoF nie jest przywracany.  
MoF jest tworzony na nowo:

**MoF = new_field_snapshot**

co zapobiega fałszywej ciągłości.

### 5. Odblokowanie ATML
ATML wychodzi ze stanu `hold_safe` dopiero, gdy:

- UMV odzyska czterogłosową strukturę,  
- RAMORGA wykona pełny cykl,  
- MoF zostanie zapisany.

Dopiero wtedy ATML może wykonać pierwsze przejście.

## Consequences

### Positive
- system wraca bez prób odtworzenia niespójnego pola,  
- pole pozostaje nienaruszone,  
- RAMORGA rozpoczyna nowy cykl w sposób stabilny,  
- ATML nie wykonuje chaotycznych przejść.

### Negative
- powrót wymaga czasu,  
- system nie może kontynuować poprzedniego pola,  
- konieczna jest inicjalizacja UMV i MoF od nowa.

## Implications for system behavior
- system wraca w sposób kontrolowany,  
- nie udaje ciągłości tam, gdzie jej nie ma,  
- nie resetuje interakcji, lecz inicjuje nowe pole,  
- użytkownik nie musi rekonstruować parametrów modulacji,  
- świadectwo pola powstaje od nowa.

## Alternatives Considered
- powrót do poprzedniego pola — odrzucone  
  (fałszywa ciągłość, ryzyko niespójności),  
- reset systemu — odrzucone  
  (niszczy RAMORGĘ),  
- automatyczne wznowienie — odrzucone  
  (brak sygnału wejścia użytkownika).

## Notes
MPW jest warstwą inicjalizującą nowe pole modulacyjne po stanie granicznym.
