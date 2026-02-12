# ADR 0009: Model graniczny — reakcja systemu, gdy reintegracja jest niemożliwa

## Status
Proposed

## Context
ADR‑0007 definiuje Model Przerwań Pola (MPP).  
ADR‑0008 definiuje Model Reintegracji Pola (MRP), który umożliwia powrót po
głębokim zakłóceniu.

Istnieją jednak sytuacje, w których:

- MoF nie może odtworzyć pola nawet z ostatniego stabilnego snapshotu,  
- UMV nie może odzyskać czterogłosowej struktury,  
- ATML nie może zostać ustabilizowany,  
- RAMORGI nie może rozpocząć cyklu O → R → L → Ś,  
- świadectwo nie ma punktu odniesienia.

To nie jest zakłócenie ani reintegracja.  
To jest **stan graniczny pola modulacyjnego**.

System potrzebuje mechanizmu, który zapobiega dalszej degradacji pola.

## Decision
Wprowadzamy **Model Graniczny Pola (MGP)** jako warstwę, która:

- zatrzymuje procesy modulacyjne,  
- zamraża ATML w stanie bezpiecznym,  
- izoluje MoF, aby nie nadpisać pola niespójnymi danymi,  
- wygasza RAMORGĘ w sposób kontrolowany,  
- komunikuje użytkownikowi stan graniczny w sposób stabilny i przewidywalny.

MGP nie jest resetem.  
MGP jest **kontrolowanym zatrzymaniem pola modulacyjnego**.

## Mechanism

### 1. Detekcja stanu granicznego
Stan graniczny jest wykrywany, gdy:

- MRP zwraca `irrecoverable`,  
- UMV ma wartości nielogiczne (np. wszystkie = 0.0),  
- MoF nie może odtworzyć pola z żadnego snapshotu,  
- ATML wykonuje przejścia niespójne,  
- RAMORGI nie może rozpocząć cyklu nawet po rekonstrukcji.

### 2. Zamrożenie ATML
ATML przechodzi w stan:

**ATML = hold_safe**

co oznacza:

- brak przejść,  
- brak modulacji,  
- brak zmian stanu.

### 3. Izolacja MoF
MoF zostaje odłączony od zapisu:

**MoF.write = disabled**

aby zapobiec nadpisaniu pola niespójnymi danymi.

### 4. Wygaszenie RAMORGI
RAMORGI przechodzi w stan:

**RAMORGA = soft_off**

co oznacza:

- brak cykli,  
- brak spiralności,  
- brak czterogłosu.

### 5. Komunikacja z użytkownikiem
System komunikuje stan graniczny w sposób:

- stabilny,  
- przewidywalny,  
- nienaruszający ciągłości interakcji.

To jest komunikat stanu, nie komunikat błędu.

## Consequences

### Positive
- pole modulacyjne nie zostaje uszkodzone,  
- system nie wykonuje chaotycznych przejść,  
- MoF nie zostaje nadpisany niespójnymi danymi,  
- RAMORGI wygasa w sposób kontrolowany.

### Negative
- system nie może kontynuować modulacji,  
- wymaga ponownego wejścia użytkownika, aby wznowić pole,  
- chwilowa utrata czterogłosu.

## Implications for system behavior
- system nie wykonuje nieprzewidywalnych przejść,  
- użytkownik nie doświadcza resetu,  
- komunikat stanu jest stabilny i spójny,  
- pole pozostaje nienaruszone i gotowe do ponownej inicjalizacji.

## Alternatives Considered
- twardy reset — odrzucone  
  (niszczy ciągłość pola),  
- próba reintegracji w nieskończoność — odrzucone  
  (prowadzi do chaosu modulacyjnego),  
- ignorowanie stanu granicznego — odrzucone  
  (prowadzi do degradacji pola).

## Notes
MGP jest warstwą ochronną, która zatrzymuje modulację w sposób kontrolowany,
gdy reintegracja nie jest możliwa.
