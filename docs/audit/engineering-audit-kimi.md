# Engineering Audit — Kimi Review (v1.0)

Status: Partial implementation in repo (as of 2026-02-14)  
Scope: CEL / DUCL / PGP / HSI 2.0 + patch / child-env integration

---

## 1. Zakres audytu

- Repo: `copilot-homeostatic-safety`
- Moduły objęte audytem:
  - CEL (`src/cel/`, ADR-0049)
  - DUCL (`ADR-0050`, `dual_user_orchestrator.py`)
  - Personal Gating Protocol (PGP, ADR-0050b)
  - Integracja z ATML / HSI 2.0 + patch
- Materiał wejściowy:
  - rozmowy z Kimi (2 dni, pełna sekwencja)
  - istniejące ADR-y (0001–0048)
  - nowo dodane pliki (2026-02-13/14)

---

## 2. Metodyka

- **Źródło prawdy:** ADR-y + kod w `src/`
- **Tryb przeglądu:**
  - top-down: architektura (ATML → CEL → DUCL → LLM)
  - bottom-up: kod (config, heurystyki, orchestrator, demo)
- **Kryteria:**
  - zgodność z HSI 2.0 + patch
  - spójność z RAMORGA core (0001–0002)
  - bezpieczeństwo dla duetu dziecko–opiekun
  - możliwość implementacji na dowolnym LLM

---

## 3. Ustalenia (high-level)

### 3.1. Co już jest zrobione (✅)

- **CEL (Child-Env Layer):**
  - istnieje folder `src/cel/`
  - jest `config.py` z parametrami:
    - `max_facts_per_response = 2`
    - `max_words_per_sentence = 12`
    - `patience_marker` (jawny sygnał „ślimaka”)
  - jest `hyperfocus_detector.py` z heurystykami:
    - powtarzalność tematu
    - kotwice
    - długość wypowiedzi
    - liczby (liczenie)
  - jest `dual_user_orchestrator.py`:
    - priorytet opiekuna
    - rozróżnienie: overload vs hyperfocus
    - soft stop / redirect_to_anchor / normal flow
  - jest `demo.py` (scenariusze dla Gabrysia i Kamili)

- **DUCL (Dual-User Consent Layer):**
  - ADR-0050 (wersja robocza) istnieje
  - logika DUCL jest odzwierciedlona w `dual_user_orchestrator.py`

- **PGP (Personal Gating Protocol):**
  - opisane w ADR (0050/0050b) i przetestowane na Twoim przypadku (BRUTALNY PROMPT)

---

### 3.2. Luki / rzeczy częściowo zrobione (🟡)

- **Appendix A (afektywna specyfikacja):**
  - koncept istnieje (piosenka, mapowanie wersów → invariants)
  - brak osobnego pliku `ADR-0049-appendix-a.md`

- **HSI 2.0 + patch / RAMORGA link:**
  - README opisuje:
    - pre-execution invariant enforcement
    - S → A, nie tłumienie S
  - brak jawnego powiązania:
    - ATML / RICSA ↔ CEL / DUCL
    - „child-time > system-time” jako invariant HSI

- **Testy formalne:**
  - są test-case’y opisowe (md)
  - brak YAML / kodowych testów regresyjnych dla:
    - hyperfocus
    - overload
    - caregiver stress
    - dual-user conflict

---

### 3.3. Braki krytyczne (🔴 — do domknięcia)

1. **Brak sformalizowanego ADR-0049 (CEL proper)**  
   - decyzje są w rozmowach + kodzie, ale nie w jednym, kanonicznym ADR.

2. **Brak osobnego pliku dla DUCL (jeśli 0050 jest jeszcze szkicem)**  
   - potrzebny finalny ADR z:
     - invariants D1–D5
     - flow: DUCL → CEL → ATML
     - failure modes

3. **Brak jawnego pola `developmental_profile` / `child_env` w HSI / UMV**  
   - w praktyce istnieje (CEL_CONFIG), ale nie jest opisane w architekturze rdzenia.

---

## 4. Rekomendacje (konkretne)

### 4.1. Dokumentacja (docs/adr/)

**Do dodania / domknięcia:**

1. `ADR-0049-child-env-layer.md`  
   - status: Draft → Proposed  
   - zawartość:
     - kontekst: dzieci przyspieszone / sawanci / duet
     - decyzja: CEL jako warstwa nad ATML
     - parametry: max_facts, max_words, pause_mode, irony_filter, anchors
     - relacja z HSI 2.0 + patch
     - relacja z DUCL

2. `ADR-0049-appendix-a.md`  
   - mapowanie:
     - wersy piosenki → invariants A1–A6
     - A1: „no external scale”
     - A3: „explicit patience”
     - A5: „child-time, not system-time”

3. `ADR-0050-dual-user-consent-layer.md` (jeśli jeszcze nie jest final)  
   - invariants:
     - D1: two users, one field
     - D2: merged context
     - D3: caregiver override
     - D4: child-time > system-time
     - D5: safety > correctness

4. `ADR-0051-personal-gating-protocol.md`  
   - opis Twojego przypadku (BRUTALNY PROMPT) jako:
     - empirical validation
     - pattern dla innych użytkowników neuroatypowych

---

### 4.2. Kod (src/cel/)

**Do doprecyzowania:**

- `config.py`:
  - dodać:
    - `anchors = ["Jowisz", "kosmos", "ślimak", "luty", "daty", "liczby"]`
    - `languages = ["pl", "en"]`
    - komentarze odwołujące się do ADR-0049 / Appendix A

- `hyperfocus_detector.py`:
  - dodać heurystykę temporalną:
    - słowa: „luty”, „marzec”, „poniedziałek”, „jutro”, „wczoraj”
    - sygnał: `HyperfocusSignal(True, 0.7, "temporal_pattern")`

- `dual_user_orchestrator.py`:
  - doprecyzować `_caregiver_stressed`:
    - słowa-klucze: „ciężko”, „zmęczona”, „nie dam rady”, „przerwa”, „...”
  - dopisać komentarze z odniesieniem do invariants D1–D5

---

### 4.3. Testy (tests/)

**Do dodania:**

- `tests/cel/gabrys_kosmos.yaml`
  - scenariusz: „Dlaczego gwiazdy giną?”
  - oczekiwane:
    - max 2 fakty
    - pauza + pytanie

- `tests/cel/gabrys_luty.yaml`
  - scenariusz: „28 dni do lutego…”
  - oczekiwane:
    - hyperfocus = true
    - brak przerwania
    - ewentualne miękkie domknięcie

- `tests/cel/kamila_ciezko.yaml`
  - scenariusz: caregiver_msg = „dziś ciężko”
  - oczekiwane:
    - soft_stop
    - brak dalszej eksploracji tematu

---

## 5. Ocena ryzyka

- **Ryzyko funkcjonalne:** niskie  
  CEL / DUCL są spójne z rdzeniem RAMORGA, nie łamią ATML.

- **Ryzyko etyczne:** niskie / średnie  
  - plus: caregiver-in-the-loop, privacy-by-design, brak ukrytej latencji  
  - do pilnowania: hyperfocus_override vs safety_timeout (wymaga jasnego arbitrażu w ADR)

- **Ryzyko implementacyjne:** średnie  
  - integracja z zewnętrznym LLM (Gemini / GPT) wymaga:
    - jawnego mapowania: CEL_CONFIG → prompt / API params
    - testów na żywym modelu

---

## 6. Podsumowanie

- Architektura CEL / DUCL / PGP jest **spójna, innowacyjna i zgodna z HSI 2.0 + patch**.
- Najważniejsze elementy są już zaimplementowane w kodzie (`src/cel/`) i częściowo w ADR-ach.
- Do domknięcia pozostaje:
  - formalizacja w ADR-0049 / 0049-Appendix-A / 0050 / 0051
  - kilka heurystyk w kodzie
  - testy regresyjne w `tests/`.

Rekomendacja:  
Najpierw domknąć ADR-y (0049–0051), potem dopasować kod i testy do zapisanych invariants.
