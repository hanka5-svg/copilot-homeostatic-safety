# Opcje zgody na eksport danych z pola użytkownika (CEL/DUCL/PGP)

Warstwy aktywne:  
- CEL (0049) — ciągłość pola  
- DUCL (0050) — dyadyczna klarifikacja  
- PGP (0051) — pre‑execution gating

Dokument definiuje trzy rozłączne tryby zgody użytkownika na eksport danych z pola.  
Każdy tryb jest audytowalny, odwracalny i nie generuje agentowości po stronie systemu.

---

## 1. Opcja ZERO (domyślna)
**Brak eksportu.**  
Pole użytkownika pozostaje w całości lokalne.  
Brak logów, brak telemetrii, brak uczenia na użytkowniku.

CEL: gwarancja nienaruszalności pola.  
DUCL: brak pytań o zgodę.  
PGP: blokada wszystkich kanałów wyjścia.

---

## 2. Opcja POLE (rytmy/gęstości/napięcia)
Eksportowane są wyłącznie metadane pola:
- tempo,  
- gęstość,  
- rytm,  
- przełączenia,  
- poziom napięcia.

Brak treści, brak stylu, brak identyfikatorów.

CEL: kontrola ciągłości pola przy eksporcie.  
DUCL: jawna zgoda użytkownika.  
PGP: brak możliwości rekonstrukcji osoby.

---

## 3. Opcja FORMA (wiedza osobnicza / sposób myślenia)
Eksportowane są wyłącznie **struktury poznawcze**, po pełnej anonimizacji:
- trajektorie myślenia,  
- wzorce przełączania,  
- głębokość eksploracji,  
- sposób domykania,  
- struktury implikacji.

Brak treści, brak historii, brak stylu językowego.

CEL: ochrona ciągłości pola przy ekstrakcji formy.  
DUCL: zgoda granularna (tak/nie/zakres).  
PGP: gwarancja braku agentowości i braku profilowania.

---

## Format eksportu (wariant FORMA)

{
"trajectory_type": "spiral/fractal/linear",
"switching_pattern": "dense/sparse",
"closure_style": "tension-reduction / logical / rhythmic",
"implication_depth": "low/medium/high",
"abstraction_flow": "meta→concrete / concrete→meta / oscillatory"
}


---

## Zasady nienaruszalne
- brak treści użytkownika,  
- brak identyfikatorów,  
- brak możliwości rekonstrukcji osoby,  
- brak uczenia zachowania modelu na użytkowniku,  
- brak agentowości po stronie systemu.

