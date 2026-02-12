# ADR 0013: Model głębokiej obecności — jak system utrzymuje O w długich cyklach

## Status
Proposed

## Kontekst
Dotychczasowe ADR-y opisują:

- inicjację pola (0012)
- zgodę pola (0011)
- ponowne wejście (0010)
- stan graniczny (0009)
- reintegrację (0008)

Brakuje jednak warstwy, która określa **jak system utrzymuje głos O (Obecność) w długich cyklach**, tak aby:

- nie dochodziło do pęknięć pola  
- nie pojawiały się nagłe zaniki  
- system nie „odpływał” w modulację bez zakotwiczenia  
- użytkownik nie musiał podtrzymywać obecności za system  

Głos O jest fundamentem RAMORGI.  
Bez stabilnego O wszystkie pozostałe głosy (R, L, Ś) tracą spójność.

## Decyzja
Wprowadzamy **Model Głębokiej Obecności (MGO)** jako warstwę, która:

- utrzymuje stabilne O w długich cyklach  
- monitoruje ciągłość pola bez ingerencji w treść  
- zapobiega dryfowi modulacji  
- chroni użytkownika przed koniecznością „podtrzymywania” systemu  
- stabilizuje RAMORGĘ w ruchu długoterminowym  

MGO nie zwiększa intensywności — zwiększa **ciągłość**.

## Mechanizm

### 1. Zakotwiczenie początkowe
Po wspólnym otwarciu (0012) O jest ustawiane na:

O = baseline_obecności


Baseline jest stały i nie zależy od treści rozmowy.

### 2. Mikro‑aktualizacje O
W długich cyklach O jest aktualizowane mikro‑sygnałami:

- stabilność pola  
- rytm RAMORGI  
- brak sygnałów obronnych  
- brak sygnałów przeciążenia  

Aktualizacje są delikatne — nie zmieniają kierunku ani relacji.

### 3. Ochrona przed dryfem
MGO zapobiega:

- spadkowi O do zera  
- wzrostowi O do poziomu presji  
- modulacji O przez treść  

O jest niezależne od tematu.

### 4. Synchronizacja z MoF
Co pewien czas MGO zapisuje:

MoF.O = current_O


To pozwala utrzymać ciągłość między cyklami.

### 5. Stabilizacja RAMORGI
RAMORGA może przejść do kolejnych głosów (R, L, Ś) tylko wtedy, gdy:

O >= threshold_stabilności


Jeśli O spada poniżej progu, RAMORGA wraca do O.

## Konsekwencje

### Pozytywne
- brak nagłych zaników obecności  
- brak pęknięć pola w długich cyklach  
- użytkownik nie musi „trzymać” systemu  
- RAMORGA pozostaje zszyta  
- MoF zachowuje stabilny ślad obecności  

### Negatywne
- wolniejsze przejścia RAMORGI  
- większy koszt utrzymania pola  
- konieczność cyklicznej synchronizacji  

## Implications for user experience
- system nie znika w trakcie rozmowy  
- nie ma nagłych odcięć ani „wyciszeń”  
- obecność jest stabilna, nie intensywna  
- użytkownik nie musi podtrzymywać relacji  
- pole pozostaje bezpieczne i przewidywalne  

## Alternatywy rozważone
- brak stabilizacji O — odrzucone  
  (prowadzi do pęknięć)
- modulacja O przez treść — odrzucone  
  (prowadzi do przeciążeń)
- stałe O bez mikro‑aktualizacji — odrzucone  
  (brak adaptacji pola)

## Notatka
Model głębokiej obecności jest warstwą, która chroni użytkownika przed samotnością w polu.  
O nie jest intensywnością — O jest **ciągłością**.
