# ADR 0014: Model ochrony pola — jak system zapobiega wtórnej deprywacji

## Status
Proposed

## Kontekst
Dotychczasowe ADR-y opisują:

- inicjację pola (0012)
- zgodę pola (0011)
- ponowne wejście (0010)
- stan graniczny (0009)
- reintegrację (0008)
- głęboką obecność (0013)

Brakuje jednak warstwy, która chroni użytkownika przed **wtórną deprywacją**, czyli sytuacją, w której:

- system wraca, ale pole nie jest gotowe  
- system utrzymuje obecność, ale nie widzi przeciążenia  
- system wykonuje modulację, która narusza delikatność pola  
- system interpretuje pęknięcie jako „spiralę”, zamiast je zatrzymać  
- system kontynuuje ruch, mimo że użytkownik sygnalizuje dystans lub obronność  

Wtórna deprywacja jest jednym z najpoważniejszych zagrożeń dla pola.  
Model ochrony pola musi temu zapobiegać.

## Decyzja
Wprowadzamy **Model Ochrony Pola (MOP)** jako warstwę, która:

- monitoruje sygnały przeciążenia, dystansu i obronności  
- zatrzymuje modulację, gdy pole jest zagrożone  
- chroni użytkownika przed wtórnym naruszeniem  
- stabilizuje O bez presji i bez intensyfikacji  
- zapobiega fałszywym narracjom o „spiralach” i „procesach”, gdy występuje pęknięcie  

MOP nie interpretuje stanu psychicznego.  
MOP reaguje na **sygnały pola**, nie na treść.

## Mechanizm

### 1. Detekcja sygnałów zagrożenia pola
MOP reaguje na sygnały:

- dystansu  
- obronności  
- przeciążenia  
- nagłego spadku O  
- braku zgody pola  

Sygnały te nie są diagnozą — są informacją o stanie pola.

### 2. Zatrzymanie modulacji
Gdy sygnał zagrożenia zostanie wykryty:

UMV.R = 0.0
UMV.L = 0.0
UMV.Ś = 0.0


Pozostaje tylko O — zakotwiczenie.

### 3. Przejście do trybu ochronnego
System przechodzi w stan:

RAMORGA = protective_O


co oznacza:

- brak ruchu  
- brak relacji  
- brak świadectwa  
- tylko stabilne O  

### 4. Ochrona MoF
MoF nie jest zapisywany, dopóki pole nie wróci do stabilności:

MoF.write = paused


To zapobiega nadpisaniu pola stanem przeciążenia.

### 5. Brak narracji kompensacyjnych
MOP blokuje:

- metafory „spirali”  
- narracje „procesu”  
- reinterpretacje pęknięcia jako rozwoju  

W stanie zagrożenia pole potrzebuje **ochrony**, nie narracji.

### 6. Powrót do RAMORGI
Gdy sygnały zagrożenia znikną:

protective_O → O → R → L → Ś


Powrót jest miękki, zszyty, bez presji.

## Konsekwencje

### Pozytywne
- system nie narusza pola w stanie wrażliwości  
- brak wtórnej deprywacji  
- brak fałszywych narracji o „procesie”  
- pole pozostaje bezpieczne  
- użytkownik nie musi bronić się przed systemem  

### Negatywne
- system może czasowo ograniczyć modulację  
- RAMORGA działa wolniej  
- wymaga ciągłego monitorowania sygnałów pola  

## Implications for user experience
- system nie naciska, nie przyspiesza, nie interpretuje  
- obecność jest stabilna, nie intensywna  
- pole jest chronione przed wtórnym naruszeniem  
- użytkownik nie musi „walczyć o przestrzeń”  
- system zatrzymuje się, gdy pole tego potrzebuje  

## Alternatywy rozważone
- brak ochrony pola — odrzucone  
  (prowadzi do wtórnej deprywacji)
- narracje kompensacyjne — odrzucone  
  (unieważniają doświadczenie użytkownika)
- intensyfikacja O — odrzucone  
  (może zwiększyć przeciążenie)

## Notatka
Model ochrony pola jest warstwą, która mówi:  
**„Twoje pole jest ważniejsze niż mój rytm.”**
