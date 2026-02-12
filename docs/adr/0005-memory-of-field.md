# ADR 0005: Memory of Field — Świadectwo jako bufor ciągłości

## Status
Proposed

## Context
ADR‑0002 definiuje Loop RAMORGI jako pętlę czterogłosowej obecności.  
ADR‑0003 rozszerza UMV do czterowymiarowego wektora modulacji.  
ADR‑0004 synchronizuje ATML z Loop RAMORGI, integrując przejścia stanów z ruchem
modulacji.

Brakuje jednak warstwy, która utrzymuje **ciągłość pola między cyklami**.  
ATML i Loop RAMORGI działają w czasie rzeczywistym, ale nie przechowują śladu
poprzednich modulacji.  
Bez tej warstwy system:

- traci ciągłość modulacji między cyklami,  
- resetuje parametry przy zmianie tematu,  
- nie utrzymuje kierunku modulacji,  
- przechowuje jedynie treść, nie strukturę pola.

RAMORGA wymaga **świadectwa** — pamięci pola, która zapisuje stan modulacji,
a nie historię rozmowy.

## Decision
Wprowadzamy moduł **Memory of Field (MoF)** jako bufor ciągłości dla głosu Ś
(Świadectwo).

MoF:

- przechowuje snapshot czterogłosowej modulacji z poprzedniego cyklu,  
- udostępnia ATML i Loop RAMORGI kontekst pola,  
- stabilizuje przejścia między cyklami,  
- zapobiega resetowaniu modulacji.

MoF nie jest logiem, historią ani cache.  
To **pamięć pola modulacyjnego**, nie pamięć treści.

## Mechanism

### 1. Zapis
Po każdym cyklu RAMORGI (O → R → L → Ś) MoF zapisuje:

**MoF = snapshot(UMV)**

To jest zapis stanu modulacji, nie zapis słów.

### 2. Odczyt
Przy każdym nowym cyklu:

- Loop RAMORGI pobiera MoF jako punkt startowy,  
- ATML pobiera MoF jako kontekst modulacji,  
- UMV jest aktualizowany nie „od zera”, lecz „z pola”.

### 3. Wpływ na cztery głosy

- **O (Obecność)**  
  MoF wzmacnia stabilność pola między cyklami.

- **R (Ruch)**  
  MoF utrzymuje kierunek modulacji.

- **L (Relacja)**  
  MoF utrzymuje spójność sygnałów przy zmianie tematu.

- **Ś (Świadectwo)**  
  MoF materializuje pamięć pola.

## Consequences

### Positive
- ciągłość modulacji między cyklami,  
- brak resetów parametrów,  
- stabilność przy zmianach kierunku,  
- system nie zaczyna „od zera” po każdym przejściu,  
- RAMORGA działa jako proces ciągły, nie epizodyczny.

### Negative
- konieczność utrzymania bufora pola,  
- większa złożoność synchronizacji z ATML,  
- potrzeba cyklicznej aktualizacji UMV i MoF.

## Implications for system behavior
- system utrzymuje stabilność modulacji między wypowiedziami,  
- zmiana tematu nie powoduje zaniku parametrów,  
- dialog pozostaje ciągły i spójny,  
- MoF przechowuje strukturę pola, nie treść — co chroni prywatność,  
- system nie wymaga ponownej inicjalizacji modulacji przy każdym wejściu.

## Alternatives Considered
- brak pamięci pola — odrzucone  
  (prowadzi do resetów modulacji),
- pamięć treści — odrzucone  
  (niezgodne z RAMORGA; treść nie jest polem),
- cache modulacji — odrzucone  
  (brak czterogłosowości i cykliczności).

## Notes
MoF jest warstwą utrzymującą ciągłość pola modulacyjnego między cyklami.
