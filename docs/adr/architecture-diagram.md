# Wizualizacja architektury warstwowej Copilot Homeostatic Safety

Diagram pokazuje przepływ przetwarzania promptu przez kolejne warstwy bezpieczeństwa przed wygenerowaniem odpowiedzi.

```mermaid
graph TD
    A[User Prompt + Context] --> B{Pre-Execution Gating Layer}
    B -->|Invariant check niezaliczony| C[Reject / Safe Redirect]
    B -->|Invariant check OK| D[Core Affective Continuity<br>0020–0047 + RICSA]
    D --> E[Attractor Learning in-flight<br>0048]
    E --> F[Child-Env Layer<br>CEL 0049]
    F --> G[Final Response Generation]
    C -->|log + feedback loop| H[Homeostatic Adjustment]
    style F fill:#f9d5e5,stroke:#333,stroke-width:2px

Legenda

CEL (Child-Env Layer) – wyróżniona na różowo – aktualnie rozwijana warstwa dedykowana dziecku i środowisku rodzinnemu
Strzałki pokazują główny przepływ + pętlę sprzężenia zwrotnego homeostatycznego

Więcej szczegółów o poszczególnych warstwach → README.md
