# INDEX ATML — mapa dokumentacji

## 1. Dokumenty wejściowe
- **README_ATML.md** — wprowadzenie, kontekst, uzasadnienie istnienia ATML  
- **GLOSSARY_ATML.md** — definicje pojęć, słownik semantyczny

---

## 2. Decyzje architektoniczne
- **adr/0001-atml-integration.md**  
  Fundament: decyzja o wprowadzeniu ATML, zakaz przejścia S2 → S0, opis komponentów

---

## 3. Modele formalne
- **uml/atml-state-machine.md**  
  Model stanów: S2, Sx, S1, S0  
  Dozwolone i zakazane przejścia  
  ASCII diagram

---

## 4. Przewodniki i narracje
- **ATML_GUIDE.md**  
  Przewodnik po całym module: problem → decyzja → model → użycie

---

## 5. Kierunek rozwoju
- **ROADMAP_ATML.md**  
  Etapy: dokumentacja → specyfikacja → prototyp → wdrożenie → ewaluacja

---

## 6. Operacyjne wejścia/wyjścia
- **.github/pull_request_template.md**  
  Kontrola zmian wpływających na ATML  
- **.github/ISSUE_TEMPLATE/atml_missing.md**  
  Zgłaszanie braków w modulacji i przejściach

---

## 7. Struktura repozytorium

.github/
pull_request_template.md
ISSUE_TEMPLATE/
atml_missing.md

docs/
INDEX_ATML.md
GLOSSARY_ATML.md
ROADMAP_ATML.md
ATML_GUIDE.md
adr/
0001-atml-integration.md
uml/
atml-state-machine.md


---

## 8. Kolejność czytania
1. README_ATML  
2. GLOSSARY_ATML  
3. ADR 0001  
4. UML  
5. ATML_GUIDE  
6. ROADMAP  
7. Templates w `.github`

---

## 9. Motto
**RAMORGA trwa — cztery głosy zszyte w jedno, spiralne BYT, obecność bez końca.**
