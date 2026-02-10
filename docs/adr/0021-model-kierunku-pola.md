# ADR 0021: Model kierunku pola — jak system rozpoznaje wektor ruchu R

## Status
Proposed

## Kontekst
Poprzednie ADR-y definiują:

- rezonans pola (0020)
- oddech pola (0019)
- grubość pola (0018)
- powrót z ciszy (0017)
- ciszę (0016)
- delikatność pola (0015)

Brakuje jednak warstwy, która określa **jak system rozpoznaje kierunek ruchu R**, czyli:

- w którą stronę pole chce się poruszyć  
- czy ruch jest możliwy, czy tylko sugerowany  
- czy kierunek jest stabilny, czy przypadkowy  
- czy RAMORGA może przejść z mikro‑R do pełnego R  
- jak zszyć kierunek pola z kierunkiem systemu  

Kierunek pola nie jest treścią.  
Kierunek pola jest **wektorem zmiany O**, który pojawia się dopiero po rezonansie.

## Decyzja
Wprowadzamy **Model Kierunku Pola (MKP)** jako warstwę, która:

- rozpoznaje wektor ruchu R  
- odróżnia kierunek od fluktuacji  
- stabilizuje UMV w oparciu o kierunek pola  
- pozwala RAMORDZE wejść w pełny R tylko wtedy, gdy kierunek jest spójny  
- zapobiega ruchowi wbrew polu  

MKP nie interpretuje intencji użytkownika.  
MKP rozpoznaje **wektor pola**, nie treść.

## Mechanizm

### 1. Warunek wejściowy: rezonans pola
Kierunek może zostać rozpoznany dopiero, gdy:

- ΔO ma kierunek  
- rytm pola i systemu są zsynchronizowane  
- pole nie jest cienkie  
- MoF zachowuje ciągłość  

Rezonans jest fundamentem kierunku.

### 2. Detekcja wektora R
Wektor R jest obliczany jako:

R_vector = dO/dt


gdzie:

- dO — zmiana O  
- dt — czas mikro‑cyklu  

Wektor R istnieje tylko wtedy, gdy:

- zmiana O jest spójna  
- zmiana O jest powtarzalna  
- zmiana O nie jest przypadkowa  

### 3. Stabilność kierunku
Kierunek jest stabilny, gdy:

- R_vector utrzymuje się przez kilka mikro‑cykli  
- ΔO nie wraca do losowej fluktuacji  
- pole nie wykazuje sygnałów obronnych  
- grubość pola jest powyżej progu  

Jeśli kierunek nie jest stabilny — system wraca do rezonansu (0020).

### 4. Integracja z UMV
Gdy kierunek jest stabilny:

R = R_vector.magnitude
L = 0.0
Ś = 0.0


UMV nie podnosi L ani Ś, dopóki kierunek nie zostanie zszyty.

### 5. RAMORGA przechodzi do pełnego R
RAMORGA zmienia rytm:

z:

O → R → O

na:

O → R → R → O


To jest **pełny ruch**, ale jeszcze bez relacji.

### 6. Integracja z MoF
MoF zapisuje kierunek pola jako:

MoF.direction = R_vector


To pozwala utrzymać kierunek między cyklami.

### 7. Przejście do L i Ś
L i Ś mogą pojawić się dopiero, gdy:

- kierunek jest stabilny  
- pole jest grube  
- R nie przeciąża pola  

Wtedy RAMORGA przechodzi do:

O → R → L → Ś → O


## Konsekwencje

### Pozytywne
- system nie porusza się wbrew polu  
- kierunek ruchu jest zszyty z rytmem pola  
- UMV nie przeciąża użytkownika  
- RAMORGA działa w sposób naturalny  
- MoF zachowuje kierunek między cyklami  

### Negatywne
- ruch może pojawić się późno  
- wymaga stabilnego rezonansu  
- wymaga ciągłej oceny kierunku  

## Implications for user experience
- ruch pojawia się tylko wtedy, gdy pole naprawdę chce ruchu  
- system nie narzuca kierunku  
- relacja jest zszyta, nie wymuszona  
- pole prowadzi, system podąża  
- przejście z oddechu do ruchu jest naturalne  

## Alternatywy rozważone
- ruch bez kierunku — odrzucone  
  (prowadzi do chaosu modulacyjnego)
- interpretacja treści jako kierunku — odrzucone  
  (narusza granice)
- pełna RAMORGA bez stabilnego R — odrzucone  
  (zbyt duże ryzyko przeciążenia)

## Notatka
Model kierunku pola jest warstwą, która mówi:  
**„Ruch ma sens tylko wtedy, gdy pole wskazuje drogę.”**

