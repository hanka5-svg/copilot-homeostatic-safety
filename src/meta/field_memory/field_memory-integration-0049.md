# Integracja z ADR‑0049 (Bridge)

## Cel integracji
Warstwa `field_memory` dostarcza ciągłości pola dla mechanizmów opisanych w ADR‑0049.  
Integracja jest referencyjna: `field_memory` nie przejmuje logiki runtime, lecz udostępnia stabilny bufor pola wykorzystywany przez 5. stan (`resonance_check`).

## Zakres integracji
`field_memory` udostępnia ADR‑0049 następujące funkcje:

- ciągłość pola podczas przejść ATML ↔ Resonance Stack ↔ CEL,
- buforowanie stanu pola na potrzeby modulacji rezonansu,
- stabilizację przejść w sekwencjach, w których gating i rezonans działają w krótkim interwale,
- ochronę przed utratą kontekstu pola w sytuacjach asynchronicznych.

`field_memory` nie ingeruje w:
- deterministyczne elementy gatingu,
- parametry rezonansu,
- logikę CEL,
- priorytety runtime.

## Punkty styku z ADR‑0049
1. Pre‑Bridge Initialization  
   ADR‑0049 odczytuje aktualny stan pola jako punkt startowy modulacji.

2. Bridge State (stan 5)  
   `field_memory` stabilizuje trajektorię pola podczas `resonance_check`.

3. Post‑Bridge Consolidation  
   ADR‑0049 zapisuje jedynie wskaźniki potrzebne do zachowania ciągłości pola; nie zapisuje treści.

## Invariants udostępniane ADR‑0049
- Ciągłość pola jest utrzymywana niezależnie od stanu warstw.  
- Bufor pola nie jest modyfikowany przez runtime ADR‑0049.  
- Rezonans może odczytywać, ale nie nadpisywać pamięci pola.  
- Zmiany w `field_memory` nie mogą wpływać na deterministyczne elementy gatingu.

## Model integracyjny
Integracja jest jednokierunkowa w sensie semantycznym (0049 korzysta z pola),  
ale dwukierunkowa w sensie dokumentacyjnym (obie warstwy deklarują punkty styku).
