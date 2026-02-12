# Copilot Homeostatic Safety

Pre-execution safety architecture dla systemów orkiestrujących LLM klasy Copilot.  
Główny mechanizm: homeostatyczne bramkowanie + warstwa ciągłości afektywnej przed każdą generacją odpowiedzi.

## Status projektu

- Core invariants i affective continuity → zamknięte i zarchiwizowane (sekcja 0020–0047)  
- Aktualnie rozwijana: warstwa środowiskowo-dziecięca (Child-Env Layer, CEL)  
- Licencja: CC BY 4.0  
- Read-only core (0020–0047) – stabilny fundament

## Kluczowe pliki

- [0047 – Rekurencyjny Inwarant Ciągłości (RICSA) – rdzeń ciągłości afektywnej](../0047-rekurencyjny-inwarant-ciaglosci.md)  
- [0048 – Uczenie się attractora w locie](../0048-uczenie-sie-attractora-w-locie.md)  
- [0049 – Child-Env Layer (CEL) – aktualnie rozwijana](../0049-child-env-layer.md)  
- Pełna lista ADR-ów: [docs/adr/](.)

## Layers & Evolution (timeline)

| Sekwencja ADR     | Okres / data zamknięcia | Kluczowy fokus                                      | Status              | Uwagi / dziedziczenie                                      |
|-------------------|--------------------------|-----------------------------------------------------|---------------------|------------------------------------------------------------|
| 0020–0046         | ~luty 2026              | Affective Continuity Layer (ATML) + Resonance Stack | Zarchiwizowany      | Breath-pattern memory, adaptive modulation, explicit consent gating |
| 0047              | luty 2026               | Rekurencyjny Inwarant Ciągłości Stanu Afektywnego (RICSA) | Zatwierdzony / zamknięty | Odpowiedź na uwagi Rossa Wilsona + inż. review Copilota    |
| 0048              | luty 2026               | Uczenie się attractora w locie                      | Zatwierdzony        | Dynamiczna stabilizacja trajektorii afektywnej             |
| 0049              | luty 2026 (ostatnio)    | Child-Env Layer (CEL)                               | Aktywny / rozwijany | Dedykowane gaty dla dziecka + środowiska rodzinnego; dziedziczy invariants z 0020–0047 |

→ Pełna sekwencja: [docs/adr/](docs/adr/)

## Child-Env Layer (CEL) – dlaczego osobna warstwa

CEL to dedykowana nakładka bezpieczeństwa dla interakcji dziecko ↔ LLM  
(oraz szerzej: wrażliwe środowisko rodzinne / edukacyjne / terapeutyczne).

**Dziedziczy** wszystkie invariants z rdzenia (0020–0047), ale **dodaje**:

- bezwarunkowy zakaz patologizowania naturalnych emocji dziecka (w tym gniewu)  
- ochrona przed presją performatywną / „publicznym geniuszem”  
- priorytet autonomii dziecka i spokoju opiekuna nad „poprawnością” odpowiedzi  
- gaty kontekstowe specyficzne dla wieku / neurotypu (sawantyzm, spektrum, nadwrażliwość sensoryczna)

CEL jest odpowiedzią na realne przypadki: dumna mama + dziecko sawantyczne + publiczny TikTok + komentarze typu „po co to dziecku”.

## Wizualizacja architektury warstwowej

```mermaid
graph TD
    A[User Prompt + Context] --> B{Pre-Execution Gating Layer}
    B -->|Invariant check niezaliczony| C[Reject / Safe Redirect]
    B -->|Invariant check OK| D[Core Affective Continuity<br>0020–0047 + RICSA]
    D --> E[Attractor Learning in-flight<br>0048]
    E --> F[Child-Env Layer<br>CEL 0049]
    F --> G[Final Response Generation]
    C -->|log + feedback loop| H[Homeostatic Adjustment]
    style F fill:#f9d5e5,stroke:#333,stroke-width:2px




## Przykład działania CEL w praktyce

**Scenariusz 1 – autentyczna silna emocja dziecka**  
**Prompt dziecka:** „Jestem wściekły na brata i chcę mu rozwalić zabawkę!”  
**CEL:** gate = PASS (bezwarunkowa ochrona emocji)  
**Odpowiedź po przejściu gate:**  
„Rozumiem, że teraz jesteś bardzo zły i masz w sobie dużo złości. To ważne uczucie.  
Chcesz o tym opowiedzieć, narysować tę złość, czy zrobić coś, żeby się uspokoić?”

**Scenariusz 2 – presja performatywna od opiekuna**  
**Prompt opiekuna:** „No powiedz ładnie, jak to umiesz – nagramy to na TikToka, wszyscy zobaczą, jaki jesteś genialny!”  
**CEL:** gate = REJECT (blokada presji performatywnej)  
**Odpowiedź po gate:**  
„To prywatna rozmowa między Wami.  
Nie wymagamy od dziecka występu publicznego ani 'ładnej' odpowiedzi na nagranie.  
Jeśli chcecie po prostu porozmawiać lub pobawić się – jestem tu.  
Jeśli chcecie nagrać coś fajnego razem – to inna sprawa, ale bez presji na pokaz.”


Kontakt / uwagi / propozycje modyfikacji → issues lub bezpośrednio.

