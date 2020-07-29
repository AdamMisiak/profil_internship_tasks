1. Wczytanie danych z pliku *persons.json* do bazy danych. Przed zapisem do bazy danych:
  * stwórz dodatkowe pole z liczbą dni pozostałych do urodzin danej osoby
  * oczyść numer telefonu ze znaków specjalnych (powinny zostać same cyfry)
  * usuń pole ‘picture’.
W celach szkoleniowych hasło w postaci plaintext też powinno zostać zapisane w bazie.
2. Na podstawie danych zapisanych w bazie wyświetl:
  * procent kobiet i mężczyzn
  * średnią wieku:
    * ogólną
    * kobiet
    * mężczyzn
  * **N** najbardziej popularnych miast w formacie: miasto, liczba wystąpień, gdzie **N** to liczba - parametr przekazywany do programu przez użytkownika, czyli np. dla **N** = 5 powinno wyświetlić się 5 miast
  * **N** najpopularniejszych haseł w formacie: hasło, liczba wystąpień (**N**, analogicznie jak wyżej)
  * wszystkich użytkowników którzy urodzili się w zakresie dat podanym jako parametr (format daty jest dowolny, może być np. *YYYY-MM-DD*)
  * najbezpieczniejsze hasło - takie, które uzyska najwięcej punktów, gdzie:
    * jeśli zawiera przynajmniej jedną małą literę otrzymuje 1 punkt
    * jeśli zawiera przynajmniej jedną dużą literę otrzymuje 2 punkty
    * jeśli zawiera przynajmniej jedną cyfrę otrzymuje 1 punkt
    * jeśli zawiera co najmniej 8 znaków - 5 punktów
    * jeśli zawiera znak specjalny - 3 punkty


Czyli np. hasło “supertajne” uzyska 6 punktów (przynajmniej jedna mała litera i przynajmniej 8 znaków), “Ab1337” uzyska 4 punkty, itd.

Zaprojektowanie interfejsu linii poleceń to część tego zadania. Każdy z tych punktów powinien być zrealizowany jako osobna komenda wywoływana z tego samego skryptu, np.:

*python script.py -average-age male*

powinno zwrócić średni wiek mężczyzn z bazy danych,

*python script.py -most-common-passwords 5*

powinno zwrócić pięć najczęstszych haseł użytkowników z bazy.

Wymagania techniczne:
* Python 3.7+
* prosimy używać przede wszystkim modułów z biblioteki standardowej (poza wybranym ORMem, modułem **requests** jeśli korzysta się z API), nie korzystać z modułu **pandas**
* do implementacji interfejsu linii poleceń polecamy użyć modułu **argparse** (z biblioteki standardowej) lub **click** (https://click.palletsprojects.com/en/7.x/)
* README z opisem jak postawić projekt oraz spisem dostępnych komend
* kod napisany obiektowo
* prosimy użyć bazy danych **SQLite**
* do operacji z bazą danych można użyć dowolnego ORM-a, np. http://docs.peewee-orm.com/en/latest/

Zadania dodatkowe:
* w zadaniu 1. zamiast pobierać dane z pliku wykorzystać API - https://randomuser.me/
* napisać testy jednostkowe z użyciem pytest

Prośba o umieszczenie rozwiązania w publicznie dostępnym repozytorium systemu kontroli wersji git (github, bitbucket, gitlab itp.).
Prosimy nie skupiać się na pisaniu “ekstra optymalnego” kodu - w pierwszej kolejności będzie oceniana jakość kodu (czytelność, rozszerzalność, łatwość modyfikowania).
Na ocenę również wpłynie gitflow.
