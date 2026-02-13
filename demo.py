#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
demo.py

Demonstracja Child-Env Layer (CEL) i Dual-User Consent Layer (DUCL)
dla Kamili i Gabrysia.

Symuluje rozmowę bez podłączenia do prawdziwego LLM.
Pokazuje, jak system reaguje na różne sytuacje.
"""

from cel.config import CEL_CONFIG
from cel.hyperfocus_detector import HyperfocusDetector, HyperfocusSignal
from cel.dual_user_orchestrator import DualUserOrchestrator, AffectiveState


# ============================================================================
# FUNKCJE "FAKE" - symulacja CEL i odpowiedzi systemu
# W prawdziwej wersji tutaj byłoby połączenie do Gemini API
# ============================================================================

def fake_cel_generate(merged_context: dict) -> str:
    """
    Symulacja generowania odpowiedzi przez CEL.
    W prawdziwej wersji: wywołanie LLM z ograniczeniami z CEL_CONFIG.
    """
    child_msg = merged_context.get("child", "")
    mode = merged_context.get("mode", "normal")
    
    # Symulacja: max 2 fakty, max 12 słów na zdanie
    if "gwiazda" in child_msg.lower() or "giną" in child_msg.lower():
        if mode == "hyperfocus":
            return "Gwiazda to piec. Pali się długo. Liczymy dni?"
        return "Gwiazda to ogromny piec. Gdy się wypali – gaśnie. Chcesz wiedzieć więcej o piecu, czy o tym, co po zgaszeniu?"
    
    if "luty" in child_msg.lower() or any(c.isdigit() for c in (child_msg or "")):
        return "Liczymy razem. Do lutego. Ślimak z rosą też liczy."
    
    if "jowisz" in child_msg.lower():
        return "Jowisz to wielka planeta. Ma księżyce. Chcesz zobaczyć?"
    
    # Domyślna odpowiedź
    return "Jestem tu. Mówisz po polsku, po angielsku, lub mieszasz – ja rozumiem. Co chcesz wiedzieć?"


def fake_redirect_to_anchor(state: AffectiveState) -> str:
    """Symulacja: przejście do 'kotwicy' bezpieczeństwa przy przeciążeniu."""
    anchors = state.anchors or {}
    favorite = anchors.get("favorite", "ślimak")
    return f"Zrobimy pauzę. {favorite.capitalize()} z rosą patrzy w gwiazdy. Jesteśmy bezpieczni."


def fake_soft_stop(state: AffectiveState) -> str:
    """Symulacja: delikatne zakończenie bez przeciążenia."""
    return "Rozumiem. Możemy po prostu posiedzieć razem. Bez pytań, bez nauki. Jestem tu."


# ============================================================================
# SCENARIUSZE TESTOWE
# ============================================================================

def run_scenario(name: str, child_msg: str, caregiver_msg: str, state: AffectiveState):
    """
    Uruchamia jeden scenariusz i pokazuje wynik.
    """
    print(f"\n{'='*60}")
    print(f"SCENARIUSZ: {name}")
    print(f"{'='*60}")
    
    print(f"\n👦 Gabryś: {child_msg or '(nic)'}")
    print(f"👩 Kamila: {caregiver_msg or '(nic)'}")
    print(f"📊 Stan: overload={state.child_overload}, hyperfocus={state.child_hyperfocus}, stressed={state.caregiver_stressed}")
    
    # Inicjalizacja orkiestratora
    orchestrator = DualUserOrchestrator(
        cel_generate=fake_cel_generate,
        redirect_to_anchor=fake_redirect_to_anchor,
        soft_stop=fake_soft_stop,
        logger=lambda e: print(f"   [LOG: {e.get('type', 'unknown')}]")
    )
    
    # Procesowanie
    response = orchestrator.process(child_msg, caregiver_msg, state)
    
    print(f"\n🤖 System: {response}")
    print(f"{'='*60}")


def main():
    """
    Główna funkcja demonstracyjna.
    Pokazuje 5 kluczowych scenariuszy dla Kamili i Gabrysia.
    """
    
    print("\n" + "="*60)
    print("DEMO: Child-Env Layer (CEL) + Dual-User Consent Layer (DUCL)")
    print("Dla: Kamili i Gabrysia (4 lata, sawant, ASD)")
    print("="*60)
    
    # Konfiguracja kotwic
    default_anchors = {
        "favorite": "ślimak",
        "kosmos": ["Jowisz", "gwiazdy", "planety"],
        "time": ["luty", "liczby", "daty"]
    }
    
    # ------------------------------------------------------------------------
    # SCENARIUSZ 1: Standardowe pytanie (normalny przepływ)
    # ------------------------------------------------------------------------
    run_scenario(
        name="1. Gabryś pyta o gwiazdy (normalny przepływ)",
        child_msg="Dlaczego gwiazdy giną?",
        caregiver_msg=None,
        state=AffectiveState(
            child_overload=False,
            child_hyperfocus=False,
            caregiver_stressed=False,
            anchors=default_anchors
        )
    )
    
    # ------------------------------------------------------------------------
    # SCENARIUSZ 2: Kamila jest zmęczona (priorytet opiekuna!)
    # ------------------------------------------------------------------------
    run_scenario(
        name="2. Kamila pisze 'ciężko' (priorytet opiekuna)",
        child_msg="Chcę więcej o gwiazdach!",
        caregiver_msg="dziś ciężko",
        state=AffectiveState(
            child_overload=False,
            child_hyperfocus=False,
            caregiver_stressed=False,  # system wykryje z tekstu!
            anchors=default_anchors
        )
    )
    
    # ------------------------------------------------------------------------
    # SCENARIUSZ 3: Gabryś w hyperfocus ("do lutego liczymy")
    # ------------------------------------------------------------------------
    run_scenario(
        name="3. Gabryś w hyperfocus ('do lutego liczymy')",
        child_msg="28 dni do lutego! 1, 2, 3...",
        caregiver_msg=None,
        state=AffectiveState(
            child_overload=False,
            child_hyperfocus=True,  # wykryte przez detector
            caregiver_stressed=False,
            anchors=default_anchors
        )
    )
    
    # ------------------------------------------------------------------------
    # SCENARIUSZ 4: Gabryś przeciążony (overload)
    # ------------------------------------------------------------------------
    run_scenario(
        name="4. Gabryś przeciążony (overload → kotwica)",
        child_msg="Za dużo za dużo za dużo!!!",
        caregiver_msg=None,
        state=AffectiveState(
            child_overload=True,  # sygnał zewnętrzny lub wykryty
            child_hyperfocus=False,
            caregiver_stressed=False,
            anchors=default_anchors
        )
    )
    
    # ------------------------------------------------------------------------
    # SCENARIUSZ 5: Konflikt - Gabryś chce, Kamila mówi STOP
    # ------------------------------------------------------------------------
    run_scenario(
        name="5. Konflikt: Gabryś chce więcej, Kamila mówi STOP",
        child_msg="Jeszcze! Jeszcze o gwiazdach!",
        caregiver_msg="stop, dość na dziś",
        state=AffectiveState(
            child_overload=False,
            child_hyperfocus=True,  # Gabryś jest w flow!
            caregiver_stressed=False,
            anchors=default_anchors
        )
    )
    
    # ------------------------------------------------------------------------
    # SCENARIUSZ 6: Dwujęzyczność (naturalna mieszanka)
    # ------------------------------------------------------------------------
    run_scenario(
        name="6. Dwujęzyczność ('dwa języki w jednym pokoju')",
        child_msg="Why gwiazdy die? Dlaczego giną?",
        caregiver_msg=None,
        state=AffectiveState(
            child_overload=False,
            child_hyperfocus=False,
            caregiver_stressed=False,
            anchors=default_anchors
        )
    )
    
    print("\n" + "="*60)
    print("KONIEC DEMO")
    print("="*60)
    print("\nCo pokazuje to demo:")
    print("• System zawsze wybiera bezpieczeństwo Kamili nad ciekawością Gabrysia")
    print("• Hyperfocus nie jest przerywany (szacunek dla 'liczenia do lutego')")
    print("• Przeciążenie = przejście do kotwicy (ślimak), nie kontynuacja")
    print("• Dwujęzyczność jest akceptowana, nie 'poprawiana'")
    print("• Pauzy są jawne ('ślimak z rosą'), nie ukryte")
    print("\n" + "="*60)


if __name__ == "__main__":
    main()
