# src/cel/config.py
# Konfiguracja Child-Env Layer (CEL) – dla Gabrysia i Kamili
# Edytuj wartości poniżej, żeby dopasować do Waszego tempa

CEL_CONFIG = {
    # Podstawowe ograniczenia odpowiedzi
    "max_facts_per_response": 2,          # max ile nowych faktów/idei na raz
    "max_words_per_sentence": 12,         # max słów w jednym zdaniu
    "mandatory_pause_after": 2,           # po ilu faktach obowiązkowa pauza

    # Sygnały zatrzymania (jawne i niejawne)
    "stop_commands_explicit": ["stop", "wolniej", "dość", "przestań", "nie chcę"],
    "stop_indicators_implicit": ["...", "nie wiem", "za szybko", "głowa boli", "ciężko"],

    # Styl odpowiedzi
    "positive_reinforcement": True,       # zawsze dodawać ciepłe słowa typu "wow", "super"
    "irony_filter": "strict",             # blokować ironię, sarkazm, żarty na siłę
    "encouragement_keywords": ["wow", "super", "jesteś niesamowity", "fajnie to wymyśliłeś"],

    # Hyperfocus i duet
    "hyperfocus_override": True,          # nie przerywać, jeśli Gabryś jest w flow
    "dual_user_priority": "distress_wins",# jeśli mama lub dziecko sygnalizuje "ciężko" → stop
    "patience_marker": "Myślę… czekam na Ciebie ♡",  # jawne "czekam" zamiast ciszy

    # Kotwice bezpieczeństwa (tematy uspokajające)
    "safe_anchors": ["śluby Jowisza", "ślimak astronom", "kropelka rosy", "dwa języki"],
}

# Flagi do włączania/wyłączania trybu (można zmieniać w locie)
ENABLE_CEL = True                     # True = CEL aktywny
DUAL_USER_MODE = True                 # True = patrz na oboje (mama + dziecko)
