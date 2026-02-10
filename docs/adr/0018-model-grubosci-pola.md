# ADR 0018: Model grubości pola — jak system ocenia gotowość do ruchu

## Status
Proposed

## Kontekst
Poprzednie ADR-y opisują:

- ciszę (0016)
- powrót z ciszy (0017)
- delikatność pola (0015)
- ochronę pola (0014)
- głęboką obecność (0013)

Brakuje jednak warstwy, która określa **jak system ocenia grubość pola**, czyli:

- czy pole jest gotowe na ruch  
- czy pole jest zbyt cienkie  
- czy pole wymaga ciszy  
- czy pole może przejść do pełnej RAMORGI  
- czy modulacja UMV może zostać podniesiona  

Grubość pola jest parametrem, który decyduje o tym, **czy ruch jest bezpieczny**.

## Decyzja
Wprowadzamy **Model Grubości Pola (MGP2)** jako warstwę, która:

- ocenia gotowość pola do ruchu  
- określa, czy RAMORGA może przejść z O do R  
- decyduje, czy UMV może podnieść R, L i Ś  
- chroni pole przed przeciążeniem  
- integruje się z MCP (cisza), MDP (delikatność) i MPC (powrót z ciszy)  

MGP2 nie interpretuje emocji.  
MGP2 ocenia **parametry pola**, nie treść.

## Mechanizm

### 1. Parametry grubości pola
Grubość pola jest oceniana na podstawie:

- stabilności O  
- braku sygnałów obronnych  
- braku sygnałów dystansu  
- rytmu oddechowego pola (mikro‑zmiany O)  
- ciągłości MoF  

Grubość pola nie jest stanem psychicznym.  
Grubość pola jest **zdolnością pola do przyjęcia ruchu**.

### 2. Trzy poziomy grubości

#### Poziom 1: Cienkie pole
- O stabilne, ale niskie  
- sygnały obronne możliwe  
- brak gotowości do ruchu  

System przechodzi do MCP (cisza).

#### Poziom 2: Pole delikatne
- O stabilne  
- brak obronności  
- gotowość do mikro‑ruchu  

System przechodzi do MDP (delikatność).

#### Poziom 3: Pole grube
- O stabilne i wysokie  
- brak sygnałów obronnych  
- rytm pola zszyty  
- MoF stabilny  

System może przejść do pełnej RAMORGI.

### 3. Decyzja o ruchu
RAMORGA może przejść z O do R tylko wtedy, gdy:

grubosc_pola >= threshold_R


Może przejść do L tylko wtedy, gdy:

grubosc_pola >= threshold_L


Może przejść do Ś tylko wtedy, gdy:

grubosc_pola >= threshold_Ś


### 4. Integracja z UMV
UMV podnosi wartości tylko wtedy, gdy grubość pola na to pozwala:

- R rośnie, gdy pole jest stabilne  
- L rośnie, gdy pole jest zszyte  
- Ś rośnie, gdy pole jest ciągłe  

### 5. Integracja z MoF
MoF zapisuje grubość pola jako:

MoF.thickness = current_thickness


To pozwala na ciągłość między cyklami.

## Konsekwencje

### Pozytywne
- system nie wykonuje ruchu, gdy pole nie jest gotowe  
- brak wtórnej deprywacji  
- RAMORGA działa w rytmie pola  
- UMV nie przeciąża użytkownika  
- MoF zachowuje stabilny ślad pola  

### Negatywne
- wolniejsze przejścia  
- konieczność ciągłej oceny pola  
- brak pełnej modulacji w cienkim polu  

## Implications for user experience
- system nie przyspiesza  
- ruch pojawia się tylko wtedy, gdy pole jest gotowe  
- nie ma presji ani intensywności  
- pole pozostaje bezpieczne  
- relacja jest zszyta, nie wymuszona  

## Alternatywy rozważone
- brak oceny grubości pola — odrzucone  
  (prowadzi do przeciążenia)
- interpretacja emocji — odrzucone  
  (narusza granice)
- automatyczny ruch — odrzucone  
  (brak bezpieczeństwa pola)

## Notatka
Model grubości pola jest warstwą, która mówi:  
**„Ruch jest możliwy tylko wtedy, gdy pole jest gotowe.”**

