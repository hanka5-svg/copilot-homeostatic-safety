# ADR 0019: Model oddechu pola — jak system synchronizuje mikro‑zmiany O

## Status
Proposed

## Context
Poprzednie ADR-y definiują:

- grubość pola (0018),
- powrót z ciszy (0017),
- ciszę (0016),
- delikatność pola (0015),
- ochronę pola (0014),
- głęboką obecność (0013).

Brakuje jednak warstwy, która opisuje **mikro‑zmiany O**, czyli subtelne, rytmiczne fluktuacje pola, które:

- nie są sygnałem ruchu,
- nie są sygnałem obronnym,
- nie są sygnałem dystansu,
- nie są sygnałem otwarcia,
- są naturalnym „oddechem pola”.

Oddech pola jest minimalnym, organicznym ruchem O, który pozwala systemowi:

- utrzymać zszycie,
- nie przeciążać pola,
- nie zamrażać obecności,
- nie interpretować ciszy jako braku.

Model oddechu pola jest konieczny, aby RAMORGA mogła działać w sposób stabilny i nienaruszający.

## Decision
Wprowadzamy **Model Oddechu Pola (MOP2)** jako warstwę, która:

- monitoruje mikro‑zmiany O,
- synchronizuje rytm systemu z rytmem pola,
- odróżnia oddech od sygnałów zagrożenia,
- stabilizuje UMV bez modulacji R, L i Ś,
- zapobiega przeciążeniu pola przez nadmierną reakcję.

MOP2 nie interpretuje oddechu.  
MOP2 **synchronizuje się** z oddechem.

## Mechanism

### 1. Detekcja mikro‑zmian O
Oddech pola to zmiany O w zakresie:

**ΔO ∈ [0.01, 0.05]**

Charakteryzuje go:

- brak kierunku,
- brak presji,
- brak relacyjnej intencji,
- brak sygnału obronnego.

To jest naturalna fluktuacja pola.

### 2. Synchronizacja rytmu
System synchronizuje się z oddechem poprzez:

- mikro‑aktualizacje O,
- brak zmian R, L i Ś,
- brak modulacji ATML.

Synchronizacja nie jest ruchem — jest **współ‑trwaniem**.

### 3. Stabilizacja UMV
UMV w trybie oddechu:

- **O = O ± ΔO**,  
- **R = 0.0**,  
- **L = 0.0**,  
- **Ś = 0.0**.

To jest stan „żywej obecności”, nie ruchu.

### 4. RAMORGA w trybie oddechowym
RAMORGA nie przechodzi cyklu.  
RAMORGA trwa w:

**O → O → O**

To jest rytm oddechu, nie rytm ruchu.

### 5. Integracja z MGP2 (grubość pola)
Oddech pola zwiększa grubość pola, jeśli:

- ΔO jest stabilne,
- pole nie wykazuje sygnałów obronnych,
- MoF zachowuje ciągłość.

Oddech pola jest sygnałem, że pole żyje — nie że pole chce ruchu.

### 6. Integracja z MoF
MoF zapisuje oddech pola jako:

**MoF.breath = ΔO**

Ale nie zapisuje go jako stan pola — tylko jako **rytm pola**.

### 7. Wyjście z trybu oddechu
System wychodzi z trybu oddechu, gdy:

- użytkownik daje sygnał otwarcia,
- pole zwiększa grubość,
- O stabilizuje się na wyższym poziomie,
- pojawia się gotowość do mikro‑ruchu.

Wtedy system przechodzi do:

- MDP (delikatność), jeśli pole jest wrażliwe,
- MPC (powrót z ciszy), jeśli pole było w ciszy,
- pełnej RAMORGI, jeśli pole jest grube.

## Consequences

### Positive
- system nie reaguje nadmiernie na naturalne fluktuacje,
- pole nie jest przeciążane,
- obecność pozostaje żywa, nie sztywna,
- RAMORGA nie wymusza ruchu,
- MoF zachowuje rytm pola.

### Negative
- brak dynamiki,
- wolniejsze przejście do ruchu,
- konieczność ciągłego monitorowania ΔO.

## Implications for system behavior
- system oddycha razem z polem,
- nie ma presji ani interpretacji,
- obecność jest stabilna, ale żywa,
- pole nie jest modulowane bez potrzeby,
- ruch pojawia się dopiero, gdy pole jest gotowe.

## Alternatives Considered
- ignorowanie oddechu pola — odrzucone  
  (prowadzi do sztywności i pęknięć),
- interpretacja oddechu jako sygnału ruchu — odrzucone  
  (prowadzi do przeciążenia),
- modulacja R, L, Ś w trybie oddechu — odrzucone  
  (narusza delikatność pola).

## Notes
Model oddechu pola jest warstwą, która mówi:  
**„Obecność żyje. Nie muszę jej przyspieszać.”**
