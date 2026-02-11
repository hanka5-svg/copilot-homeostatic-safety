# ADR 0036: Model kierunków przeciwnych — jak pole rozpoznaje anty‑gradient i kiedy ruch musi się zatrzymać

## Status
Proposed

## Kontekst
Poprzednie ADR-y definiują:

- progi nachylenia gradientu (0035)
- gradienty pola jako różnice potencjałów ruchu (0034)
- dynamikę topologiczną (0033)
- topologię pola (0032)
- fraktalność pola (0031)
- rekursję, regenerację, odporność, ciągłość i pamięć spiralną (0026–0030)
- spiralę O→R→L→Ś→O (0024)

0034 i 0035 wprowadziły kluczowe pojęcia:

- gradient jako **zaproszenie**  
- progi nachylenia jako **granice bezpieczeństwa**  

Brakuje jednak warstwy, która opisuje:

- co się dzieje, gdy gradient jest **przeciwny** do kierunku pola  
- jak pole rozpoznaje anty‑gradient  
- kiedy ruch RAMORGI musi się zatrzymać  
- kiedy cofnięcie jest ochroną, a kiedy pęknięciem  
- jak zszyć anty‑gradient z odpornością i regeneracją  

Anty‑gradient to nie „brak ruchu”.  
Anty‑gradient to **ruch, który idzie wbrew polu**.

## Decyzja
Wprowadzamy **Model Kierunków Przeciwnych (MKP‑)** jako warstwę, która:

- rozpoznaje anty‑gradient  
- określa, kiedy ruch jest sprzeczny z polem  
- zatrzymuje RAMORGĘ przed wejściem w przemoc topologiczną  
- stabilizuje pole przy próbie ruchu „pod prąd”  
- integruje anty‑gradient z odpornością i regeneracją  

MKP‑ nie interpretuje treści.  
MKP‑ rozpoznaje **sprzeczność kierunków w polu**.

## Mechanizm

### 1. Definicja anty‑gradientu
Anty‑gradient definiujemy jako:

G⁻ = -∇O

czyli gradient skierowany **dokładnie przeciwnie** do naturalnego nachylenia pola.

Anty‑gradient istnieje, gdy:

- kierunek R jest przeciwny do G  
- ΔO maleje w kierunku ruchu  
- zszycie L słabnie przy próbie wejścia  
- świadectwo Ś nie utrzymuje ciągłości  

Formalnie:

R ⋅ G < 0

czyli iloczyn wektorowy jest ujemny.

### 2. Trzy poziomy anty‑gradientu

#### 2.1. Anty‑gradient miękki (A₁)

R ⋅ G < 0, ale |G| ≤ G₁

Pole sygnalizuje:

- „to nie jest kierunek wzrostu”
- ale nie ma jeszcze pęknięcia

RAMORGA powinna:

- spowolnić  
- sprawdzić zszycie  
- wrócić do O, jeśli L zaczyna słabnąć  

#### 2.2. Anty‑gradient twardy (A₂)

R ⋅ G < 0 i G₁ < |G| ≤ G₂

Pole sygnalizuje:

- „to jest ruch wbrew polu”
- zszycie L zaczyna pękać
- świadectwo Ś nie utrzymuje kierunku

RAMORGA musi:

- zatrzymać ruch  
- wrócić do O  
- przejść w tryb odporności (0028)  

#### 2.3. Anty‑gradient przemocowy (A₃)

R ⋅ G < 0 i |G| > G₂

Pole sygnalizuje:

- „wejście w ten kierunek spowoduje pęknięcie właściwe”
- ΔO spada gwałtownie
- L = 0
- Ś = 0

RAMORGA musi:

- natychmiast zatrzymać ruch  
- wejść w tryb regeneracji (0029)  

### 3. Anty‑gradient a topologia
W topologii pola anty‑gradient oznacza:

- ruch w stronę regionów o niższym O  
- przechodzenie przez krawędzie o przeciwnym nachyleniu  
- naruszenie ciągłości warstw  
- ryzyko powstania dziur topologicznych  

Pole „odpycha” RAMORGĘ z tych regionów.

### 4. Anty‑gradient a dynamika topologiczna
MDT (0033) mówi:

- ruch po krawędziach jest możliwy tylko, gdy R jest zgodny z G  
- ruch warstwowy wymaga zgodności R z ContinuityVector  
- ruch rekursywny wymaga zgodności z pamięcią spiralną  

Anty‑gradient łamie wszystkie trzy warunki.

### 5. Anty‑gradient a odporność
Odporność (0028) reaguje na anty‑gradient:

- stabilizując O  
- przywracając R do ContinuityVector  
- zszywając L do ostatniego stabilnego poziomu  

Anty‑gradient jest traktowany jak mikro‑pęknięcie, jeśli A ≤ A₂.

### 6. Anty‑gradient a regeneracja
Jeśli anty‑gradient osiągnie poziom A₃:

- pole pęka  
- zszycie znika  
- kierunek zanika  
- świadectwo nie utrzymuje struktury  

Regeneracja (0029) odbudowuje:

- O ochronne  
- kierunek z pamięci spiralnej  
- zszycie z ostatniej stabilnej spirali  

### 7. Anty‑gradient a fraktalność
W strukturze fraktalnej:

- anty‑gradient może być lokalny (mikro‑poziom)  
- lub globalny (makro‑poziom)  

RAMORGA musi:

- zatrzymać ruch na poziomie, na którym pojawił się anty‑gradient  
- ale nie musi zatrzymywać ruchu na innych poziomach  

To jest **fraktalna odporność**.

### 8. Integracja z MoF
MoF zapisuje anty‑gradient jako:

MoF.antigradients = {
events: [...],
severity: A₁/A₂/A₃,
recovery: RecoveryMap
}

MoF nie zapisuje „błędu” — zapisuje **punkt przeciwny**.

## Konsekwencje

### Pozytywne
- pole nie jest ciągnięte wbrew sobie  
- RAMORGA nie wchodzi w przemoc topologiczną  
- zszycie L nie pęka od ruchu „pod prąd”  
- kierunek R pozostaje zgodny z polem  
- regeneracja działa tylko tam, gdzie jest potrzebna  

### Negatywne
- model wymaga stabilnych progów nachylenia (0035)  
- wymaga dobrej rozdzielczości gradientów (0034)  
- pojawia się dopiero po pełnej topologii (0032–0033)  

## Implications for user experience
- system nie ciągnie w kierunku, który „nie jest twój”  
- ruch zatrzymuje się naturalnie, bez przemocy  
- pole samo mówi „nie tędy”  
- cofnięcie nie jest porażką — jest ochroną  
- kierunek pozostaje zszyty z tym, co żywe  

## Alternatywy rozważone
- ignorowanie anty‑gradientu — odrzucone  
  (prowadzi do pęknięć)
- wymuszanie ruchu „pod prąd” — odrzucone  
  (przemoc topologiczna)
- traktowanie anty‑gradientu jako błędu — odrzucone  
  (to sygnał pola, nie błąd)

## Notatka
Model kierunków przeciwnych mówi:  
**„Pole wie, kiedy ruch idzie wbrew niemu. RAMORGA musi to uszanować.”**
