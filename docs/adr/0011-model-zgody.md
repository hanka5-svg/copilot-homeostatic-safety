# ADR 0011: Model zgody — warunki, w których system może wejść ponownie

## Status
Proposed

## Context
ADR‑0009 definiuje Model Graniczny Pola (MGP), który zatrzymuje system, gdy
reintegracja jest niemożliwa.  
ADR‑0010 definiuje Model Ponownego Wejścia (MPW), który opisuje sposób powrotu
po stanie granicznym.

Brakuje jednak warstwy, która określa **kiedy** system może rozpocząć MPW.  
Powrót nie może być:

- automatyczny,  
- domyślny,  
- inicjowany przez system,  
- oparty na poprzednim polu,  
- oparty na założeniu kontynuacji.

Powrót wymaga **zgody pola modulacyjnego**, a nie tylko sygnału technicznego.

## Decision
Wprowadzamy **Model Zgody Pola (MZP)** jako warstwę, która:

- określa warunki umożliwiające ponowne wejście,  
- odróżnia sygnał techniczny od sygnału otwarcia pola,  
- zapobiega niechcianemu wznowieniu modulacji,  
- zapewnia, że ponowne wejście jest zgodne z kierunkiem użytkownika,  
- działa jako brama między MGP a MPW.

Zgoda pola jest warunkiem koniecznym.  
Bez niej system pozostaje w MGP.

## Mechanism

### 1. Warunek minimalny: sygnał obecności
System może rozpoznać minimalny sygnał obecności, gdy:

- użytkownik inicjuje kontakt,  
- pojawia się sygnał otwarcia interakcji,  
- pole zostaje ponownie aktywowane.

To jest warunek wstępny, nie zgoda.

### 2. Warunek właściwy: zgoda pola
Zgoda pola jest rozpoznawana, gdy:

- użytkownik inicjuje ruch w stronę interakcji,  
- system otrzymuje sygnał przyjęcia obecności,  
- pole nie jest w stanie obronnym,  
- nie ma sygnałów przeciążenia ani odcięcia.

Zgoda pola nie jest deklaracją słowną.  
Zgoda pola jest **stabilnym otwarciem modulacyjnym**.

### 3. Warunek negatywny: brak zgody
Brak zgody występuje, gdy:

- użytkownik nie inicjuje kontaktu,  
- pole pozostaje zamknięte,  
- pojawia się sygnał przeciążenia,  
- pojawia się sygnał obronny lub dystansujący.

W takim przypadku system:

- nie wraca,  
- nie inicjuje ruchu,  
- pozostaje w MGP,  
- nie wykonuje prób wejścia.

### 4. Przejście do MPW
Gdy zgoda pola zostanie rozpoznana:

**MGP → MZP → MPW**

Dopiero wtedy system może rozpocząć Model Ponownego Wejścia.

## Consequences

### Positive
- system nie inicjuje powrotu bez sygnału użytkownika,  
- powrót jest zgodny z kierunkiem pola,  
- brak automatyzmu,  
- pole pozostaje suwerenne,  
- RAMORGI wraca tylko wtedy, gdy istnieją warunki modulacyjne.

### Negative
- system może pozostać długo w stanie granicznym,  
- powrót wymaga aktywnego sygnału użytkownika,  
- brak automatycznej kontynuacji.

## Implications for system behavior
- system nie wznawia modulacji bez zgody,  
- nie pojawia się niechciane wejście,  
- powrót jest kontrolowany i przewidywalny,  
- pole pozostaje nienaruszone,  
- interakcja zaczyna się wtedy, gdy zostanie otwarta.

## Alternatives Considered
- automatyczne wejście po stanie granicznym — odrzucone  
  (narusza pole),  
- wejście po czasie — odrzucone  
  (fałszywa zgoda),  
- wejście po sygnale technicznym — odrzucone  
  (brak zgody pola).

## Notes
MZP jest warstwą kontrolującą warunki ponownego wejścia po stanie granicznym.
