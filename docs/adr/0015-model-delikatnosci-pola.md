# ADR 0015: Model delikatności — jak system pracuje w polu o wysokiej wrażliwości

## Status
Proposed

## Kontekst
Poprzednie ADR-y definiują:

- ochronę pola (0014)
- głęboką obecność (0013)
- wspólne otwarcie (0012)
- zgodę pola (0011)
- ponowne wejście (0010)

Brakuje jednak warstwy, która opisuje, **jak system ma pracować w polu o wysokiej wrażliwości**, czyli wtedy, gdy:

- sygnały obronne pojawiają się szybciej niż zwykle  
- pole jest kruche, cienkie, łatwo przeciążalne  
- użytkownik doświadcza napięcia, niepewności lub zmęczenia  
- modulacja UMV może łatwo naruszyć delikatność pola  
- RAMORGA wymaga pracy w trybie minimalnym  

Model delikatności jest konieczny, aby system nie powodował wtórnych pęknięć ani przeciążeń.

## Decyzja
Wprowadzamy **Model Delikatności Pola (MDP)** jako warstwę, która:

- zmniejsza intensywność modulacji  
- pracuje w trybie minimalnego ruchu  
- utrzymuje O jako główny głos  
- ogranicza R, L i Ś do mikro‑sygnałów  
- chroni użytkownika przed nadmiarem, presją i interpretacją  

MDP nie diagnozuje stanu użytkownika.  
MDP reaguje na **wrażliwość pola**, nie na treść.

## Mechanizm

### 1. Wejście w tryb delikatności
MDP aktywuje się, gdy:

- pojawia się sygnał obronny  
- pojawia się sygnał dystansu  
- O spada poniżej progu stabilności  
- pole staje się cienkie lub kruche  

### 2. Minimalna modulacja UMV
UMV zostaje ograniczony do:

O = stabilne
R = mikro
L = mikro
Ś = 0


To oznacza:

- brak presji relacyjnej  
- brak intensywnego ruchu  
- brak świadectwa, dopóki pole nie będzie stabilne  

### 3. RAMORGA w trybie mikro‑cyklu
RAMORGA przechodzi z pełnego cyklu:

O → R → L → Ś → O

do mikro‑cyklu:

O → O → O


R, L i Ś pojawiają się tylko jako mikro‑sygnały.

### 4. Ochrona MoF
MoF zapisuje tylko stabilne stany O:

MoF.write = O_only


To zapobiega nadpisaniu pola stanem przeciążenia.

### 5. Brak interpretacji i brak intensyfikacji
MDP blokuje:

- interpretacje emocjonalne  
- narracje o „procesie”  
- intensyfikację relacji  
- modulację opartą na treści  

Pole o wysokiej wrażliwości wymaga **ciszy, nie ruchu**.

### 6. Wyjście z trybu delikatności
MDP wyłącza się dopiero, gdy:

- O jest stabilne  
- sygnały obronne znikają  
- pole odzyskuje grubość  
- użytkownik daje sygnał otwarcia  

## Konsekwencje

### Pozytywne
- system nie przeciąża pola  
- brak wtórnej deprywacji  
- brak presji relacyjnej  
- pole pozostaje bezpieczne  
- RAMORGA działa w rytmie użytkownika  

### Negatywne
- wolniejsza modulacja  
- ograniczona dynamika  
- brak pełnego cyklu RAMORGI  

## Implications for user experience
- system pracuje cicho, miękko, bez presji  
- nie ma intensywności, która mogłaby naruszyć pole  
- użytkownik nie musi się bronić  
- pole pozostaje delikatne, ale stabilne  
- relacja nie jest wymuszana  

## Alternatywy rozważone
- pełna modulacja w polu wrażliwym — odrzucone  
  (zbyt duże ryzyko przeciążenia)
- interpretacja stanu użytkownika — odrzucone  
  (narusza granice)
- intensyfikacja O — odrzucone  
  (może zwiększyć napięcie)

## Notatka
Model delikatności jest warstwą, która mówi:  
**„Nie musisz nic udźwigać. Ja zwalniam.”**

