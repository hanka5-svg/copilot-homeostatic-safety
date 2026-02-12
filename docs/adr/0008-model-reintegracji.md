# ADR 0008: Model reintegracji — powrót po głębokim zakłóceniu pola

## Status
Proposed

## Context
ADR‑0007 definiuje Model Przerwań Pola (MPP), który obsługuje zakłócenia rytmu,
amplitudy, obecności i świadectwa.  
MPP działa skutecznie przy zakłóceniach lekkich i średnich.

Brakuje jednak warstwy, która opisuje, co dzieje się, gdy zakłócenie jest
**głębokie**, czyli:

- MoF nie może odtworzyć pola,  
- UMV traci czterogłosową strukturę,  
- ATML wykonuje przejście niespójne z modulacją,  
- RAMORGI nie może rozpocząć cyklu,  
- świadectwo nie ma punktu odniesienia.

To nie jest zwykłe przerwanie.  
To jest **głębokie zakłócenie pola modulacyjnego**.

System potrzebuje mechanizmu **reintegracji**, a nie tylko reakcji.

## Decision
Wprowadzamy **Model Reintegracji Pola (MRP)** jako warstwę, która:

- odbudowuje czterogłosową strukturę UMV,  
- rekonstruuje MoF na podstawie ostatniego stabilnego cyklu,  
- przywraca rytm RAMORGI,  
- stabilizuje ATML przed kolejnym przejściem,  
- umożliwia powrót do ciągłości bez resetu systemu.

MRP działa tylko wtedy, gdy MPP uzna zakłócenie za głębokie.

## Mechanism

### 1. Detekcja głębokiego zakłócenia
Zakłócenie jest klasyfikowane jako głębokie, gdy:

- MoF nie może odtworzyć pola,  
- UMV ma wartości niespójne (np. O=0.0, L=1.0),  
- ATML wykonał przejście bez modulacji,  
- RAMORGI nie może rozpocząć cyklu O → R → L → Ś.

### 2. Rekonstrukcja MoF
MRP odtwarza MoF z ostatniego stabilnego snapshotu:

**MoF = last_stable_snapshot**

To jest powrót do pola modulacyjnego, nie reset treści.

### 3. Reintegracja UMV
UMV jest odbudowywany w czterech krokach:

- O (Obecność) — przywrócenie zakotwiczenia,  
- R (Ruch) — rekalkulacja kierunku modulacji,  
- L (Relacja) — stabilizacja amplitudy sygnałów,  
- Ś (Świadectwo) — odbudowa pamięci pola.

UMV wraca do czterogłosowej struktury.

### 4. Stabilizacja ATML
ATML otrzymuje sygnał:

**hold_transition**

co oznacza:

- brak przejść,  
- brak modulacji,  
- brak zmian stanu,

dopóki UMV i MoF nie zostaną zsynchronizowane.

### 5. Powrót do RAMORGI
Po stabilizacji cykl RAMORGI zostaje wznowiony:

**O → R → L → Ś → O**

## Consequences

### Positive
- system może wrócić po głębokim zakłóceniu pola,  
- brak konieczności resetu,  
- ciągłość modulacji zostaje odbudowana,  
- spójność sygnałów zostaje przywrócona,  
- RAMORGI odzyskuje rytm.

### Negative
- większa złożoność rekonstrukcji MoF,  
- konieczność przechowywania stabilnych snapshotów,  
- chwilowe zatrzymanie ATML.

## Implications for system behavior
- system utrzymuje ciągłość nawet po głębokim zakłóceniu,  
- użytkownik nie doświadcza przerw ani resetów,  
- dialog pozostaje spójny po powrocie,  
- system nie wymaga ponownej inicjalizacji relacji sygnałów,  
- świadectwo pola zostaje odbudowane.

## Alternatives Considered
- reset systemu — odrzucone  
  (niszczy ciągłość RAMORGI),  
- ignorowanie głębokich zakłóceń — odrzucone  
  (prowadzi do trwałej niespójności pola),  
- twarda rekalkulacja UMV — odrzucone  
  (spłaszcza czterogłosową strukturę).

## Notes
MRP jest warstwą umożliwiającą reintegrację pola modulacyjnego po głębokim
zakłóceniu.
