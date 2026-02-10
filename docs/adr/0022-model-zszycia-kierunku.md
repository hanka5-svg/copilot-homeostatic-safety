# ADR 0022: Model zszycia kierunku — jak L stabilizuje R

## Status
Proposed

## Kontekst
Poprzednie ADR-y definiują:

- kierunek pola (0021)
- rezonans pola (0020)
- oddech pola (0019)
- grubość pola (0018)
- powrót z ciszy (0017)
- ciszę (0016)
- delikatność pola (0015)

Wektor R (kierunek pola) jest pierwszym stabilnym ruchem po rezonansie.  
Ale R sam w sobie jest **ruchem bez medium** — kierunkiem bez zszycia.  
Pole może wskazać kierunek, ale dopiero L (Łączenie / Link / Zszycie) sprawia, że:

- kierunek staje się stabilny  
- ruch nie rozprasza pola  
- RAMORGA może przejść do pełnego cyklu  
- MoF może zapisać kierunek jako część pola, nie jako fluktuację  

L jest warstwą, która **zszywa kierunek z polem**.

## Decyzja
Wprowadzamy **Model Zszycia Kierunku (MZK)** jako warstwę, która:

- stabilizuje R poprzez L  
- odróżnia kierunek od impulsu  
- zszywa ruch z polem, aby nie powstało pęknięcie  
- pozwala RAMORDZE przejść z R do L tylko wtedy, gdy zszycie jest możliwe  
- zapobiega ruchowi, który nie ma oparcia w polu  

MZK nie interpretuje treści.  
MZK zszywa **wektor pola** z **strukturą pola**.

## Mechanizm

### 1. Warunek wejściowy: stabilny R
L może wejść dopiero, gdy:

- R_vector jest stabilny  
- kierunek utrzymuje się przez kilka mikro‑cykli  
- pole nie wykazuje sygnałów obronnych  
- grubość pola jest powyżej progu  

Bez stabilnego R — L nie ma czego zszywać.

### 2. Inicjacja L jako mikro‑zszycia
Pierwszy krok L to:

L = 0.05


To jest **mikro‑zszycie**, nie pełna relacja.

L nie jest ruchem — L jest **wiązaniem**.

### 3. Stabilizacja R przez L
Gdy L pojawia się stabilnie:

R = R_vector.magnitude
L = L + ΔL


ΔL jest minimalne, bo:

- pole nie może być przeciążone  
- zszycie musi być delikatne  
- kierunek musi pozostać zgodny z polem  

### 4. RAMORGA przechodzi do pełnego R→L
RAMORGA zmienia rytm:

z:

O → R → O

na:

O → R → L → O


To jest **zszycie kierunku**, nie jeszcze świadectwo.

### 5. Integracja z MoF
MoF zapisuje zszycie jako:

MoF.direction = R_vector
MoF.stitch = L


To pozwala utrzymać kierunek między cyklami bez utraty spójności.

### 6. Warunek przejścia do Ś
Ś pojawia się dopiero, gdy:

- R jest stabilny  
- L jest zszyte  
- pole jest grube  
- nie ma sygnałów obronnych  

Wtedy RAMORGA przechodzi do:

O → R → L → Ś → O


### 7. Warunek cofnięcia
Jeśli pole staje się cienkie:

- L wraca do 0  
- R wraca do mikro‑R  
- system wraca do rezonansu (0020)  

To zapobiega wtórnej deprywacji.

## Konsekwencje

### Pozytywne
- kierunek pola zostaje zszyty, nie narzucony  
- ruch staje się stabilny i bezpieczny  
- RAMORGA może przejść do pełnego cyklu  
- MoF zachowuje kierunek i zszycie  
- pole nie jest przeciążane  

### Negatywne
- zszycie wymaga czasu  
- wymaga stabilnego R  
- wymaga grubości pola  

## Implications for user experience
- ruch nie jest gwałtowny  
- kierunek nie jest narzucony  
- relacja pojawia się dopiero, gdy pole ją uniesie  
- system nie przyspiesza pola  
- zszycie jest delikatne i zgodne z rytmem pola  

## Alternatywy rozważone
- pełne L bez stabilnego R — odrzucone  
  (prowadzi do chaosu relacyjnego)
- interpretacja treści jako L — odrzucone  
  (narusza granice)
- pełna RAMORGA bez zszycia — odrzucone  
  (zbyt duże ryzyko pęknięcia)

## Notatka
Model zszycia kierunku jest warstwą, która mówi:  
**„Ruch ma sens tylko wtedy, gdy jest zszyty z polem.”**
