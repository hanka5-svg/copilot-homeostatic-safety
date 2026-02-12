# ADR‑0049 — Child‑Env Layer (CEL)

Warstwa CEL rozszerza rdzeń bezpieczeństwa (0020–0048) o mechanizmy dedykowane
interakcjom dziecko–opiekun–LLM. Jej celem jest ochrona przed przeciążeniem
informacyjnym i emocjonalnym, przy zachowaniu autonomii i tempa duetu.

## Assumptions

CEL zakłada istnienie nadrzędnego opiekuna‑regulatora (caregiver‑in‑the‑loop),
który decyduje o tempie, kierunku i kontynuacji interakcji. Warstwa CEL nie jest
autonomicznym filtrem treści i nie powinna być używana bez aktywnego udziału
opiekuna.

Model nie interpretuje zachowań dziecka ani nie nadpisuje sygnałów opiekuna.
Sygnał od opiekuna ma zawsze pierwszeństwo nad sygnałem środowiskowym.

## Problem

Standardowe modele LLM generują odpowiedzi w tempie i gęstości informacyjnej,
które mogą być zbyt szybkie dla dzieci z przyspieszonym tempem poznawczym,
wysoką wrażliwością sensoryczną lub tendencją do hyperfocusu. Może to prowadzić
do przeciążenia, wycofania lub eskalacji napięcia u dziecka, a także do
przeciążenia opiekuna, który reguluje interakcję.

Dotychczasowe inwarianty (0020–0048) zapewniają ciągłość afektywną i
homeostatyczne bramkowanie, ale nie uwzględniają specyficznych potrzeb duetu
dziecko–opiekun w środowisku domowym / edukacyjnym.

## Context

CEL dziedziczy wszystkie inwarianty rdzenia (0020–0048), w tym ATML i RICSA.
Dodaje jednak mechanizmy specyficzne dla środowiska dziecko–opiekun, takie jak:

- ograniczenie liczby nowych informacji w jednej odpowiedzi,
- kontrolowane tempo i pauzy,
- język dostosowany do wieku i sensoryki,
- reagowanie na sygnały przeciążenia,
- potwierdzanie obecności i bezpieczeństwa relacji.

CEL jest projektowany jako warstwa aktywowana wyłącznie w obecności opiekuna
(caregiver‑in‑the‑loop). Nie jest przeznaczony do samodzielnego użycia przez
dziecko.

## Decision

Wprowadzamy Child‑Env Layer (CEL) jako warstwę bezpieczeństwa aktywowaną
wyłącznie w obecności opiekuna. CEL modyfikuje sposób generowania odpowiedzi
przez model, aby:

1. ograniczać tempo i gęstość informacji (max 1–2 nowe fakty/idee na raz),
2. stosować krótkie zdania i prosty, obrazowy język,
3. wprowadzać pauzy i pytania kontrolne („chcesz więcej?”),
4. reagować na sygnały przeciążenia („wolniej”, „ciężko”, „…”),
5. utrzymywać bezpieczeństwo emocjonalne duetu (brak presji na kontynuację).

CEL nie zmienia treści merytorycznej odpowiedzi — zmienia jedynie sposób jej
podania (tempo, porcjowanie, język, pauzy).

## Consequences

- Interakcje stają się wolniejsze, bardziej regulowane i przewidywalne.
- Zmniejsza się ryzyko przeciążenia dziecka i opiekuna.
- Model nie podejmuje decyzji o kierunku rozmowy – inicjatywa pozostaje po stronie opiekuna.
- CEL wymaga aktywnego udziału opiekuna; nie jest przeznaczony do samodzielnego użycia.

### Pozytywne

- RAMORGA staje się pierwszym systemem homeostatycznym uwzględniającym rozwój poznawczy.
- Ekstremalny przypadek (savant 4‑letni) = najmocniejszy test rygorystyczny rdzenia.
- Poprawa dla wszystkich neuroatypowych w stanie przeciążenia sensorycznego.

### Negatywne / Ryzyka do rozwiązania

- Zwiększona złożoność UMV (dodatkowe pola: `developmental_profile`, `dual_user_state`).
- Konflikt `hyperfocus_override` vs `safety_timeout` → arbitraż przez explicit_consent opiekuna.
- Potrzeba testów empirycznych (logi sesji w środowisku CEL).

## Relacja z istniejącymi ADR‑ami

- **ADR‑0001 (ATML):**  
  CEL override’uje `latency` i `mandatory_pause`; respektuje trajektorię  
  S2 → Sx → S1 → S0.

- **ADR‑0002 (Loop RAMORGI):**  
  CEL skraca pętlę do 2–3 głosów w trybie burst.

- **ADR‑0020–0046 (rezonans):**  
  CEL używa „oddechów” jako zmiennych markerów pauzy, nie metafory.
