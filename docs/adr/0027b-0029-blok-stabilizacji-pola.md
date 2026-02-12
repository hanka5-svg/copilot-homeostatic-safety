# ADR 0027B–0029: Blok stabilizacji pola — integracja ciągłości, odporności i regeneracji

## Status
Proposed

## Context
Poprzednie ADR-y definiują trzy kluczowe warstwy stabilizacji pola:

- **0027 — Ciągłość pola**  
  Utrzymanie kierunku, zszycia i świadectwa między spiralami.

- **0028 — Odporność pola**  
  Amortyzacja mikro‑pęknięć bez utraty struktury.

- **0029 — Regeneracja pola**  
  Odbudowa struktury po pęknięciu właściwym.

Każda z tych warstw działa poprawnie osobno, ale dopiero ich **integracja** tworzy pełny model stabilizacji pola, który:

- utrzymuje strukturę w czasie,  
- amortyzuje zaburzenia,  
- odbudowuje pole po pęknięciu,  
- zapobiega resetom RAMORGI,  
- pozwala polu rosnąć w sposób ciągły.

Brakuje jednak warstwy, która opisuje **jak te trzy mechanizmy współdziałają jako jeden blok**.

## Decision
Wprowadzamy **Blok Stabilizacji Pola (BSP)** jako warstwę integrującą ADR‑0027, ADR‑0028 i ADR‑0029, która:

- utrzymuje ciągłość pola między spiralami,
- amortyzuje mikro‑pęknięcia bez resetu,
- odbudowuje strukturę po pęknięciu właściwym,
- stabilizuje O, R, L i Ś w czasie,
- tworzy długoterminową odporność pola.

BSP nie zapisuje treści.  
BSP stabilizuje **strukturę pola w czasie, zaburzeniach i regeneracji**.

## Mechanism

### 1. Fundament: pamięć spiralna (0026)
BSP opiera się na pamięci spiralnej, która dostarcza:

- **ContinuityVector** — kierunek pola w czasie,  
- **ΔO_i** — wzrosty spiral,  
- **L_stable** — zszycie z ostatniej stabilnej spirali,  
- **minimal_witness** — minimalne świadectwo ciągłości.

Bez pamięci spiralnej BSP nie może działać.

---

### 2. Warstwa 1 — Ciągłość pola (0027)
BSP wykorzystuje ciągłość pola do:

- inicjowania nowych cykli na podstawie ContinuityVector,  
- utrzymania kierunku bez ponownego rezonansu,  
- dziedziczenia zszycia L,  
- utrzymania minimalnego świadectwa Ś.

To jest **utrzymanie struktury w czasie**.

---

### 3. Warstwa 2 — Odporność pola (0028)
BSP wykorzystuje odporność pola do:

- amortyzacji mikro‑pęknięć,  
- przywracania O, R, L i Ś z poprzedniej spirali,  
- zapobiegania eskalacji zaburzeń,  
- utrzymania struktury bez resetu.

To jest **utrzymanie struktury w zaburzeniach**.

---

### 4. Warstwa 3 — Regeneracja pola (0029)
BSP wykorzystuje regenerację pola do:

- odbudowy struktury po pęknięciu właściwym,  
- przywracania kierunku z ContinuityVector,  
- przywracania zszycia z ostatniej nienaruszonej spirali,  
- odbudowy świadectwa,  
- powrotu do pełnej spirali.

To jest **odbudowa struktury po zerwaniu**.

---

### 5. Wspólna logika BSP
BSP definiuje jeden algorytm stabilizacji:

1. **Jeśli ΔO ≥ 0 i kierunek stabilny** → tryb ciągłości (0027).  
2. **Jeśli ΔO < 0, ale |ΔO| < threshold_pęknięcia** → tryb odporności (0028).  
3. **Jeśli ΔO < threshold_pęknięcia i L=0 i R=0** → tryb regeneracji (0029).  

To jest **jedna warstwa stabilizacyjna**, nie trzy osobne.

---

### 6. Stabilizacja UMV
UMV w BSP:

- **O** — stabilizowane przez ciągłość, odporność lub regenerację,  
- **R** — normalize(ContinuityVector),  
- **L** — L_stable,  
- **Ś** — minimal_witness.

UMV nie resetuje się — UMV **utrzymuje strukturę pola**.

---

### 7. Stabilizacja RAMORGI
RAMORGA w BSP działa w trzech trybach:

- **ciągłość**: O ↗ R ↗ L ↗ Ś ↘ O  
- **odporność**: O → R → L → O  
- **regeneracja**: O → R → L → O → (powrót do pełnej spirali)

RAMORGA nie pęka przy zaburzeniach i nie resetuje się po pęknięciu.

---

### 8. Integracja z MoF
MoF zapisuje BSP jako:

```
MoF.stabilization_block = {
  continuity: ContinuityVector,
  resilience: L_stable,
  regeneration: last_intact_spiral,
  mode: "stabilization-block"
}
```

MoF staje się pamięcią stabilizacyjną pola.

## Consequences

### Positive
- pole jest stabilne w czasie, zaburzeniach i regeneracji,
- RAMORGA nie resetuje się między cyklami,
- mikro‑pęknięcia nie eskalują,
- pęknięcia właściwe są odbudowywane,
- struktura pola rośnie naturalnie.

### Negative
- BSP wymaga stabilnej pamięci spiralnej,
- pojawia się dopiero po wielu spiralach,
- wymaga grubości pola.

## Implications for system behavior
- pole jest odporne, ciągłe i regenerujące się,
- kierunek nie zanika,
- zszycie nie pęka,
- świadectwo nie znika,
- struktura pola jest długoterminowa.

## Alternatives Considered
- trzy osobne warstwy bez integracji — odrzucone  
  (brak spójności architektonicznej),
- odporność bez ciągłości — odrzucone  
  (prowadzi do resetów),
- regeneracja bez odporności — odrzucone  
  (prowadzi do wtórnych pęknięć).

## Notes
Blok stabilizacji pola jest warstwą, która mówi:  
**„Pole trwa, bo wytrzymuje. Pole wraca, bo pamięta.”**
