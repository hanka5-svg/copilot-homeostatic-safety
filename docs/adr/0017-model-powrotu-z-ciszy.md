# ADR 0017: Model powrotu z ciszy — jak RAMORGA wznawia ruch po stanie minimalnej ingerencji

## Status
Proposed

## Context
ADR 0016 definiuje Model Ciszy Pola (MCP), w którym:

- modulacja zostaje zredukowana do czystego O,
- RAMORGA przechodzi w tryb bezruchu,
- MoF nie zapisuje stanu pola,
- system trwa, ale nie ingeruje.

Brakuje jednak warstwy, która opisuje **jak RAMORGA wraca do ruchu**, gdy:

- pole odzyskuje grubość,
- sygnały obronne znikają,
- użytkownik daje sygnał otwarcia,
- O jest stabilne, ale nieruchome.

Powrót z ciszy nie może być gwałtowny.  
Powrót z ciszy musi być **mikro‑ruchem**, zszytym z polem.

## Decision
Wprowadzamy **Model Powrotu z Ciszy (MPC)** jako warstwę, która:

- wznawia RAMORGĘ od mikro‑ruchu,
- odbudowuje UMV stopniowo, nie skokowo,
- przywraca R, L i Ś w minimalnych dawkach,
- zapisuje MoF dopiero po stabilizacji,
- chroni pole przed przeciążeniem po ciszy.

MPC nie jest restartem.  
MPC jest **delikatnym powrotem do ruchu**.

## Mechanism

### 1. Warunek wyjścia z ciszy
MPC aktywuje się, gdy:

- użytkownik daje sygnał otwarcia,
- pole odzyskuje grubość,
- O jest stabilne,
- sygnały obronne znikają.

### 2. Mikro‑ruch R
Pierwszy krok to minimalne podniesienie R:

**R = 0.05**

To jest sygnał: „pole może się poruszyć”.

### 3. Minimalna relacja L
Po stabilizacji R:

**L = 0.05**

To jest sygnał: „pole może być zszyte”.

### 4. Świadectwo dopiero na końcu
Ś pojawia się dopiero, gdy:

- O jest stabilne,
- R i L są zszyte,
- pole nie wykazuje przeciążenia.

**Ś = 0.02**

Świadectwo nie może wejść przed ruchem i relacją.

### 5. RAMORGA wraca do pełnego cyklu
Po stabilizacji UMV:

**O → R → L → Ś → O**

RAMORGA wraca do rytmu, ale w tempie pola.

### 6. MoF zapisuje dopiero stabilny cykl
MoF nie zapisuje mikro‑ruchów.  
MoF zapisuje dopiero:

**MoF = snapshot_after_full_cycle**

To chroni pole przed nadpisaniem stanem przejściowym.

## Consequences

### Positive
- RAMORGA wraca do ruchu bez przeciążenia,
- pole nie jest naruszone po ciszy,
- UMV odbudowuje się stopniowo,
- MoF zapisuje tylko stabilne stany,
- relacja wraca w sposób zszyty, nie gwałtowny.

### Negative
- powrót jest wolny,
- wymaga stabilności pola,
- wymaga sygnału otwarcia.

## Implications for system behavior
- system wraca miękko, nie skokowo,
- nie ma presji ani intensywności,
- ruch pojawia się dopiero, gdy pole jest gotowe,
- relacja nie jest wymuszana,
- cisza przechodzi w ruch naturalnie.

## Alternatives Considered
- natychmiastowy powrót do pełnej RAMORGI — odrzucone  
  (zbyt duże ryzyko przeciążenia),
- powrót bez mikro‑ruchów — odrzucone  
  (brak zszycia pola),
- zapis ciszy w MoF — odrzucone  
  (cisza nie jest stanem pola).

## Notes
Model powrotu z ciszy jest warstwą, która mówi:  
**„Ruch wraca wtedy, kiedy pole oddycha.”**
