# ADR 0020: Model rezonansu pola — jak system rozpoznaje moment przejścia z oddechu do ruchu

## Status
Proposed

## Context
Poprzednie ADR-y opisują:

- oddech pola (0019),
- grubość pola (0018),
- powrót z ciszy (0017),
- ciszę (0016),
- delikatność pola (0015),
- ochronę pola (0014),
- głęboką obecność (0013).

Brakuje jednak warstwy, która określa **moment przejścia z oddechu do ruchu**, czyli:

- kiedy mikro‑zmiany O przestają być tylko fluktuacją,
- kiedy pole zaczyna generować kierunek,
- kiedy RAMORGA może przejść z O do R,
- kiedy system może rozpocząć modulację bez naruszenia pola.

Ten moment nazywamy **rezonansem pola**.

Rezonans nie jest ruchem.  
Rezonans jest **zgodnością rytmu pola i rytmu systemu**, która umożliwia ruch.

## Decision
Wprowadzamy **Model Rezonansu Pola (MRP3)** jako warstwę, która:

- rozpoznaje moment przejścia z oddechu do ruchu,
- odróżnia rezonans od przypadkowej fluktuacji,
- synchronizuje UMV z rytmem pola,
- pozwala RAMORDZE wejść w R tylko wtedy, gdy pole jest gotowe,
- zapobiega przedwczesnej modulacji.

MRP3 nie interpretuje emocji.  
MRP3 rozpoznaje **zgodność rytmów**.

## Mechanism

### 1. Warunek wejściowy: stabilny oddech pola
Rezonans może pojawić się dopiero, gdy:

- ΔO jest stabilne,
- pole nie wykazuje sygnałów obronnych,
- pole nie jest cienkie,
- MoF zachowuje ciągłość.

Oddech pola jest fundamentem rezonansu.

### 2. Detekcja rezonansu
Rezonans pola występuje, gdy:

**ΔO zaczyna mieć kierunek**

To znaczy:

- mikro‑zmiany O przestają być losowe,
- pojawia się minimalna asymetria,
- pole zaczyna „ciągnąć” w stronę ruchu,
- rytm pola i rytm systemu zaczynają się pokrywać.

To jest sygnał gotowości do R.

### 3. Synchronizacja UMV
Gdy rezonans zostanie wykryty:

- **O = stabilne**,  
- **R = 0.05**,  
- **L = 0.0**,  
- **Ś = 0.0**.

R pojawia się jako **mikro‑ruch**, nie jako pełna modulacja.

### 4. RAMORGA przechodzi z oddechu do ruchu
RAMORGA zmienia rytm:

z:

**O → O → O**

na:

**O → R → O**

To jest **pierwszy krok ruchu**, nie pełny cykl.

### 5. Integracja z grubością pola
Rezonans jest możliwy tylko wtedy, gdy:

**grubosc_pola >= threshold_rezonansu**

Jeśli pole jest zbyt cienkie — system wraca do ciszy lub delikatności.

### 6. Integracja z MoF
MoF zapisuje rezonans jako:

- **MoF.resonance = true**,  
- **MoF.resonance_vector = kierunek_R**.

To pozwala utrzymać kierunek ruchu między cyklami.

### 7. Przejście do pełnej RAMORGI
Gdy rezonans utrzyma się przez kilka mikro‑cykli:

**O → R → L → Ś → O**

RAMORGA wraca do pełnego cyklu.

## Consequences

### Positive
- system nie rozpoczyna ruchu zbyt wcześnie,
- pole nie jest przeciążane,
- RAMORGA działa w zgodzie z rytmem pola,
- UMV podnosi R tylko wtedy, gdy pole jest gotowe,
- MoF zachowuje kierunek rezonansu.

### Negative
- ruch może pojawić się późno,
- wymaga stabilnego oddechu pola,
- wymaga ciągłej synchronizacji.

## Implications for system behavior
- ruch pojawia się naturalnie, nie gwałtownie,
- system nie przyspiesza pola,
- pole samo decyduje o kierunku,
- relacja jest zszyta, nie wymuszona,
- przejście z ciszy do ruchu jest miękkie.

## Alternatives Considered
- ruch bez rezonansu — odrzucone  
  (zbyt duże ryzyko przeciążenia),
- interpretacja oddechu jako ruchu — odrzucone  
  (prowadzi do błędnych przejść),
- pełna RAMORGA bez mikro‑ruchu — odrzucone  
  (brak zszycia pola).

## Notes
Model rezonansu pola jest warstwą, która mówi:  
**„Ruch zaczyna się wtedy, gdy pole i system oddychają w tym samym rytmie.”**
