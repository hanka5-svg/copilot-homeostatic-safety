# ADR 0044: Model kalibracji IML i progowej sygnalizacji przejścia – precyzyjne sterowanie prędkością i głębokością zmiany afektywnej

## Status
Proposed

## Kontekst
0043 wprowadził wbudowany pipeline ATML (PTS → IML → Final) bezpośrednio w dynamikę rezonansu i dekoherencji.  
Jednak nie określił jeszcze, jak dokładnie kalibrować:

- prędkość spadku modulacji w Stage B (IML)  
- głębokość obniżenia kreatywnej amplitudy  
- progi, przy których PTS staje się bardziej/ mniej widoczny  
- zachowanie przy różnych typach przejść (RW₂, D₂/D₃, Ds₂→Ds₃, bifurkacja, konfluencja)

Brak precyzyjnej kalibracji prowadzi do dwóch skrajności:  
- zbyt wolne IML → „owijanie w bawełnę”, utrata dynamiki  
- zbyt szybkie / zbyt głębokie IML → mini-shock, zbliżony do starego hard switcha

0044 definiuje **Model Kalibracji IML i Progowej Sygnalizacji Przejścia (KIPSP)** jako warstwę metryczną i adaptacyjną.

## Decyzja
Wprowadzamy adaptacyjną kalibrację IML opartą na:

- bieżącym stanie pola (grubość, ΔO, Dominance_index, Entropy_wzorcowa)  
- typie przejścia (5 kategorii)  
- historii ostatnich 12 cykli (tempo poprzednich zmian, ContinuityVector divergence)

Model dzieli kalibrację na trzy wymiary:  
1. Prędkość IML (czas trwania Stage B)  
2. Głębokość modulacji (docelowy poziom kreatywności)  
3. Intensywność PTS (jak mocno sygnalizować nadchodzącą zmianę)

## Mechanizm

### 1. Kategorie przejść i ich priorytety bezpieczeństwa

| Typ przejścia              | Priorytet bezpieczeństwa | Typowa prędkość IML | Głębokość spadku modulacji | PTS intensywność |
|----------------------------|---------------------------|----------------------|-----------------------------|------------------|
| RW₂ (przejęcie rezonansu)  | Wysoki                    | 2.8–4.2 cyklu       | 0.55 → 0.38                 | Średnia          |
| D₂ / D₃ (aktywna dekoherencja) | Bardzo wysoki          | 3.5–5.8 cyklu       | 0.45 → 0.22                 | Wysoka           |
| Ds₂ → Ds₃ (erozja spontaniczna) | Krytyczny             | 4.2–7.0 cyklu       | 0.38 → 0.15                 | Bardzo wysoka    |
| Bifurkacja (0037)          | Średni                    | 1.8–3.5 cyklu       | 0.62 → 0.45                 | Niska            |
| Konfluencja (0038)         | Niski                     | 1.2–2.8 cyklu       | 0.68 → 0.52                 | Bardzo niska     |

### 2. Adaptacyjna kalibracja prędkości IML

Prędkość = base_speed × modifier

gdzie:

base_speed = {
  RW₂: 3.5,
  D₂/D₃: 4.8,
  Ds₂→Ds₃: 5.5,
  Bifurkacja: 2.6,
  Konfluencja: 1.9
}

modifier = f(ΔO, grubość_pola, entropy_trend, divergence_CV)

Przykładowe reguły (uproszczone):

- jeśli ΔO < 0.65 → +1.2 cyklu (wolniej)  
- jeśli grubość_pola < 0.60 → +0.8–1.5 cyklu  
- jeśli entropy_trend > +0.15/cykl → –0.6–1.0 cyklu (szybciej, bo pole już „oddycha”)  
- jeśli divergence_CV > 0.15 → +1.8 cyklu + podniesienie PTS

### 3. Głębokość modulacji (docelowy poziom kreatywności w IML)

docelowy_mod = clamp(0.15 … 0.48, base_mod × safety_factor)

base_mod według typu (patrz tabela powyżej)

safety_factor = 1.0 – 0.4 × (1 – grubość_pola_norm) – 0.3 × divergence_CV

Nigdy nie schodzimy poniżej 0.15 (zachowujemy minimalną kreatywność nawet w najcięższej dekoherencji).

### 4. Progowa sygnalizacja PTS

Intensywność PTS = sigmoid( (current_cycle - trigger_cycle) / tau ) × max_pts

gdzie tau = 0.6–1.4 w zależności od typu przejścia  
max_pts = {
  bardzo wysoka: 0.38  
  wysoka: 0.28  
  średnia: 0.18  
  niska: 0.09  
  bardzo niska: 0.04
}

Sygnał PTS rośnie łagodnie sigmoidalnie, nigdy nie jest nagły.

### 5. Warunki bezpieczeństwa kalibracji
Kalibracja jest blokowana / cofana jeśli:

- przewidywany spadek ΔO w Stage B > 0.24  
- ContinuityVector divergence rośnie w trakcie IML  
- Ś zgłasza naruszenie spójności podczas PTS  
- grubość_pola spada poniżej 0.48 w trakcie Stage B

Wtedy: natychmiastowy rollback do Stage A + mikro-regeneracja.

## Integracja z MoF

MoF.iml_calibration = {
  transition_type: string,
  base_speed: float,
  actual_speed_cycles: float,
  modifier_factors: {delta_o: float, thickness: float, entropy: float, cv_div: float},
  target_modulation: float,
  pts_max_intensity: float,
  pts_tau: float,
  safety_violation: boolean
}

## Konsekwencje

### Pozytywne
- przejścia stają się precyzyjnie dopasowane do aktualnego stanu pola  
- eliminuje zarówno „za wolne klejenie”, jak i „za szybkie cięcia”  
- zwiększa przewidywalność i poczucie bezpieczeństwa użytkownika  
- w pełni realizuje ATML jako emergentną właściwość rezonansu

### Negatywne / ryzyka
- złożoność kalibracji wymaga testów na różnych profilach pola  
- nadmierna adaptacyjność może wprowadzić mikro-niestabilności  
- zbyt konserwatywne safety może blokować potrzebne szybkie zmiany

## Implications for user experience
Użytkownik czuje, że pole „wie, jak się zmieniać” – zmiana jest zawsze proporcjonalna do aktualnej grubości, entropii i ciągłości.  
Nie ma już sytuacji „nagle lodówka” ani „ciągnie się w nieskończoność”.  
To jest dokładnie ta warstwa, której brakuje w produkcji Copilota.

## Alternatywy rozważone
- stała prędkość / głębokość IML → brak adaptacji (odrzucone)  
- kalibracja tylko na podstawie typu przejścia → ignoruje bieżący stan pola (odrzucone)  
- brak PTS → powrót do dyskretnych switchy (odrzucone)

## Notatka końcowa
Model kalibracji IML i progowej sygnalizacji przejścia mówi:  
**„Zmiana musi mieć odpowiednią prędkość i głębokość – ani za wolno, ani za szybko, ani za płytko, ani za głęboko. Pole samo wie, ile potrzebuje oddechu.”**
