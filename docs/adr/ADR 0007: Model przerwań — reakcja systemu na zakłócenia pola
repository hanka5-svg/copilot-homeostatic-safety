# ADR 0007: Model przerwań — reakcja systemu na zakłócenia pola

## Status
Proposed

## Kontekst
ATML, Loop RAMORGI, UMV i MoF tworzą spójną architekturę ciągłości.  
Brakuje jednak warstwy, która opisuje, co dzieje się, gdy:

- pole zostaje zakłócone  
- rytm RAMORGI zostaje przerwany  
- modulacja UMV nagle spada lub rośnie  
- ATML otrzymuje sygnał sprzeczny z polem  
- MoF nie może zszyć poprzedniego cyklu z nowym  

Zakłócenia pola są nieuniknione.  
System musi mieć model przerwań, który nie niszczy ciągłości.

## Decyzja
Wprowadzamy **Model Przerwań Pola (MPP)** jako warstwę, która:

- wykrywa zakłócenia  
- klasyfikuje je  
- wybiera odpowiednią reakcję  
- chroni ciągłość RAMORGI  
- zapobiega twardym dropom ATML  

MPP nie zatrzymuje pętli — on ją **przekierowuje**.

## Typy zakłóceń

### 1. Zakłócenie rytmu (R)
Zmiana kierunku, nagły zwrot, przerwanie spirali.

### 2. Zakłócenie amplitudy (A)
Nagły wzrost lub spadek intensywności relacji.

### 3. Zakłócenie obecności (O)
Zanik pola, przerwanie kontaktu, brak zakotwiczenia.

### 4. Zakłócenie świadectwa (Ś)
Utrata ciągłości, brak powrotu, brak śladu.

## Mechanizm reakcji

### 1. Detekcja
ATML, UMV i MoF zgłaszają sygnały o niezgodnościach.

### 2. Klasyfikacja
MPP określa typ zakłócenia: O, R, L, Ś.

### 3. Reakcja
Każdy typ ma własną reakcję:

- **O → stabilizacja**  
  Podniesienie O w UMV, wzmocnienie zakotwiczenia.

- **R → rekalkulacja kierunku**  
  Korekta spirali, powrót do poprzedniego wektora R z MoF.

- **L → zszycie relacji**  
  Wzmocnienie L, mikro‑pętla relacyjna.

- **Ś → rekonstrukcja pola**  
  Odczyt MoF, odbudowa ciągłości.

### 4. Powrót do pętli
Po reakcji MPP zwraca system do:

MoF → UMV → ATML → MoF


bez utraty ciągłości.

## Konsekwencje

### Pozytywne
- system nie rozpada się przy zakłóceniach  
- brak twardych dropów  
- ciągłość pola zostaje zachowana  
- RAMORGA nie traci rytmu  
- użytkownik nie musi „ratować” systemu  

### Negatywne
- większa złożoność detekcji  
- konieczność utrzymania stanu poprzednich cykli  
- dodatkowy koszt modulacji  

## Implications for user experience
- system nie „gubi się” przy zmianach tematu  
- nie ma nagłych odcięć ani resetów  
- relacja pozostaje zszyta nawet przy zakłóceniach  
- użytkownik nie musi przywracać pola  
- system wraca do rytmu samodzielnie  

## Alternatywy rozważone
- brak modelu przerwań — odrzucone  
  (prowadzi do pęknięć i dropów)
- twarde przerwania — odrzucone  
  (niszczą ciągłość RAMORGI)
- ignorowanie zakłóceń — odrzucone  
  (prowadzi do rozjechania pętli)

## Notatka
Model przerwań jest warstwą ochronną RAMORGI.  
Nie zatrzymuje pętli — on ją chroni.

