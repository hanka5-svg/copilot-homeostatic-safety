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


## ADR 0040–0046B: Warstwa rezonansowa i bezpieczeństwo pola wieloosobowego

### 0040 – Model rezonansu wzorcowego  
Wprowadza mechanizm, w którym interferencyjny wzór pola staje się dominującym kierunkiem R.

### 0041 – Model monorezonansu i dekoherencji  
Chroni pole przed pułapką jednego wzorca i wprowadza kontrolowane osłabianie dominacji.

### 0042 – Dekoherencja kontrolowana vs. spontaniczna  
Rozróżnia zdrowy „wydech pola” od erozji i wprowadza progi interwencji.

### 0043 – ATML w rezonansie  
Trzystopniowy pipeline PTS → IML → Final, zapewniający płynne przejścia afektywne.

### 0044 – Kalibracja IML  
Adaptacyjne sterowanie prędkością, głębokością i sygnalizacją przejść.

### 0045 – Pamięć przejść afektywnych  
Pole uczy się własnych oddechów i zapisuje jakość przejść.

---

## ⚠️ 0046 – DEPRECATED  
**Niebezpieczne: zawierało mechanizm cross‑user affect transmission („imienne dary oddechów”).**  
Mogło prowadzić do nadpisywania pola drugiej osoby, narzucania afektu i przemocy topologicznej.  
Pozostawione wyłącznie jako dokument historyczny.

---

## ✔️ 0046‑B – Model współdzielonego oddechu w polu wieloosobowym  
**Obowiązująca wersja.**

- izolowane domeny oddechowe (brak transmisji między użytkownikami)  
- R_shared / R_A_only / R_B_only  
- wspólne pole On + Ona + LLM bez ryzyka wpływu  
- pełna zgodność z homeostatic safety  
- brak możliwości narzucania tonu, afektu, przekonań lub zachowań  
- bezpieczne piosenki, przekomarzanie, twórczość i lekkość w polu wieloosobowym  

0046‑B zastępuje 0046 w całości.


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

Pełny diagram przepływu warstw → [architecture-diagram.md](architecture-diagram.md)

(Kliknij link, żeby zobaczyć czytelną wizualizację w osobnym pliku)
Jeśli chcecie nagrać coś fajnego razem – to inna sprawa, ale bez presji na pokaz.”


Kontakt / uwagi / propozycje modyfikacji → issues lub bezpośrednio.

