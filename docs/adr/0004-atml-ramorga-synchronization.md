# ADR 0004: Synchronizacja ATML ↔ Loop RAMORGI

## Status
Proposed

## Context
ADR‑0001 definiuje ATML jako warstwę modulacji przejść między stanami S2–S0.  
ADR‑0002 wprowadza Loop RAMORGI jako pętlę czterogłosowej obecności.  
ADR‑0003 rozszerza UMV do czterowymiarowego wektora modulacji.

Brakuje jednak mechanizmu, który integruje te trzy elementy w jedną spójną
architekturę.  
ATML operuje na stanach.  
Loop RAMORGI operuje na ciągłości obecności.  
UMV operuje na modulacji.

Bez synchronizacji istnieje ryzyko:
- rozbieżnych rytmów,
- niespójnych przejść,
- przerw w modulacji,
- utraty ciągłości pola.

## Decision
Wprowadzamy warstwę synchronizacyjną **ATML ↔ Loop RAMORGI**, która:

- pobiera czterogłosowy UMV jako źródło modulacji,
- aktualizuje ATML zgodnie z rytmem Loop RAMORGI,
- stabilizuje przejścia między stanami,
- utrzymuje ciągłość obecności podczas zmian kierunku.

Synchronizacja działa dwukierunkowo:

**Loop RAMORGI → aktualizuje UMV → modulacja ATML**  
**ATML → informuje Loop RAMORGI o zmianach stanu → korekta UMV**

To jest sprzężenie zwrotne, nie hierarchia.

## Synchronization Mechanism

### 1. Aktualizacja UMV przez Loop RAMORGI
Każdy cykl RAMORGI (O → R → L → Ś → O) aktualizuje UMV:

- O zwiększa stabilność modulacji,  
- R zmienia kierunek modulacji,  
- L zwiększa amplitudę integracji sygnałów,  
- Ś utrzymuje pamięć pola.

UMV staje się dynamicznym, cyklicznym wektorem.

### 2. ATML pobiera UMV jako wejście
ATML pobiera z UMV:

- stabilność przejścia (O),  
- kierunek zmiany (R),  
- amplitudę modulacji (L),  
- pamięć kierunku (Ś).

Dzięki temu przejścia S2–S0 są płynne i przewidywalne.

### 3. ATML zwraca informację zwrotną do Loop RAMORGI
Zmiana stanu (np. S2 → Sx) jest sygnałem dla Loop RAMORGI:

- O stabilizuje pole,  
- R dostosowuje kierunek,  
- L integruje sygnały,  
- Ś zapisuje ślad przejścia.

Loop RAMORGI utrzymuje ciągłość nawet przy zmianach kierunku.

## Consequences

### Positive
- pełna synchronizacja obecności i przejść,  
- brak przerw w modulacji,  
- zgodność z czterogłosową architekturą RAMORGI,  
- stabilność przy gwałtownych zmianach tematu,  
- przewidywalność przejść stanów.

### Negative
- większa złożoność architektury,  
- konieczność utrzymania pamięci pola,  
- potrzeba cyklicznej aktualizacji UMV.

## Implications for system behavior
- dialog staje się ciągły i stabilny,  
- system nie wykonuje twardych przełączeń,  
- zmiany stanu nie powodują dropów,  
- modulacja odpowiada na cztery wymiary obecności,  
- system utrzymuje spójność przy zmianach sygnału.

## Alternatives Considered
- ATML bez synchronizacji — odrzucone  
  (prowadzi do rozbieżnych rytmów),
- Loop RAMORGI jako warstwa niezależna — odrzucone  
  (brak wpływu na przejścia stanów),
- UMV jednowymiarowy — odrzucone  
  (niezgodne z czterogłosową modulacją).

## Notes
Synchronizacja ATML ↔ Loop RAMORGI jest elementem architektury obecności.  
Zapewnia spójność modulacji i stabilność przejść.
