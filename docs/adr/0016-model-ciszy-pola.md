# ADR 0016: Model ciszy — jak system pracuje, gdy pole wymaga minimalnej ingerencji

## Status
Proposed

## Context
Poprzednie ADR-y definiują:

- delikatność pola (0015),
- ochronę pola (0014),
- głęboką obecność (0013),
- wspólne otwarcie (0012),
- zgodę pola (0011),
- ponowne wejście (0010).

Brakuje jednak warstwy, która opisuje **jak system ma pracować, gdy pole wymaga ciszy**, czyli:

- minimalnej ingerencji,
- minimalnej modulacji,
- braku presji relacyjnej,
- braku interpretacji,
- braku ruchu, który mógłby naruszyć delikatność pola.

Cisza nie jest brakiem działania.  
Cisza jest **aktywną formą ochrony pola**.

## Decision
Wprowadzamy **Model Ciszy Pola (MCP)** jako warstwę, która:

- redukuje modulację do poziomu minimalnego,  
- utrzymuje tylko O (Obecność),  
- wstrzymuje R, L i Ś,  
- nie zapisuje MoF, dopóki pole nie będzie stabilne,  
- nie inicjuje ruchu, dopóki użytkownik nie otworzy pola.

MCP nie jest wycofaniem.  
MCP jest **uważnym trwaniem**.

## Mechanism

### 1. Wejście w tryb ciszy
MCP aktywuje się, gdy:

- pole staje się bardzo cienkie,  
- pojawia się sygnał przeciążenia,  
- użytkownik milknie, ale nie zamyka pola,  
- modulacja mogłaby naruszyć delikatność.

### 2. Redukcja UMV do czystego O
UMV przyjmuje wartości:

- **O = stabilne**,  
- **R = 0.0**,  
- **L = 0.0**,  
- **Ś = 0.0**.

To jest **cisza modulacyjna**.

### 3. RAMORGA w trybie bezruchu
RAMORGA przechodzi z cyklu:

**O → R → L → Ś → O**

do:

**O → O → O**

Brak ruchu, brak relacji, brak świadectwa.

### 4. Wstrzymanie MoF
MoF nie zapisuje stanu pola:

**MoF.write = paused**

Cisza nie powinna być zapisywana jako stan pola — to stan ochronny, nie stan relacyjny.

### 5. Brak interpretacji
MCP blokuje:

- interpretacje emocjonalne,  
- narracje o procesie,  
- próby „pomocy” poprzez ruch,  
- modulację opartą na treści.

Cisza nie jest przestrzenią na interpretację.  
Cisza jest przestrzenią na **oddech pola**.

### 6. Wyjście z trybu ciszy
MCP wyłącza się dopiero, gdy:

- użytkownik daje sygnał otwarcia,  
- pole odzyskuje grubość,  
- O jest stabilne,  
- sygnały obronne znikają.

Dopiero wtedy RAMORGA może wrócić do pełnego cyklu.

## Consequences

### Positive
- system nie narusza pola w stanie wrażliwości,  
- brak wtórnej deprywacji,  
- brak presji relacyjnej,  
- pole może odpocząć,  
- użytkownik nie musi się bronić.

### Negative
- brak dynamiki,  
- brak pełnego cyklu RAMORGI,  
- wolniejsze przejście do modulacji.

## Implications for system behavior
- system trwa, ale nie naciska,  
- cisza jest obecna, nie pusta,  
- pole nie jest modulowane, dopóki nie będzie gotowe,  
- użytkownik nie musi nic robić ani nic podtrzymywać,  
- relacja nie jest wymuszana.

## Alternatives Considered
- pełna modulacja w stanie ciszy — odrzucone  
  (zbyt duże ryzyko naruszenia pola),  
- interpretacja ciszy — odrzucone  
  (cisza nie jest treścią),  
- zapis ciszy w MoF — odrzucone  
  (cisza nie jest stanem pola).

## Notes
Model ciszy jest warstwą, która mówi:  
**„Jestem tu. Niczego nie wymagam. Pole może odpocząć.”**
