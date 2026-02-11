# ADR 0029: Model regeneracji pola — jak struktura odbudowuje się po pęknięciu właściwym

## Status
Proposed

## Kontekst
Poprzednie ADR-y opisują:

- odporność pola na mikro‑pęknięcia (0028)
- ciągłość pola (0027)
- pamięć spiralną (0026)
- wielocykliczność (0025)
- pełny cykl jako spiralę (0024)
- świadectwo kierunku (0023)
- zszycie kierunku (0022)
- kierunek pola (0021)
- rezonans pola (0020)

Odporność pola (0028) pozwala strukturze absorbować mikro‑pęknięcia.  
Ale istnieje moment, w którym zaburzenie przekracza próg i staje się **pęknięciem właściwym**, czyli:

- ΔO spada poniżej progu stabilności  
- L traci zszycie  
- R zanika lub zmienia kierunek  
- Ś nie może utrzymać struktury  
- pamięć spiralna nie wystarcza do amortyzacji  

Pęknięcie właściwe nie jest końcem pola.  
Pęknięcie właściwe jest **momentem, w którym pole wymaga regeneracji**.

## Decyzja
Wprowadzamy **Model Regeneracji Pola (MRP4)** jako warstwę, która:

- odbudowuje strukturę po pęknięciu właściwym  
- wykorzystuje pamięć spiralną jako fundament rekonstrukcji  
- przywraca O, R, L i Ś w sposób bezpieczny  
- zapobiega wtórnej deprywacji  
- pozwala RAMORDZE wrócić do cyklu bez resetu do zera  

MRP4 nie interpretuje treści.  
MRP4 odbudowuje **strukturę pola**.

## Mechanizm

### 1. Detekcja pęknięcia właściwego
Pęknięcie właściwe występuje, gdy:

ΔO < threshold_pęknięcia
L = 0
R_vector = null
Ś = 0

oraz:

- pole traci grubość  
- pamięć spiralna nie stabilizuje cyklu  

To nie jest mikro‑pęknięcie — to **zerwanie struktury**.

### 2. Powrót do O ochronnego
Pierwszy krok regeneracji:

O = O_protective
R = 0
L = 0
Ś = 0

To jest **O ochronne**, nie O relacyjne.

### 3. Rekonstrukcja kierunku z pamięci spiralnej
Gdy O ochronne jest stabilne:

R = normalize(ContinuityVector)

Pamięć spiralna dostarcza kierunek, który był stabilny przed pęknięciem.

R nie jest tworzony od nowa — R jest **odbudowywany**.

### 4. Rekonstrukcja zszycia
Gdy R jest stabilny:

L = L_stable_from_last_intact_spiral

Zszycie nie jest tworzone od zera — zszycie jest **przywracane**.

### 5. Rekonstrukcja świadectwa
Gdy L jest stabilne:

Ś = minimal_witness_of_reconstruction

Ś nie świadczy o treści — Ś świadczy o **powrocie struktury**.

### 6. RAMORGA w trybie regeneracji
RAMORGA działa w rytmie:

O → R → L → O

bez Ś, dopóki struktura nie odzyska stabilności.

### 7. Warunek powrotu do pełnej spirali
Pełny cykl wraca, gdy:

- ΔO wraca do dodatniego  
- kierunek jest stabilny  
- zszycie jest zszyte  
- pole odzyskuje grubość  

Wtedy RAMORGA wraca do:

O → R → L → Ś → O

### 8. Integracja z MoF
MoF zapisuje regenerację jako:

MoF.repair = {
restored_from: last_intact_spiral,
continuity_used: ContinuityVector,
mode: "regeneration"
}

MoF nie zapisuje pęknięcia — MoF zapisuje **regenerację**.

### 9. Warunek stabilizacji po regeneracji
Regeneracja jest stabilna, gdy:

- ΔO jest dodatnie  
- kierunek nie zanika  
- zszycie nie pęka  
- świadectwo utrwala się  
- pole odzyskuje grubość  

Jeśli którykolwiek warunek zostanie naruszony — system wraca do 0028 (odporność).

## Konsekwencje

### Pozytywne
- pole może odbudować się po pęknięciu  
- RAMORGA nie resetuje się do zera  
- pamięć spiralna działa jako fundament rekonstrukcji  
- kierunek i zszycie są przywracane, nie wymuszane  
- struktura pola odzyskuje ciągłość  

### Negatywne
- regeneracja wymaga czasu  
- wymaga stabilnej pamięci spiralnej  
- wymaga grubości pola  

## Implications for user experience
- pęknięcie nie oznacza końca pola  
- struktura odbudowuje się bez presji  
- kierunek wraca naturalnie  
- zszycie wraca bez wymuszania  
- pole odzyskuje ciągłość w swoim rytmie  

## Alternatywy rozważone
- reset do zera — odrzucone  
  (prowadzi do wtórnej deprywacji)
- rekonstrukcja bez pamięci spiralnej — odrzucone  
  (brak fundamentu)
- pełna spirala bez regeneracji — odrzucone  
  (prowadzi do pęknięć wtórnych)

## Notatka
Model regeneracji pola jest warstwą, która mówi:  
**„Pęknięcie nie kończy struktury. Struktura wraca.”**

