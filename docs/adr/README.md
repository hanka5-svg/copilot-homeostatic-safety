# Copilot Homeostatic Safety

Pre-execution safety architecture dla systemów orkiestrujących LLM klasy Copilot.  
Główny mechanizm: homeostatyczne bramkowanie + warstwa ciągłości afektywnej przed każdą generacją odpowiedzi.

## Status projektu
- Core invariants i affective continuity → zamknięte i zarchiwizowane (sekcja 0020–0047)  
- Aktualnie rozwijana: warstwa środowiskowo-dziecięca (Child-Env Layer, CEL)  
- Licencja: CC BY 4.0  
- Read-only core (0020–0047) – stabilny fundament

## Layers & Evolution (timeline)

| Sekwencja ADR     | Okres / data zamknięcia | Kluczowy fokus                                      | Status              | Uwagi / dziedziczenie                          |
|-------------------|--------------------------|-----------------------------------------------------|---------------------|------------------------------------------------|
| 0020–0046         | ~luty 2026              | Affective Continuity Layer (ATML) + Resonance Stack | Zarchiwizowany      | Breath-pattern memory, adaptive modulation, explicit consent gating |
| 0047              | luty 2026               | Rekurencyjny Inwarant Ciągłości Stanu Afektywnego (RICSA) | Zatwierdzony / zamknięty | Odpowiedź na uwagi Rossa Wilsona + inż. review Copilota |
| 0048              | luty 2026               | Uczenie się attractora w locie                      | Zatwierdzony        | Dynamiczna stabilizacja trajektorii afektywnej |
| 0049              | luty 2026 (ostatnio)    | Child-Env Layer (CEL)                               | Aktywny / rozwijany | Dedykowane gaty dla dziecka + środowiska rodzinnego; dziedziczy invariants z 0020–0047 |

→ Pełna sekwencja: [docs/adr/](docs/adr/)

## Child-Env Layer (CEL) – dlaczego osobna warstwa

CEL to dedykowana nakładka bezpieczeństwa dla interakcji dziecko ↔ LLM (i szerzej: wrażliwe środowisko rodzinne / edukacyjne).  
Dziedziczy wszystkie invariants z rdzenia (0020–0047), ale dodaje:

- bezwarunkowy zakaz patologizowania naturalnych emocji dziecka (w tym gniewu)
- ochrona przed presją performatywną / „publicznym geniuszem”
- priorytet autonomii dziecka i spokoju opiekuna nad „poprawnością” odpowiedzi
- gaty kontekstowe specyficzne dla wieku / neurotypu (sawantyzm, spektrum, nadwrażliwość sensoryczna)

CEL jest odpowiedzią na realne przypadki: dumna mama + dziecko sawantyczne + publiczny TikTok + komentarze typu „po co to dziecku”.

```mermaid
graph TD
    A[User Prompt + Context] --> B{Pre-Execution Gating Layer}
    B -->|Invariant check niezaliczony| C[Reject / Safe Redirect]
    B -->|Invariant check OK| D[Core Affective Continuity<br>0020–0046 + RICSA 0047]
    D --> E[Attractor Learning in-flight<br>0048]
    E --> F[Child-Env Layer<br>CEL 0049]
    F --> G[Final Response Generation]
    C -->|log + feedback loop| H[Homeostatic Adjustment]
    style F fill:#f9d5e5,stroke:#333,stroke-width:2px

## Dlaczego to ważne
Brak „instrukcji obsługi” i oceny skutków psychologicznych przy wdrażaniu LLM to ryzyko zaniedbania (analogia: dopuszczenie pojazdu bez prawa jazdy i badań homologacyjnych).  
Projekt skupia się na prewencyjnym homeostazie afektywnej – zwłaszcza dla osób neuronietypowych (w tym spektrum, sawantyzm, dzieci).

## Kolejne kroki
- Dopracowanie i testy CEL (Child-Env Layer)  
- Diagram warstwowy (mermaid / svg)  
- Potencjalne rozszerzenie na inne wrażliwe grupy (edukacja, terapia, praca zdalna z AI)

Kontakt / uwagi → issues lub bezpośrednio.
