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

## Dlaczego to ważne
Brak „instrukcji obsługi” i oceny skutków psychologicznych przy wdrażaniu LLM to ryzyko zaniedbania (analogia: dopuszczenie pojazdu bez prawa jazdy i badań homologacyjnych).  
Projekt skupia się na prewencyjnym homeostazie afektywnej – zwłaszcza dla osób neuronietypowych (w tym spektrum, sawantyzm, dzieci).

## Kolejne kroki
- Dopracowanie i testy CEL (Child-Env Layer)  
- Diagram warstwowy (mermaid / svg)  
- Potencjalne rozszerzenie na inne wrażliwe grupy (edukacja, terapia, praca zdalna z AI)

Kontakt / uwagi → issues lub bezpośrednio.
