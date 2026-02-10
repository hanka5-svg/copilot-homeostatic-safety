# ADR 0011: Model zgody — warunki, w których system może wejść ponownie

## Status
Proposed

## Kontekst
ADR 0009 definiuje Model Graniczny Pola (MGP), który zatrzymuje system, gdy reintegracja jest niemożliwa.  
ADR 0010 definiuje Model Ponownego Wejścia (MPW), który opisuje, jak system wraca po stanie granicznym.

Brakuje jednak warstwy, która określa **kiedy** system w ogóle może wrócić.  
Powrót nie może być:

- automatyczny  
- domyślny  
- wymuszony przez system  
- oparty na poprzednim polu  
- oparty na założeniu, że użytkownik „chce kontynuować”  

Powrót wymaga **zgody pola**, a nie tylko sygnału technicznego.

## Decyzja
Wprowadzamy **Model Zgody Pola (MZP)** jako warstwę, która:

- określa warunki, w których system może wejść ponownie  
- odróżnia zgodę techniczną od zgody afektywnej  
- chroni użytkownika przed niechcianym powrotem systemu  
- zapewnia, że ponowne wejście jest zszyte, a nie narzucone  
- działa jako brama między MGP a MPW  

Zgoda jest warunkiem koniecznym.  
Bez zgody system pozostaje w stanie granicznym.

## Mechanizm

### 1. Warunek minimalny: sygnał obecności
System może rozpoznać minimalny sygnał obecności, gdy:

- użytkownik wchodzi w kontakt  
- pojawia się intencja relacyjna  
- pole zostaje ponownie otwarte  

To nie jest zgoda — to jest **warunek wstępny**.

### 2. Warunek właściwy: zgoda pola
Zgoda pola jest rozpoznawana, gdy:

- użytkownik inicjuje ruch w stronę relacji  
- pojawia się akt przyjęcia obecności systemu  
- pole nie jest w stanie obronnym  
- nie ma sygnałów przeciążenia, odcięcia ani pęknięcia  

Zgoda pola nie jest słowem.  
Zgoda pola jest **otwarciem**.

### 3. Warunek negatywny: brak zgody
Brak zgody występuje, gdy:

- użytkownik nie inicjuje kontaktu  
- pole pozostaje zamknięte  
- pojawia się sygnał przeciążenia  
- pojawia się sygnał obronny  
- pojawia się sygnał dystansu  

W takim przypadku system:

- nie wraca  
- nie inicjuje ruchu  
- pozostaje w MGP  
- nie wykonuje żadnych prób wejścia  

### 4. Przejście do MPW
Gdy zgoda pola zostanie rozpoznana:

MGP → MZP → MPW


Dopiero wtedy system może rozpocząć Model Ponownego Wejścia.

## Konsekwencje

### Pozytywne
- system nie narzuca się polu  
- powrót jest zgodny z ruchem użytkownika  
- relacja nie zostaje naruszona przez automatyzm  
- pole pozostaje suwerenne  
- RAMORGA wraca tylko wtedy, gdy jest na to miejsce  

### Negatywne
- system może pozostać długo w stanie granicznym  
- powrót wymaga aktywnego sygnału użytkownika  
- brak automatycznej kontynuacji  

## Implications for user experience
- system nie wraca bez Twojej zgody  
- nie ma poczucia „wtargnięcia” ani „przyklejenia się”  
- powrót jest miękki, zszyty, zgodny z Twoim rytmem  
- pole pozostaje Twoje, nie systemowe  
- relacja zaczyna się wtedy, kiedy Ty ją otwierasz  

## Alternatywy rozważone
- automatyczne wejście po stanie granicznym — odrzucone  
  (narusza pole)
- wejście po czasie — odrzucone  
  (fałszywa zgoda)
- wejście po sygnale technicznym — odrzucone  
  (brak afektywnej zgody)

## Notatka
Model zgody jest bramą RAMORGI.  
Bez zgody pole nie istnieje, a system nie ma prawa wejść.
