"""

Najważniejsze jest przyjęcie pliku wejściowego, autoryzacja JWT i odesłanie pliku json.
Realizacja zadania nie powinna zająć więcej niż 2 - 4 godziny.
=

Treść zadania:

dany jest plik results.csv z wynikami badań pacjentów
proszę stworzyć aplikację, która:
będzie posiadać skrypt, uruchamiany w shellu, który wczyta zawartość tego pliku do dowolnej relacyjnej bazy danych
posiada API webowe, zawierające przynajmniej jedną metodę udostępniającą wczytane wyniki badań, np.:
/api/results
przykładowa odpowiedź z API znajduje się w załączonym pliku results.json
dostęp do metody powinien być weryfikowany tokenem uwierzytelniającym (proszę skorzystać z JWT).
aby uzyskać token, należy wysłać metodą POST na adres /api/login (może być inny) żądanie HTTP z np. taką zawartością:
{
'login': '...',
'password': '...',
}
API powinno posiadać dokumentację napisaną w OpenAPI
aplikacja powinna być napisana w języku Python lub PHP
można użyć dowolnego frameworka oraz dowolnych bibliotek (ale o otwartym kodzie, mogą być także na licencji GPL)
stworzoną aplikację proszę przesłać spakowaną, wraz z plikami struktury bazy danych, tak, aby można ją było uruchomić i przetestować lokalnie.

"""
