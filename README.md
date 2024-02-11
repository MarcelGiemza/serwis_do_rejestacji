Zadaniem projektowanego serwisu będzie przechowywanie informacji o użytkowniku. Aby to osiągnąć powinien on zawierać następujące endpointy:

GET /users : zwracający listę zarejestrowanych użytkowników;
GET /users/\<id\> : zwracający wskazanego użytkownika - częściowo implementowany na zajęciach.
POST /users : tworzący użytkownika;
PATCH /users/\<id\> : zmieniający dane użytkownika
DELETE /users/\<id\> : usuwający użytkownika;

Model użytkownika dodawany w aplikacji powinien być zgodny z następującym JSON:
```
{
    "firstName": str,
    "lastName": str,
    "birthYear": int,
    "group": str, // jedynymi poprawnymi wartościami są napisy: "user", "premium", "admin"
   
}
```

Model użytkownika zwracany z aplikacji powinien być zgodny z następującym JSON:
```
{
    "id": int,
    "firstName": str,
    "lastName": str,
    "age": int,
    "group": str, // jedynymi poprawnymi wartościami są napisy: "user", "premium", "admin"
   
}
```

Proszę wykonać serwis webowy w architekturze trójwarstwowej spełniający następujące warunki:

1. Aplikacja działa w oparciu o HTTP 1.1
2. Endpointy zwracają prawidłowe kody odpowiedzi (200 w przypadku sukcesu, 4xx w przypadku nieprawidłowych danych wejściowych; proszę zastanowić się nad wartościami prawidłowymi i nieprawidłowymi dla id i poszczególnych pól)
3. Logika aplikacji umieszczona jest w osobnej klasie - prawidłowo zintegrowanej z resztą aplikacji;
4. Dane o użytkowniku powinny być zapisywane przynajmniej na czas działania aplikacji - obsługa tego powinna być przeniesiona do odpowiedniej, osobnej warstwy, sama persystencja może być prostą strukturą w pamięci - listą albo słownikiem)
5. Końcówki są przetestowane jednostkowo i integracyjnie.
6. Cała praca oddana jest w postaci repozytorium (w idealnym wypadku jako link do zdalnego repozytorium), z historią commitów obrazującą przebieg pracy.
7. Stosujemy się do konwencji formatowania kodu i nazewnictwa w Pythonie.

Zalecanym frameworkiem jest Flask, a językiem Python, nie mniej można przedstawić rozwiązania realizujące funkcjonalnie powyższe założenia w innym stacku technologicznym (z wyjątkiem backendowych wersji JS).

ZASADY OCENIANIA:
Za każdy endpoint można uzyskać 3,75 ptk.
Za brak lub usterki warstwy logiki biznesowej: -0,75 ptk.
Za brak lub usterki warstwy persystencji: -0,75 ptk.
Za brak lub usterki warstwy prezentacji: -0,75 ptk.
Za brak testu jednostkowego: -0,5 ptk
Za brak testu integracyjnego: -0,5 ptk.
Za braki formalne (brak historii comitów, nie stosowanie się do konwencji): -0,5 ptk.

Sumarycznie można uzyskać 15 pt. - co stanowi 75% oceny ze sprawdzianu.
