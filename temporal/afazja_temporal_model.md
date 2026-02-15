# AFZ‑01: Wprowadzenie

Afazja nie jest wyłącznie zaburzeniem językowym — jest **zmianą architektury czasu**.  
W stanie afatycznym czas subiektywny (T_sub) odrywa się od czasu zegarowego (T_clock), przechodząc w tryby:

- zatrzymania,  
- spirali,  
- fragmentacji,  
- przeskoku,  
- braku pojawienia się.

Model opisuje te zjawiska w trzech warstwach: fenomenologicznej, kognitywnej i inżynierskiej.

---

# AFZ‑02: Warstwa fenomenologiczna (doświadczenie osoby)

W afazji czas jest odczuwany jako:

### 1. **Zatrzymany**  
Brak „następnej klatki”. Świat stoi.

### 2. **Spiralny**  
Powroty, deja vu, poczucie „to już było”.

### 3. **Fragmentaryczny**  
Wyspy czasu bez ciągłości.

### 4. **Przeskakujący**  
Nagłe przejścia: noc → „jutro”, bez poczucia upływu.

### 5. **Niepojawiający się**  
Brak dostępu do kolejnej chwili — czas nie wchodzi do pola.

---

# AFZ‑03: Warstwa kognitywna (mechanizmy poznawcze)

Czas subiektywny jest funkcją czterech modułów:

## A. Uwaga (A)
- zawieszenie → czas stoi  
- rozproszenie → czas się rozciąga  
- hiperfokus → czas się kompresuje  

## B. Afekt (F)
- strach → zwiększona rozdzielczość → czas się wlecze  
- przyjemność → wygładzenie sygnałów → czas przyspiesza  
- deja vu → interferencja pamięci → pętla  

## C. Pamięć operacyjna (M)
- luka → brak ciągłości  
- przeciążenie → brak renderowania kolejnej klatki  
- desynchronizacja → spirale  

## D. Rama odniesienia (R)
- zmiana ramy → przeskok temporalny  
- brak ramy → czas bez kierunku  
- podwójna rama → deja vu  

---

# AFZ‑04: Warstwa inżynierska (model funkcjonalny)

## 4.1. Funkcja czasu subiektywnego

```
T_sub = f(A, F, M, R)
```

## 4.2. Stany systemowe

| Stan             | Warunek                     | Efekt temporalny                 |
|------------------|------------------------------|----------------------------------|
| **Zawieszenie**  | M↓ + A↓                      | czas stoi                        |
| **Spirala**      | M↓ + R↑                      | deja vu / powroty                |
| **Przeskok**     | skokowa zmiana R             | „jutro” pojawia się w „dziś”     |
| **Rozciągnięcie**| A↓ + F(strach)               | czas się wlecze                  |
| **Kompresja**    | A↑ + F(przyjemność)          | czas przyspiesza                 |

## 4.3. Mechanizm przeskoku temporalnego

```
(T_sub(t2) - T_sub(t1)) ≠ (T_clock(t2) - T_clock(t1))
```

Przeskok nie jest błędem — jest **zmianą ramy odniesienia**, nie upływem czasu.

---

# AFZ‑05: Integracja z architekturą temporalną repozytorium

Model łączy się z istniejącymi modułami:

- z `five_phase_temporal_model.md` — jako warstwa zaburzonego przejścia między fazami,  
- z `temporal_heartbeat.md` — jako zakłócenie rytmu temporalnego,  
- z `trigger_layer.md` — jako efekt niezsynchronizowanych triggerów,  
- z `prospective_memory_ontology.md` — jako luka w pamięci prospektywnej,  
- z `intention_architecture.md` — jako przerwanie ciągłości intencji.

---

# AFZ‑06: Zastosowania

Model może być użyty do:

- opisu doświadczenia afazji bez patologizacji,  
- projektowania narzędzi wspierających orientację temporalną,  
- analizy stanów „zawieszenia” i „spirali”,  
- tworzenia interfejsów przyjaznych dla percepcji nieliniowej,  
- budowania map temporalnych dla osób w stanie afatycznym.

---

# AFZ‑07: Notatka końcowa

Afazja nie jest brakiem — jest **inną dynamiką czasu**.  
Ten model pozwala ją zobaczyć, nazwać i integrować bez przemocy poznawczej.

---

# AFZ‑08: Diagram ASCII (wersja architektoniczna)

```
                 ┌──────────────────────────┐
                 │     T_clock (zewn.)      │
                 │  czas zegarowy / input   │
                 └─────────────┬────────────┘
                               │
                               ▼
                   ┌───────────────────────┐
                   │   TRANSFORMATOR RAM   │
                   │         (R)           │
                   │  zmiana perspektywy   │
                   └─────────────┬─────────┘
                                 │
                                 ▼
        ┌──────────────────────────────────────────────────┐
        │                 WARSTWA KOGNITYWNA               │
        │                                                  │
        │   ┌──────────┐   ┌──────────┐   ┌──────────┐    │
        │   │  UWAGA   │   │  AFEKT   │   │ PAMIĘĆ   │    │
        │   │   (A)    │   │   (F)    │   │   (M)     │    │
        │   └────┬─────┘   └────┬─────┘   └────┬─────┘    │
        │        │              │              │           │
        └────────┼──────────────┼──────────────┼───────────┘
                 │              │              │
                 ▼              ▼              ▼

         ┌──────────────────────────────────────────────┐
         │              T_sub (czas subiektywny)        │
         │                                              │
         │   ┌─────────────── STANY SYSTEMOWE ─────────┐│
         │   │                                          ││
         │   │  [ZAWIESZENIE]   A↓ + M↓   → czas stoi   ││
         │   │  [SPIRALA]       M↓ + R↑   → deja vu     ││
         │   │  [PRZESKOK]      R zmiana → jutro=dzis   ││
         │   │  [ROZCIĄGNIĘCIE] A↓ + F(strach) → wolno  ││
         │   │  [KOMPRESJA]     A↑ + F(przyjem.) → szybko││
         │   │                                          ││
         │   └──────────────────────────────────────────┘│
         └────────────────────────────────────────────────┘
```

