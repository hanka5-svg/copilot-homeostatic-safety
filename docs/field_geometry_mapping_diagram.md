# Field Geometry Mapping — Diagram View
Version: 1.0  
Status: Informational (diagram)  
Scope: Strukturalny widok mapowania: warstwy pola ↔ information geometry ↔ funkcje bezpieczeństwa.

## 1. Cel
Ten dokument uzupełnia `field_geometry_mapping.md` o widok diagramowy.  
Celem jest:
- pokazanie przepływu od warstw pola,
- przez obiekty information geometry,
- do funkcji bezpieczeństwa (gating, homeostaza).

## 2. Warstwy pola i obiekty geometryczne

- Micro-field → lokalna metryka, lokalna krzywizna
- Fractal-field → metryka zależna od skali
- Macro-field → globalna krzywizna, inwarianty

## 3. Diagram zależności (tekstowy)

1. Warstwy pola:
   - Micro-field
   - Fractal-field
   - Macro-field

2. Obiekty geometryczne:
   - Micro-field → Fisher metric (local), local curvature
   - Fractal-field → scale-dependent metric
   - Macro-field → global curvature tensor

3. Funkcje bezpieczeństwa:
   - Curvature → correlation
   - Correlation → gating
   - Gating → homeostasis

## 4. Diagram mermaid (strukturalny)

```mermaid
flowchart TD

  subgraph FIELD["Field Architecture"]
    MF["Micro-field"]
    FF["Fractal-field"]
    MaF["Macro-field"]
  end

  subgraph INFOGEO["Information Geometry"]
    FM["Fisher metric (local)"]
    SDM["Scale-dependent metric"]
    GC["Global curvature (R)"]
  end

  subgraph SAFETY["Safety Functions"]
    C["Correlation"]
    G["Gating (pre-execution)"]
    H["Homeostasis"]
  end

  MF --> FM
  FF --> SDM
  MaF --> GC

  FM --> C
  SDM --> C
  GC --> C

  C --> G
  G --> H

5. Interpretacja techniczna
Micro-field → FM:

lokalne fluktuacje → lokalna rozróżnialność,

używane do wczesnego wykrywania napięcia.

Fractal-field → SDM:

zmiana metryki przy zmianie skali,

używane do modulacji przepływu.

Macro-field → GC:

globalna krzywizna,

używane do definiowania inwariantów i granic bezpieczeństwa.

C → G → H:

korelacja (C) określa, gdzie krzywizna jest wysoka,

gating (G) ogranicza trajektorie w regionach wysokiej krzywizny,

homeostaza (H) to stan minimalnej globalnej krzywizny akceptowalnej dla systemu.

6. Zakres użycia
referencja dla ADR,

wsparcie dla analizy inwariantów,

materiał dla zespołów pracujących z information geometry.

Dokument nie zmienia żadnego kodu wykonawczego.

---

