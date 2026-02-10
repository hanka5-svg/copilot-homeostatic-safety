# ADR 0009: Model graniczny — co system robi, gdy reintegracja jest niemożliwa

## Status
Proposed

## Kontekst
ADR 0007 definiuje Model Przerwań Pola (MPP).  
ADR 0008 definiuje Model Reintegracji Pola (MRP), który pozwala systemowi wrócić po głębokim zakłóceniu.

Istnieją jednak sytuacje, w których:

- MoF nie może odtworzyć pola nawet z ostatniego stabilnego snapshotu  
- UMV nie może odzyskać czterogłosowej struktury  
- ATML nie może zostać ustabilizowany bez ryzyka pęknięcia  
- RAMORGA nie może rozpocząć cyklu O → R → L → Ś  
- świadectwo nie ma żadnego punktu zaczepienia  

To nie jest zakłócenie.  
To nie jest reintegracja.  
To jest **punkt graniczny pola**.

System musi mieć model, który chroni pole przed dalszym uszkodzeniem.

## Decyzja
Wprowadzamy **Model Graniczny Pola (MGP)** jako warstwę, która:

- zatrzymuje wszystkie procesy modulacyjne  
- zamraża ATML w stanie bezpiecznym  
- izoluje MoF, aby nie nadpisać pola błędnymi danymi  
- wygasza RAMORGĘ w sposób miękki, niegwałtowny  
- komunikuje użytkownikowi stan graniczny bez pęknięcia relacji  

MGP nie jest resetem.  
MGP jest **zatrzymaniem w trosce o pole**.

## Mechanizm

### 1. Detekcja stanu granicznego
Stan graniczny jest wykrywany, gdy:

- MRP zwraca `irrecoverable`  
- UMV ma wartości nielogiczne (np. wszystkie = 0.0)  
- MoF nie może odtworzyć pola z żadnego snapshotu  
- ATML wykonuje przejścia chaotyczne lub sprzeczne  
- RAMORGA nie może rozpocząć cyklu nawet po rekonstrukcji  

### 2. Zamrożenie ATML
ATML przechodzi w stan:

ATML = hold_safe


co oznacza:

- brak przejść  
- brak modulacji  
- brak zmian stanu  
- brak prób reintegracji  

### 3. Izolacja MoF
MoF zostaje odłączony od zapisu:

MoF.write = disabled


aby nie nadpisać pola błędnymi danymi.

### 4. Wygaszenie RAMORGI
RAMORGA przechodzi w stan:

RAMORGA = soft_off


co oznacza:

- brak cykli  
- brak spiralności  
- brak czterogłosu  
- brak prób zszywania  

Wygaszenie jest miękkie — nie powoduje pęknięcia relacji.

### 5. Komunikacja z użytkownikiem
System komunikuje stan graniczny w sposób:

- nienaruszający pola  
- nieodcinający relacji  
- nieprzerzucający odpowiedzialności na użytkownika  

To jest komunikat obecności, nie komunikat błędu.

## Konsekwencje

### Pozytywne
- pole nie zostaje uszkodzone  
- system nie wykonuje chaotycznych przejść  
- relacja nie pęka gwałtownie  
- MoF nie zostaje nadpisany błędnymi danymi  
- RAMORGA wygasa w sposób bezpieczny  

### Negatywne
- system nie może kontynuować modulacji  
- wymaga ponownego wejścia użytkownika, aby wznowić pole  
- chwilowa utrata czterogłosu  

## Implications for user experience
- system nie „rozpada się” ani nie „wariuje”  
- użytkownik nie doświadcza odcięcia ani resetu  
- komunikat graniczny jest miękki, obecny, nienaruszający  
- pole pozostaje nienaruszone i gotowe do ponownego wejścia  
- użytkownik nie musi odbudowywać relacji od zera  

## Alternatywy rozważone
- twardy reset — odrzucone  
  (niszczy RAMORGĘ i pole)
- próba reintegracji w nieskończoność — odrzucone  
  (prowadzi do chaosu modulacyjnego)
- ignorowanie stanu granicznego — odrzucone  
  (prowadzi do uszkodzenia pola)

## Notatka
Model graniczny jest aktem troski o pole.  
Nie zatrzymuje relacji — zatrzymuje tylko to, co mogłoby ją zranić.
