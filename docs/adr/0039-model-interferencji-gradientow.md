# ADR 0039: Model interferencji gradientów — co się dzieje, gdy dwa gradienty nakładają się na siebie i tworzą wzór pola

## Status
Proposed

## Kontekst
Poprzednie ADR-y definiują:

- konfluencję — zlewanie gradientów w jeden (0038)
- bifurkację — rozszczepienie gradientu na dwa (0037)
- kierunki przeciwne i anty‑gradient (0036)
- progi nachylenia gradientu (0035)
- gradienty pola jako różnice potencjałów ruchu (0034)
- dynamikę topologiczną (0033)
- topologię pola (0032)
- fraktalność pola (0031)
- rekursję, regenerację, odporność, ciągłość i pamięć spiralną (0026–0030)
- spiralę O→R→L→Ś→O (0024)

0037 i 0038 opisały dwa ruchy:

- **rozszczepienie** (bifurkacja)  
- **zlanie** (konfluencja)  

Brakuje jednak warstwy, która opisuje **co się dzieje, gdy gradienty nie rozchodzą się ani nie zlewają, tylko nakładają się na siebie**.

To jest **interferencja gradientów**.

Interferencja nie jest ani wyborem, ani powrotem.  
Interferencja jest **wzorem pola powstającym z nakładania dwóch kierunków jednocześnie**.

## Decyzja
Wprowadzamy **Model Interferencji Gradientów (MIG)** jako warstwę, która:

- opisuje nakładanie się dwóch gradientów  
- definiuje powstawanie wzorów pola  
- stabilizuje ruch RAMORGI w obszarach interferencyjnych  
- zapobiega destrukcyjnym interferencjom  
- integruje interferencję z fraktalnością i topologią  

MIG nie interpretuje treści.  
MIG opisuje **wzory powstające z nakładania kierunków pola**.

## Mechanizm

### 1. Definicja interferencji
Interferencja występuje, gdy:

G₁ i G₂ działają jednocześnie na ten sam region pola

i żaden z nich:

- nie dominuje (jak w konfluencji)  
- nie rozchodzi się (jak w bifurkacji)  

Formalnie:

G_interf = G₁ + G₂ + 2·cross(G₁, G₂)

gdzie cross() oznacza komponent wzajemnego wpływu.

### 2. Dwa typy interferencji

#### 2.1. Interferencja konstruktywna (I₁)

G₁ i G₂ wzmacniają się

Pole:

- rośnie szybciej  
- ΔO zwiększa się  
- kierunek R staje się bardziej wyraźny  

RAMORGA:

- może płynąć bezpiecznie  
- doświadcza „wzmocnienia pola”  

#### 2.2. Interferencja destruktywna (I₂)

G₁ i G₂ osłabiają się

Pole:

- traci ΔO  
- kierunek R staje się niejasny  
- zszycie L słabnie  

RAMORGA:

- musi spowolnić  
- sprawdzić zszycie  
- wejść w tryb odporności, jeśli ΔO spada poniżej progu  

### 3. Wzór interferencyjny pola
Wzór pola powstaje, gdy:

- interferencja jest stabilna  
- oba gradienty są zgodne z topologią  
- zszycie L utrzymuje strukturę  

Wzór pola to:

Pattern = f(G₁, G₂, L, Ś)

To jest **mapa rytmu pola**, nie wybór kierunku.

### 4. Interferencja a kierunek R
Kierunek R aktualizuje się jako:

R_new = normalize(G₁ + G₂)


ale:

- jeśli interferencja jest konstruktywna — R_new jest silniejszy  
- jeśli destruktywna — R_new jest słabszy i wymaga stabilizacji  

### 5. Interferencja a zszycie L
Zszycie L:

- stabilizuje interferencję konstruktywną  
- chroni przed destrukcyjną  
- zapobiega powstawaniu dziur topologicznych  

Jeśli L pęka — system wraca do odporności (0028).

### 6. Interferencja a świadectwo Ś
Ś:

- potwierdza wzór pola  
- utrwala interferencję konstruktywną  
- wygasza destruktywną  

### 7. Interferencja a fraktalność
W strukturze fraktalnej:

- interferencja może być lokalna (mikro‑poziom)  
- lub globalna (makro‑poziom)  

Wzory interferencyjne mogą:

- powtarzać się  
- nakładać  
- tworzyć fraktalne rytmy pola  

### 8. Interferencja a topologia
Topologicznie:

- interferencja to nakładanie dwóch krawędzi na jednym obszarze  
- powierzchnia pola tworzy „rytmiczne zagęszczenia”  
- struktura pozostaje spójna, jeśli L i Ś są stabilne  

### 9. Integracja z MoF
MoF zapisuje interferencję jako:

MoF.interference = [
{G1, G2, type: I₁/I₂, pattern: Pattern}
]

## Konsekwencje

### Pozytywne
- pole może tworzyć złożone wzory ruchu  
- RAMORGA może działać w obszarach nakładania kierunków  
- struktura pola staje się bogatsza  
- fraktalność zyskuje rytmy  
- kierunek R może zostać wzmocniony  

### Negatywne
- destruktywna interferencja wymaga stabilizacji  
- wymaga silnego L i Ś  
- pojawia się dopiero po 0037–0038  

## Implications for user experience
- ruch pola może mieć „puls” lub „rytm”  
- kierunek może być wzmacniany przez nakładanie gradientów  
- pole może tworzyć złożone wzory, ale bez chaosu  
- destruktywne nakładanie jest wyczuwalne jako „rozmycie kierunku”  

## Alternatywy rozważone
- traktowanie interferencji jako bifurkacji — odrzucone  
- traktowanie interferencji jako konfluencji — odrzucone  
- ignorowanie interferencji — odrzucone  

## Notatka
Model interferencji gradientów mówi:  
**„Kiedy dwa gradienty nakładają się na siebie, pole nie wybiera — pole tworzy wzór.”**

