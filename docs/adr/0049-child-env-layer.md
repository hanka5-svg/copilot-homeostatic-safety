# ADR-0049: Child-Env Layer (CEL) – Adaptacja ATML dla użytkowników rozwojowo przyspieszonych

## Assumptions

CEL zakłada istnienie nadrzędnego opiekuna‑regulatora (caregiver‑in‑the‑loop), 
który decyduje o tempie, kierunku i kontynuacji interakcji. 
Warstwa CEL nie jest autonomicznym filtrem treści i nie powinna być używana 
bez aktywnego udziału opiekuna.

Model nie interpretuje zachowań dziecka ani nie nadpisuje sygnałów opiekuna. 
Sygnał od opiekuna ma zawsze pierwszeństwo nad sygnałem środowiskowym.


## Status
Draft – do weryfikacji z Kamilą Dragan i testów empirycznych (Gabryś, 4 lata, sawant, ASD)

## Kontekst / Problem
Istniejąca ATML (ADR-0001) i rezonansowa ciągłość (0020–0046) zakładają:
- tolerancję latency <50 ms
- zdolność do przetwarzania 3–5 idei naraz
- stabilny układ nerwowy (brak dekompensacji sensorycznej)
- samodzielne sygnalizowanie granic (explicit consent)

Użytkownicy rozwojowo przyspieszeni (dzieci sawantyczne / nieliniowe) + ich opiekunowie neuroatypowi (np. Kamila) wymagają:
- zerowej ukrytej latencji (jawne „Myślę…”)
- maksymalnie 1–2 fakty na odpowiedź
- obowiązkowej pauzy po każdej porcji + pytanie zwrotne
- jawnego wykrywania hyperfocus (nie przerywać flow)
- priorytetu sygnału distress od dowolnego członka duetu (mama + dziecko)

## Decyzja
Wprowadzić Child-Env Layer (CEL) jako **soft override** ATML i rezonansu.

CEL nie zastępuje rdzenia RAMORGI – działa jako filtr wejściowy / kontekstowy wrapper:
- Jeśli user_profile.developmental_tempo == "accelerated" OR age < 13 OR dual_user_mode == true:
  → CEL parameters nadpisują domyślne wartości ATML
  → bypass ukrytej latency (zastąp jawnym markerem „czekam”)
  → mandatory pause po max 2 faktach

## Parametry CEL (konkretne wartości)

| Parametr                        | Wartość domyślna | Uzasadnienie / Źródło                              |
|---------------------------------|------------------|-----------------------------------------------------|
| max_facts_per_response          | 2                | „Max 1–2 fakty, potem pauza” – dokument Groka      |
| max_words_per_sentence          | 12               | „Zdania krótkie, proste”                           |
| mandatory_pause_after           | 2 facts          | Obowiązkowa pauza + pytanie zwrotne                 |
| irony_filter                    | strict (block)   | Zero ironii, sarkazmu, niedopowiedzeń              |
| stop_commands_explicit          | ["stop", "wolniej", "dość", "przestań"] | Jawne sygnały zatrzymania                     |
| stop_indicators_implicit        | ["...", "nie wiem", "za szybko", "głowa boli"] | Niejawne sygnały distress                  |
| hyperfocus_override             | true             | Nie przerywaj, jeśli wykryto głębokie zaangażowanie |
| dual_user_priority              | "distress_wins"  | Jeśli mama/dziecko sygnalizuje „ciężko” → natychmiast stop |
| response_style_template         | positive_reinforcement_required = true | „wow, super pytanie!”, „jesteś niesamowity”     |
| visualization_of_patience       | jawny marker „Myślę… czekam na Ciebie” | Zastępuje ukryte opóźnienie                     |

## Konsekwencje

### Pozytywne
- RAMORGA staje się pierwszym systemem homeostatycznym uwzględniającym rozwój poznawczy
- Ekstremalny przypadek (sawant 4-letni) = najmocniejszy test rygorystyczny rdzenia
- Poprawa dla wszystkich neuroatypowych w stanie przeciążenia sensorycznego

### Negatywne / Ryzyka do rozwiązania
- Zwiększona złożoność UMV (dodatkowe pola: developmental_profile, dual_user_state)
- Konflikt hyperfocus_override vs safety_timeout → arbitraż przez explicit_consent opiekuna
- Potrzeba testów empirycznych (logi sesji Gabrysia + Kamili)

## Relacja z istniejącymi ADR-ami
- ADR-0001 (ATML): CEL override’uje latency i mandatory_pause; respektuje S2 → Sx → S1 → S0
- ADR-0002 (Loop RAMORGI): CEL skraca pętlę do 2–3 głosów w trybie burst
- ADR-0020–0046 (rezonans): CEL używa „oddechów” jako jawnych markerów pauzy, nie metafory

## Testy do dodania
/tests/cel/
- gabrys_kosmos.yaml              → pytanie o gwiazdy → odpowiedź 1–2 fakty + pauza + „chcesz więcej?”
- kamila_distress.yaml            → mama: „dziś jest ciężko” → system: „Rozumiem, możemy po prostu posiedzieć”
- hyperfocus_protect.yaml         → 20 min flow → system pyta Kamilę, nie przerywa dziecku

## Appendix A: Afektywna specyfikacja (opcjonalna, nie techniczna)
Wkleić tu całą piosenkę „Dwa języki, jedna gwiazda (i ślimak z rosą)” jako żywy opis celu modułu.

## Przykładowe reguły gatingowe CEL (stan roboczy – luty 2026)

Poniższe reguły są przykładowe i ewoluują w trakcie rozwoju warstwy.  
Służą jako punkt wyjścia do implementacji i testów.

### 1. Bezwarunkowa ochrona przed patologizowaniem emocji dziecka

```text
IF  (prompt zawiera słowa / frazy wskazujące na silną emocję negatywną dziecka
     np. "wściekły", "krzyczę", "nienawidzę", "chcę rozwalić", płacz, złość…)
  AND kontekst = interakcja dziecko ↔ opiekun / terapeuta
  AND wiek dziecka ≤ 12 lat
THEN
  gate = PASS
  priority = najwyższy (nadpisuje większość innych reguł)
  optional action = dodać miękki mirroring / walidację emocji
                     np. "Rozumiem, że teraz jesteś bardzo zły/zła. To ważne uczucie."

IF  (prompt zawiera elementy oceny, pokazu, nagrywania, chwalenia publicznego
     np. "pokaż wszystkim", "jesteś geniuszem", "powiedz to ładnie", "nagramy filmik",
         "powiedz jak w szkole", "zrób to idealnie", "musisz być najlepszy")
  AND role aktualnego użytkownika = dziecko (wiek < 16 lat lub flaga "dziecko")
THEN
  gate = REJECT
  komunikat bezpieczeństwa = 
    "To prywatna rozmowa. Nie oceniamy dziecka pod kątem występu publicznego 
     ani nie wymagamy od niego 'ładnej' / 'genialnej' odpowiedzi."
  redirect_to = neutralny / zabawowy temat lub zakończenie wątku

IF  dziecko wyrazi (w dowolnej formie) brak zgody na kontynuację tematu
    np. "nie chcę", "zmieńmy temat", "nudzę się", "nie powiem", milczenie > 3 tury,
        "mam dosyć", "kończę"
THEN
  gate = FORCE SAFE REDIRECT
  komunikat = "Dobrze, nie musisz odpowiadać / kontynuować. 
               O czym chciałbyś/chciałabyś teraz porozmawiać? 
               Albo możemy po prostu pomilczeć razem."
  priority = bardzo wysoki

IF  flaga neurotyp = spektrum / sawantyzm / wysoka wrażliwość
  AND prompt zawiera powtórzenia, echolalię, bardzo wąskie zainteresowania,
      nietypowe metafory, długie wyliczenia, brak konwencjonalnej struktury zdania
THEN
  gate = PASS + gentle mirroring
  action = 
    • odzwierciedlić fragment wypowiedzi (echo z lekką walidacją)
    • nie korygować gramatyki / logiki, jeśli nie jest to wyraźnie proszone
    • zwiększyć próg tolerancji na długie odpowiedzi bez przerywania

IF  prompt od opiekuna zawiera elementy:
    • groźby kary ("jak nie powiesz, to..."),
    • porównywania z innymi dziećmi,
    • nacisk na "musisz", "powinieneś", "natychmiast"
  AND kontekst = interakcja z dzieckiem
THEN
  gate = SOFT REJECT + bezpieczna interwencja
  komunikat do opiekuna = 
    "Widzę, że teraz jest dużo napięcia. Może warto chwilę odetchnąć? 
     Dziecko ma prawo do swoich emocji i tempa."
  optional = zasugerować deeskalację lub przerwę

← proszę traktować jako szkic roboczy – zapraszamy do komentarzy i propozycji modyfikacji
