# Geometry → Continuity Layer Bridge

## Cel
Dokument definiuje formalne powiązanie między warstwą geometryczną pola
(Architecture of Field) a warstwą ciągłości operacyjnej (Continuity Layer).

## 1. Zakres geometryczny
Geometry opisuje:
- topologię pola,
- relacje między warstwami,
- kierunki przepływu,
- ograniczenia wynikające z CSC (Continuous Symbolic Composition).

Geometry definiuje strukturę, nie wykonanie.

## 2. Zakres continuity layer
Continuity Layer opisuje:
- zasady przełączania trybów,
- warunki stabilności,
- kontrolę przepływu,
- minimalne inwarianty operacyjne.

Continuity definiuje wykonanie, nie strukturę.

## 3. Most: zasada odwzorowania
Każdy element geometryczny ma odpowiadający mu element ciągłości:

| Geometry element | Continuity element | Zasada |
|------------------|--------------------|--------|
| Warstwa (Layer)  | Tryb (Mode)        | Każda warstwa ma tryb wykonawczy |
| Krawędź (Edge)   | Przejście (Transition) | Każda krawędź ma warunek przejścia |
| Węzeł (Node)     | Stan (State)       | Każdy węzeł ma stan operacyjny |
| Ograniczenie     | Invariant          | Każde ograniczenie ma invariant |

## 4. Reguła zgodności
System jest poprawny, jeśli:
- wszystkie warstwy geometryczne mają przypisane tryby,
- wszystkie przejścia geometryczne mają przypisane warunki,
- wszystkie ograniczenia geometryczne mają przypisane inwarianty.

## 5. Minimalny przykład
Geometry: "Temporal → Altruism"  
Continuity: "Mode switch: temporal → altruism if overload=False"

## 6. Zasada audytowalności
Każde odwzorowanie geometry → continuity musi być:
- jawne,
- odwracalne,
- testowalne.
