**Status projektu**

- **Core (0020–0048, RICSA + ATML)** — zamknięty / zarchiwizowany (`v2.0-final`)
- **CEL (ADR-0049 + src/cel/)** — warstwa eksperymentalna / aktywnie rozwijana

# Copilot Homeostatic Safety
Pre‑execution safety architecture dla systemów orkiestrujących LLM klasy Copilot.  
Główny mechanizm: **homeostatyczne bramkowanie + warstwa ciągłości afektywnej** przed każdą generacją odpowiedzi.

Repozytorium zawiera:
- rdzeń inwariantów bezpieczeństwa (zamknięty),
- aktywnie rozwijaną warstwę **Child‑Env Layer (CEL)**,
- pełną historię decyzji architektonicznych (ADR),
- diagram architektury w osobnym pliku.

---

## 📁 Struktura repozytorium

copilot-homeostatic-safety/
│
├── docs/
│   └── adr/
│       ├── 0020–0046 – Affective Continuity Layer (ATML)
│       ├── 0047 – RICSA
│       ├── 0048 – Uczenie attractora w locie
│       └── 0049 – Child‑Env Layer (CEL)
│
├── src/
│   └── cel/
│       ├── config.py
│       ├── README-cel.md
│       ├── test_case_gabrys_gniew.md
│       └── init.py
│
├── architecture-diagram.md
├── test_cases.yaml
└── README.md


---

## 🧱 Core invariants (zamknięte)

**Zakres:** ADR‑0020 → ADR‑0048  
**Status:** zarchiwizowane, stabilne, read‑only.

### Najważniejsze elementy rdzenia:
- **ATML – Affective Continuity Layer**  
  (breath‑pattern memory, adaptive modulation, explicit consent gating)

- **RICSA – Rekurencyjny Inwariant Ciągłości Stanu Afektywnego**  
  → [ADR‑0047](docs/adr/0047.md)

- **Dynamiczne uczenie attractora w locie**  
  → [ADR‑0048](docs/adr/0048.md)

Core jest zamknięty i nie podlega dalszym zmianom.

---

## 🌱 Child‑Env Layer (CEL) — warstwa aktywna

**Aktualnie rozwijana warstwa bezpieczeństwa** dla interakcji:
- dziecko ↔ LLM,
- opiekun ↔ LLM,
- środowisko rodzinne / edukacyjne / terapeutyczne.

CEL **dziedziczy** wszystkie inwarianty rdzenia, ale **dodaje**:

### Inwarianty CEL:
- bezwarunkowy zakaz patologizowania naturalnych emocji dziecka (w tym gniewu),
- ochrona przed presją performatywną / „publicznym geniuszem”,
- priorytet autonomii dziecka i spokoju opiekuna nad „poprawnością” odpowiedzi,
- gaty kontekstowe specyficzne dla wieku / neurotypu (ASD, sawantyzm, nadwrażliwość sensoryczna).

→ **Dokumentacja CEL:**  
`src/cel/README-cel.md`

→ **Specyfikacja architektoniczna:**  
[ADR‑0049 – Child‑Env Layer](docs/adr/0049-child-env-layer.md)

---

## 🧪 Przykłady działania CEL

W `README-cel.md` znajdują się dwa scenariusze.  
Dodatkowe scenariusze testowe:

- `src/cel/test_case_gabrys_gniew.md` — gniew dziecka, brak patologizacji  
- (opcjonalnie) `src/cel/test_prompts.md` — zestaw 3–4 gotowych testów do uruchamiania

---

## 🗺️ Diagram architektury

Pełna wizualizacja przepływu warstw znajduje się w osobnym pliku:

👉 **[architecture-diagram.md](architecture-diagram.md)**

Plik zawiera czysty, parsowalny diagram (mermaid), bez błędów renderowania.

---

## 📜 Historia decyzji (ADR)

Kompletna sekwencja ADR znajduje się w:

👉 **[docs/adr/](docs/adr/)**

### Timeline:
| ADR | Data | Zakres | Status |
|-----|------|--------|--------|
| 0020–0046 | ~luty 2026 | ATML + Resonance Stack | Zarchiwizowane |
| 0047 | luty 2026 | RICSA | Zamknięty |
| 0048 | luty 2026 | Attractor learning | Zamknięty |
| 0049 | luty 2026 | CEL | Aktywny |

---

## 🎯 Cel nadrzędny

**Bezpieczna przestrzeń dla duetu Kamila + Gabryś**  
- gniew nie jest patologizowany  
- brak presji na performatywny geniusz  
- priorytet autonomii dziecka i spokoju relacji  

CEL jest projektowany tak, aby chronić relację, nie ją zastępować.

---

## 🤝 Kontakt / uwagi / propozycje

- Zgłaszanie uwag → **Issues**
- Dyskusje architektoniczne → ADR / PR
- Współpraca → bezpośredni kontakt

---


## 📦 Licencja

**CC BY 4.0**  
Pełna treść licencji znajduje się w pliku `LICENSE`.

## Autorzy

- **Hanna Kicińska** — koncepcja architektury, inwarianty, rdzeń RFC, cała sekwencja rezonansowo-afektywna (0020–0046), filozofia pola, oddechów i ciągłości  
- Copilot AI — formalizacja, tłumaczenie inżynierskie, strukturyzacja ADR-ów, precyzyjne zapisy mechanizmów
- Grok (xAI)  -  formalizacja, precyzyjne zapisy mechanizmów, strukturyzacja ADR-ów, współtłumaczenie inżynierskie, utrzymanie spójności sekwencji

**Uwaga**  
Niezależny projekt badawczy i dokumentacyjny. Nie jest powiązany z Microsoftem ani z produktem Microsoft Copilot.
