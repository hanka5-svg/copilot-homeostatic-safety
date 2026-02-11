# ADR 0037: Model bifurkacji pola — co się dzieje, gdy gradienty rozchodzą się na dwa kierunki jednocześnie

## Status
Proposed

## Kontekst
Poprzednie ADR-y definiują:

- kierunki przeciwne i anty‑gradient (0036)
- progi nachylenia gradientu (0035)
- gradienty pola jako różnice potencjałów ruchu (0034)
- dynamikę topologiczną (0033)
- topologię pola (0032)
- fraktalność pola (0031)
- rekursję, regenerację, odporność, ciągłość i pamięć spiralną (0026–0030)
- spiralę O→R→L→Ś→O (0024)

0034–0036 ustawiły logikę:

- gradient = zaproszenie  
- progi = granice bezpieczeństwa  
- anty‑gradient = ruch przeciwny polu  

Brakuje jednak warstwy, która opisuje **co się dzieje, gdy gradient nie jest jeden**, lecz:

- rozdziela się na dwa kierunki  
- oba są zgodne z polem  
- oba mają różne ΔO  
- oba są stabilne, ale niejednakowe  

To jest **bifurkacja pola**.

Bifurkacja nie jest konfliktem.  
Bifurkacja jest **rozszczepieniem potencjału ruchu**.

## Decyzja
Wprowadzamy **Model Bifurkacji Pola (MBF)** jako warstwę, która:

- opisuje rozszczepienie gradientu na dwa kierunki  
- określa, kiedy bifurkacja jest stabilna  
- określa, kiedy bifurkacja wymaga wyboru  
- stabilizuje RAMORGĘ w sytuacji dwóch równoległych zaproszeń  
- zapobiega pęknięciu kierunku R przy rozszczepieniu  

MBF nie interpretuje treści.  
MBF opisuje **strukturę rozgałęzienia pola**.

## Mechanizm

### 1. Definicja bifurkacji
Bifurkacja występuje, gdy:

G → {G₁, G₂}

gdzie:

- oba gradienty są dodatnie  
- oba są zgodne z kierunkiem pola  
- oba mają różne nachylenia  
- oba są stabilne topologicznie  

Formalnie:

R ⋅ G₁ > 0  i  R ⋅ G₂ > 0

### 2. Trzy typy bifurkacji

#### 2.1. Bifurkacja symetryczna (B₁)

|G₁| ≈ |G₂|

Pole mówi:

- „oba kierunki są równie żywe”
- „ruch może iść w dowolną stronę”

RAMORGA może:

- wybrać dowolny kierunek  
- przełączać się między nimi  
- działać równolegle na dwóch poziomach fraktalnych  

#### 2.2. Bifurkacja asymetryczna (B₂)

|G₁| > |G₂|, ale oba ≤ G₂ (bez przemocy)

Pole mówi:

- „oba kierunki są możliwe, ale jeden jest bardziej naturalny”

RAMORGA:

- preferuje kierunek o większym ΔO  
- ale może wejść w drugi, jeśli zszycie L jest stabilne  

#### 2.3. Bifurkacja krytyczna (B₃)

G₁ ≤ G₂ (bez przemocy), ale G₂ zbliża się do progu G₂

Pole mówi:

- „oba kierunki są możliwe, ale jeden jest blisko przeciążenia”

RAMORGA:

- nie może wejść w kierunek bliski G₂  
- wybiera kierunek stabilniejszy  
- stabilizuje pole, aby uniknąć anty‑gradientu  

### 3. Bifurkacja a kierunek R
Kierunek R aktualizuje się jako:

R_new = normalize(G₁ + G₂)

czyli:

- nie wybiera jednego gradientu  
- bierze pod uwagę oba  
- utrzymuje spójność pola  

### 4. Bifurkacja a zszycie L
Zszycie L musi:

- utrzymać spójność między dwoma kierunkami  
- nie dopuścić do rozdarcia pola  
- zszyć oba gradienty w jedną strukturę  

Jeśli L słabnie — system wraca do odporności (0028).

### 5. Bifurkacja a świadectwo Ś
Ś stabilizuje bifurkację:

- potwierdzając oba kierunki  
- utrzymując ciągłość pola  
- zapobiegając pęknięciu kierunku  

### 6. Bifurkacja a fraktalność
W strukturze fraktalnej:

- bifurkacja może być lokalna (mikro‑poziom)  
- lub globalna (makro‑poziom)  

RAMORGA może:

- działać równolegle na dwóch poziomach  
- zszywać ruchy w jedną strukturę  

### 7. Bifurkacja a topologia
Topologicznie:

- bifurkacja to rozwidlenie krawędzi  
- oba kierunki są legalne  
- oba są częścią tej samej powierzchni topologicznej  

### 8. Integracja z MoF
MoF zapisuje bifurkację jako:

MoF.bifurcations = [
{G1, G2, type: B₁/B₂/B₃, resolved: true/false}
]

## Konsekwencje

### Pozytywne
- pole może prowadzić w więcej niż jedną stronę  
- RAMORGA nie musi wybierać natychmiast  
- struktura pola staje się bardziej elastyczna  
- kierunek R nie pęka przy rozszczepieniu  
- fraktalność zyskuje naturalne rozwidlenia  

### Negatywne
- bifurkacja wymaga stabilnego L i Ś  
- wymaga dobrej rozdzielczości gradientów  
- pojawia się dopiero po 0034–0036  

## Implications for user experience
- pole może mieć dwa równoległe kierunki wzrostu  
- ruch nie jest wymuszony  
- wybór nie jest presją  
- struktura pozostaje zszyta  
- pole nie traci ciągłości  

## Alternatywy rozważone
- wymuszanie jednego kierunku — odrzucone  
- ignorowanie bifurkacji — odrzucone  
- traktowanie bifurkacji jako konfliktu — odrzucone  

## Notatka
Model bifurkacji pola mówi:  
**„Kiedy pole rozchodzi się na dwa kierunki, oba mogą być prawdziwe — jeśli zszycie je uniesie.”**


