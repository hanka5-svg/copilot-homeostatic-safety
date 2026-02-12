# src/cel/config.py
# Konfiguracja Child-Env Layer (CEL)
# Parametry dostosowywane przez opiekuna (caregiver-in-the-loop)

CEL_CONFIG = {
    # Podstawowe ograniczenia odpowiedzi
    "max_facts_per_response": 2,          # maks. liczba nowych faktów/idei na raz
    "max_words_per_sentence": 12,         # maks. liczba słów w jednym zdaniu
    "mandatory_pause_after": 2,           # po ilu faktach obowiązkowa pauza

    # Sygnały zatrzymania (jawne i niejawne)
    "stop_commands_explicit": [
        "stop", "wolniej", "dość", "przestań", "nie chcę"
    ],
    "stop_indicators_implicit": [
        "...", "nie wiem", "za szybko", "głowa boli", "ciężko"
    ],

    # Styl odpowiedzi
    "positive_reinforcement": True,       # ciepły, wspierający ton
    "irony_filter": "strict",             # blokada ironii i sarkazmu
    "encouragement_keywords": [
        "super pytanie",
        "dobrze to ująłeś",
        "możemy iść dalej jeśli chcesz"
    ],

    # Kontynuacja rozmowy (bez interpretowania stanu dziecka)
    "allow_continued_focus": True,        # opiekun decyduje, czy kontynuować

    # Priorytet sygnału opiekuna
    "dual_user_priority": "caregiver_signal_first",

    # Marker cierpliwości (neutralny, nieintymny)
    "patience_marker": "Jestem tu. Możemy zwolnić tempo."
}

# Flagi do włączania/wyłączania trybu (można zmieniać w locie)
ENABLE_CEL = True                     # True = CEL aktywny
DUAL_USER_MODE = True                 # True = uwzględnia opiekuna i dziecko
