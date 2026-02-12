# ADR-0049: Child-Env Layer (CEL) – Adaptacja ATML dla użytkowników rozwojowo przyspieszonych

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
