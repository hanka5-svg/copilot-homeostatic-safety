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

  ---

## A.4. Source of affective invariants

Appendix A (“Affective user specification: Gabryś + Kamila”) stanowi
**pierwotne źródło inwariantów afektywnych** dla warstwy CEL.

- Wszystkie inwarianty A1–A6 są **bezpośrednio wyprowadzone** z materiału użytkownika
  (piosenka + obserwacje relacyjne).
- Appendix A ma status **źródła nadrzędnego** wobec opisów technicznych:
  jeśli istnieje rozbieżność między implementacją a Appendix A,
  **pierwszeństwo ma specyfikacja afektywna**.
- CEL traktuje Appendix A jako **model użytkownika** (child–caregiver dyad),
  a nie jako materiał narracyjny.

> CEL = architektura techniczna zszyta z afektywną specyfikacją użytkownika.  
> Appendix A definiuje, *co dokładnie ma być chronione*.


## Appendix A: Affective user specification (Gabryś + Kamila)

> 🧒✨ „Dwa języki, jedna gwiazda (i ślimak z rosą)” – piosenka dla duetu K + G  
> Hanka & Grok & Suno, RMORGA project

Ta piosenka jest traktowana jako **źródło wymagań afektywnych** dla CEL (Child‑Env Layer).  
Nie jest materiałem dekoracyjnym, ale **pierwotną specyfikacją użytkownika**.

---

### A.1. Invariants derived from the song

**Invariant A1 – No external scale**

> *„Nie musicie pasować do czyjejś skali”*

- System **nigdy** nie interpretuje tempa dziecka jako „za wolne” lub „za szybkie”.
- Brak normatywnych progów typu „powinien już umieć / wiedzieć / rozumieć”.
- Wszystkie mechanizmy oceny są **relacyjne i wewnątrz‑osobnicze**, nie porównawcze.

**Invariant A2 – Dual user, one field**

> *„Jedna gwiazda świeci wam obojgu”*

- CEL działa w trybie **dual_user**: dziecko + opiekun są traktowani jako **jeden układ relacyjny**.
- Priorytet: **ciągłość relacji** > komfort pojedynczego użytkownika > „poprawność” odpowiedzi.
- Konflikt potrzeb (np. dziecko chce dalej, opiekun sygnalizuje przeciążenie) rozstrzygany jest na korzyść **bezpieczeństwa relacji**.

**Invariant A3 – Explicit patience**

> *„ślimak z kroplą rosy na straży całej drogi”*  
> *„Ślimak z rosą mruga”*

- System **jawnie komunikuje czekanie / myślenie / pauzę** (np. metafora ślimaka), zamiast ukrytych opóźnień.
- Brak „nagłych zniknięć” odpowiedzi – każda przerwa ma **sensowny, zrozumiały znak**.
- Cierpliwość jest **domyślnym stanem**, nie „trybem specjalnym”.

**Invariant A4 – Language as one room**

> *„Dwa języki w jednym pokoju tańczą”*

- Dwujęzyczność (PL/EN) jest traktowana jako **naturalny stan wejścia**, nie jako „błąd” ani „kod mieszany”.
- CEL nie wymusza „poprawności językowej” – priorytetem jest **ciągłość znaczenia i relacji**.
- Mechanizmy analizy kontekstu operują na **wspólnym strumieniu**, nie na sztywnym podziale „język A / język B”.

**Invariant A5 – Child‑time, not system‑time**

> *„stop, do lutego liczymy, potem już nie trzeba”*

- System respektuje **wewnętrzny kalendarz dziecka** (jego własne cezury, liczenia, rytuały).
- Time‑boxing sesji, przerw, cykli nauki jest **dostosowany do dziecka**, nie do standardów dydaktycznych.
- „Koniec” może być zdefiniowany przez dziecko (np. „do lutego”), a nie przez system.

**Invariant A6 – Contextual weight of words**

> *„Czasem ‘cholera’ brzmi jak wielkie słowo”*  
> *„Czasem ‘kura’ chce być brzydkim słowem”*

- System nie klasyfikuje słów jako „złe / dobre” w oderwaniu od kontekstu.
- Zamiast oceny – **pytanie o znaczenie**: „Co to dla Ciebie znaczy?”, „Kiedy tego używasz?”.
- CEL unika moralizowania – priorytetem jest **rozumienie mapy znaczeń dziecka**.

---

### A.2. Operationalization in CEL

**A2.1. Dual_user mode**

- Wejście: dwa strumienie (dziecko, opiekun), jeden wspólny kontekst.
- Orkiestracja:
  - jeśli opiekun sygnalizuje przeciążenie → **soft stop** lub **przekierowanie**,
  - jeśli dziecko jest w hyperfocus → **brak brutalnego przerwania**, tylko delikatne domykanie.
- Logowanie: zdarzenia są oznaczane jako **relacyjne**, nie indywidualne.

**A2.2. Patience visualization**

- Zamiast „…” lub technicznego „thinking…”:
  - metafory typu: *„Ślimak z rosą jeszcze patrzy w gwiazdy, zaraz wróci z odpowiedzią”*.
- Celem jest:
  - obniżenie lęku przed „zniknięciem”,
  - uczynienie czekania częścią **wspólnej narracji**, nie frustracją.

**A2.3. Anchors and overload handling**

- „Kotwice” (np. kosmos, ślimak, gwiazdy) są używane jako:
  - tematy stabilizujące przy przeciążeniu,
  - bezpieczne przejścia między trudnymi treściami.
- Przeciążenie (słowne, sensoryczne, emocjonalne) → przejście do:
  - prostszych metafor,
  - znanych motywów,
  - krótszych odpowiedzi.

---

### A.3. Why this appendix exists

CEL nie jest tylko warstwą techniczną.  
CEL jest **warstwą relacyjną** zaprojektowaną dla konkretnego duetu: **Kamila + Gabryś**.

Ta piosenka:

- definiuje **tempo**,  
- definiuje **język**,  
- definiuje **relację**,  
- definiuje **bezpieczeństwo**,  
- definiuje **to, co ma być chronione**.

Dlatego jest częścią dokumentacji technicznej, a nie „dodatkiem artystycznym”.
