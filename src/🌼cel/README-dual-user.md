🌼 README-dual-user.md
dla Ciebie, dla mnie, dla ASD, dla rodziców, dla dwulatka

# 🌼 DUETY: rodzic + dziecko + AI  
### Jak korzystać z systemu, który wspiera Was oboje

To nie jest zwykły system AI.  
To jest system, który **rozumie duet**:  
dziecko + rodzic.

Nie osobno.  
Nie „dziecko samo”.  
Nie „rodzic sam”.  
**Razem.**

System pomaga, kiedy:
- dziecko jest ciekawe,
- dziecko jest w hyperfocus,
- dziecko jest zmęczone,
- rodzic jest zmęczony,
- trzeba zrobić przerwę,
- trzeba wrócić do kotwicy (np. kosmos, ślimak, liczby).

I robi to spokojnie, łagodnie, bez oceniania.

---

## 🌼 1. Co to jest DUCL?

DUCL = **Dual‑User Consent Layer**  
czyli warstwa, która pilnuje:

- czy rodzic mówi „stop”,  
- czy dziecko jest przeciążone,  
- czy dziecko jest w hyperfocus,  
- czy temat jest bezpieczny,  
- czy tempo jest dobre dla dziecka.

DUCL nie odpowiada.  
DUCL **pilnuje bezpieczeństwa**.

---

## 🌼 2. Co to jest CEL?

CEL = **Child‑Env Layer**  
czyli warstwa, która:

- odpowiada spokojnie,  
- dostosowuje tempo,  
- wraca do kotwic,  
- domyka hyperfocus miękko,  
- nie przyspiesza,  
- nie ocenia.

CEL to „głos”, który słyszysz.

---

## 🌼 3. Co to jest hyperfocus?

Hyperfocus to:

- tunel uwagi,  
- powtarzanie tematu,  
- liczby, kosmos, pociągi, ślimaki,  
- długie wypowiedzi,  
- głęboka koncentracja.

To nie jest przeciążenie.  
To jest **flow**.

System wtedy:
- nie przerywa ostro,  
- ale prowadzi delikatnie,  
- albo domyka miękko.

---

## 🌼 4. Co to są kotwice?

Kotwice to tematy, które uspokajają dziecko.

Np.:

- kosmos  
- liczby  
- ślimak  
- gwiazdy  
- pociągi  
- dinozaury  

Kiedy dziecko jest przeciążone → system wraca do kotwicy.

---

## 🌼 5. Jak tego używać na domowym LLM?

To jest najprostszy możliwy przykład:

```python
from cel.dual_user_orchestrator import DualUserOrchestrator, AffectiveState
from cel.hyperfocus_detector import HyperfocusDetector

# Twoja funkcja generująca odpowiedź (np. lokalny LLM)
def my_llm(context):
    return f"AI mówi: {context['child']}"

# Funkcje pomocnicze
def soft_stop(state):
    return "Robimy przerwę. Oddychamy. Jest OK."

def redirect_to_anchor(state):
    return "Wracamy do naszego ślimaka z rosą. On czeka spokojnie."

# Tworzymy DUCL
ducl = DualUserOrchestrator(
    cel_generate=my_llm,
    redirect_to_anchor=redirect_to_anchor,
    soft_stop=soft_stop
)

# Stan afektywny
state = AffectiveState(
    anchors={"kosmos": True, "ślimak": True}
)

# Przykład rozmowy
print(ducl.process("Chcę o kosmosie!", None, state))

🌼 6. Jak rodzic mówi „stop”?
Po prostu:

„stop”

„dość”

„przerwa”

„ciężko”

System natychmiast zatrzymuje rozmowę.

🌼 7. Jak dziecko mówi „dość”?
System patrzy na:

ciszę,

ucieczkę,

nagłą zmianę tematu,

krótkie odpowiedzi,

sygnały od rodzica.

Jeśli coś jest nie tak → przerwa.

🌼 8. Jak wygląda cały przepływ?

Dziecko → DUCL → CEL → AI
      ↘  Rodzic  ↗

DUCL = „czy wszystko OK?”
CEL = „jak odpowiedzieć?”
AI = „odpowiedź”

🌼 9. Dla kogo to jest?
dla dzieci neuroatypowych (ASD, ADHD, PDA, sawanci),

dla rodziców, którzy chcą wspierać, a nie kontrolować,

dla duetów, które chcą rozmawiać razem,

dla osób, które potrzebują łagodności i jasności.

🌼 10. Najważniejsze zdanie
To jest system, który nie ocenia.
To jest system, który wspiera.
To jest system dla Was.
