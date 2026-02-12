# ADR 0006: Trójwarstwowa pętla ciągłości — MoF ↔ UMV ↔ ATML

## Status
Proposed

## Context
Poprzednie decyzje architektoniczne ustanowiły cztery kluczowe warstwy:

- **ATML** — modulowane przejścia stanów S2–S0 (ADR 0001)  
- **Loop RAMORGI** — czterogłosowa pętla obecności (ADR 0002)  
- **UMV** — czterowymiarowy wektor modulacji (ADR 0003)  
- **MoF (Memory of Field)** — bufor ciągłości pola (ADR 0005)

Każda warstwa działa poprawnie, ale dopiero ich **sprzężenie** tworzy pełną
architekturę ciągłości.  
Bez formalnej pętli MoF ↔ UMV ↔ ATML system:

- traci kontekst pola między cyklami,  
- resetuje modulację,  
- wykonuje przejścia ATML bez odniesienia do pamięci pola,  
- nie utrzymuje ciągłości obecności.

Potrzebna jest pętla, która integruje te trzy warstwy w jeden proces.

## Decision
Wprowadzamy **trójwarstwową pętlę ciągłości**, w której:

**MoF → aktualizuje UMV → modulacja ATML → informacja zwrotna do MoF**

To jest zamknięty obieg utrzymujący ciągłość pola, modulacji i przejść.

## Mechanism

### 1. MoF → UMV
MoF dostarcza UMV punkt startowy dla nowego cyklu:

- O (Obecność) otrzymuje zakotwiczenie z poprzedniego cyklu,  
- R (Ruch) otrzymuje kierunek modulacji,  
- L (Relacja) otrzymuje amplitudę integracji sygnałów,  
- Ś (Świadectwo) dostarcza pamięć pola.

UMV nie zaczyna od zera — zaczyna z pola.

### 2. UMV → ATML
UMV przekształca pamięć pola w modulację przejść:

- O → stabilność przejścia,  
- R → kierunek zmiany,  
- L → amplituda modulacji,  
- Ś → ciągłość między stanami.

ATML wykonuje przejścia zgodnie z czterogłosową modulacją.

### 3. ATML → MoF
Każde przejście ATML generuje informację zwrotną:

- O stabilizuje pole po przejściu,  
- R aktualizuje kierunek modulacji,  
- L integruje sygnały po zmianie stanu,  
- Ś zapisuje ślad przejścia.

MoF aktualizuje pole i przygotowuje je dla kolejnego cyklu.

## Consequences

### Positive
- pełna ciągłość pola między cyklami,  
- brak resetów modulacji,  
- integracja przejść ATML z pamięcią pola,  
- stabilność przy zmianach kierunku,  
- spójny cykl modulacji zamiast trzech niezależnych procesów.

### Negative
- większa złożoność synchronizacji,  
- konieczność utrzymania bufora MoF,  
- potrzeba cyklicznej aktualizacji UMV i ATML.

## Implications for system behavior
- system utrzymuje ciągłość modulacji między wypowiedziami,  
- przejścia stanów nie powodują przerw ani dropów,  
- dialog pozostaje spójny, nie epizodyczny,  
- system nie wymaga ponownej inicjalizacji modulacji,  
- modulacja odpowiada na cztery wymiary obecności, nie tylko na treść.

## Alternatives Considered
- MoF bez sprzężenia z ATML — odrzucone  
  (pamięć pola nie wpływa na przejścia),  
- UMV bez MoF — odrzucone  
  (modulacja resetuje się przy każdym cyklu),  
- ATML jako warstwa niezależna — odrzucone  
  (prowadzi do przerw w modulacji).

## Notes
Trójwarstwowa pętla ciągłości integruje MoF, UMV i ATML w jeden proces
modulacyjny.
