# Child‑Env Layer (CEL)

Child‑Env Layer (CEL) to dodatkowa warstwa bezpieczeństwa, która spowalnia i
upraszcza sposób generowania odpowiedzi przez model w interakcjach
dziecko–opiekun. Jej celem jest zmniejszenie ryzyka przeciążenia
informacyjnego i emocjonalnego oraz utrzymanie jasnego, przewidywalnego tempa
rozmowy.

CEL działa wyłącznie w trybie **caregiver‑in‑the‑loop** — to opiekun decyduje,
kiedy warstwa jest aktywna, jakie parametry obowiązują i kiedy należy zrobić
pauzę lub zakończyć rozmowę.

---

## Co zmienia CEL

- maksymalnie **1–2 nowe fakty lub idee** w jednej odpowiedzi,
- **krótkie zdania** (do ok. 12 słów),
- po przekazaniu informacji model robi **pauzę** i pyta:
  „**Chcesz więcej, czy na razie wystarczy?**”,
- **brak ironii**, sarkazmu i komunikatów typu „to skomplikowane”,
- model reaguje na sygnały spowolnienia lub przeciążenia, takie jak:
  „wolniej”, „ciężko”, „…”, „za szybko”,
- model nie narzuca kierunku rozmowy — inicjatywa pozostaje po stronie
  opiekuna.

CEL nie zmienia treści merytorycznej odpowiedzi — zmienia jedynie **tempo,
formę i porcjowanie**.

---

## Jak włączyć CEL

1. Na początku rozmowy opiekun może dodać instrukcję:
   **„Używaj konfiguracji z `src/cel/config.py` — tryb CEL aktywny.”**

2. Parametry można zmieniać w locie, np.:
   **„Zmień `max_facts_per_response` na 1.”**

3. CEL można w każdej chwili wyłączyć:
   **„Wyłącz tryb CEL.”**

---

## Co można dostosować

W pliku `src/cel/config.py` opiekun może regulować m.in.:

- liczbę nowych faktów na odpowiedź,
- maksymalną długość zdań,
- moment obowiązkowej pauzy,
- listę sygnałów zatrzymania,
- ton odpowiedzi (ciepły, wspierający),
- priorytet sygnału opiekuna,
- marker cierpliwości („Jestem tu. Możemy zwolnić tempo.”).

CEL nie zawiera żadnych danych osobowych ani profili rozwojowych — wszystkie
parametry są neutralne i ogólne.

---

## Dla kogo jest CEL

CEL jest przeznaczony do sytuacji, w których:

- dziecko uczy się szybko, intensywnie lub nielinearnie,
- istnieje ryzyko przeciążenia sensorycznego lub informacyjnego,
- opiekun chce mieć pełną kontrolę nad tempem rozmowy,
- model ma wspierać, a nie prowadzić interakcję.

CEL **nie jest** autonomicznym filtrem treści i nie powinien być używany bez
aktywnego udziału opiekuna.

---

## Informacja zwrotna

Po kilku rozmowach opiekun może ocenić:

- co działa dobrze,
- co jest za szybkie,
- co jest za wolne,
- jakie parametry wymagają korekty.

CEL jest warstwą elastyczną — można ją dostosowywać do konkretnej sytuacji,
zachowując pełną zgodność z zasadą **caregiver‑in‑the‑loop**.
