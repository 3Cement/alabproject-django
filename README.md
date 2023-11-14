# Aplikacja do zarządzania wynikami badań laboratoryjnych

## Opis
Aplikacja ta pozwala na wczytywanie wyników badań laboratoryjnych z pliku CSV do bazy danych oraz udostępnia te dane poprzez interfejs API.
https://github.com/3Cement/alabproject-django.git
## Instalacja
1. Sklonuj repozytorium na swój lokalny komputer lub rozpakuj archiwum. 
```bash
git clone https://github.com/3Cement/alabproject-django.git
cd alabproject-django
```
2. Utwórz wirtualne środowisko (opcjonalne, ale zalecane): 
```bash
python -m venv env
source env/bin/activate
```
2. Zainstaluj wymagane zależności używając polecenia 
```bash
pip install -r requirements.txt`
```
3. Utwórz superusera Django
Aby uzyskać dostęp do panelu administratora Django, utwórz superusera za pomocą poniższej komendy:
```bash
python manage.py createsuperuser
```
4. Uruchom migracje bazy danych za pomocą komendy 
```bash
python manage.py migrate
```
5. Uruchom serwer deweloperski Django (załóżmy że używasz portu :8000)
```bash
python manage.py runserver
```
6. Wczytaj dane z pliku results.csv za pomocą skryptu load_data.py znajdującego się w katalogu głównym. 
Upewnij się, że podajesz właściwą ścieżkę do pliku results.csv.
```bash
python load_data.py <ścieżka_do_pliku_csv>
```
7. Sprawdź wczytane dane.
Po wykonaniu skryptu sprawdź bazę danych, aby upewnić się, że dane zostały poprawnie wczytane:
- Zaloguj się do panelu administratora Django (http://localhost:8000/admin/) i przejrzyj modele Patient, Test, TestResult oraz Order, aby zobaczyć wczytane dane.

## Punkty końcowe API
Punkty Autentykacyjne
- Logowanie: http://localhost:8000/api/login

Aby zalogować się i otrzymać tokeny JWT, wyślij żądanie POST z następującym obiektem JSON:

```bash
{
    "username": "twoja_nazwa_uzytkownika",
    "password": "twoje_haslo"
}
```
Po udanej autentykacji otrzymasz token dostępu i odświeżenia.

## Dostęp do Danych Pacjentów i Wyników Badań
- Pobierz wszystkie wyniki: http://localhost:8000/api/results/ (Wymaga tokena Bearer)
- Pobierz wyniki dla konkretnego pacjenta: http://localhost:8000/api/results/<int:patient_id>/ (Wymaga tokena Bearer)
- Pobierz szczegóły pacjenta: http://localhost:8000/api/patient/<int:patient_id>/ (Wymaga tokena Bearer)
- Tokeny Bearer są wymagane do dostępu do chronionych punktów końcowych. Dołącz token w nagłówku Authorization w następujący sposób:
```bash
Authorization: Bearer <twój_token_dostępu>
```

##  Dokumentacja API
Eksploruj API za pomocą udostępnionej dokumentacji:

- Swagger UI: http://localhost:8000/docs/ - Interaktywna dokumentacja API w Swagger UI.
- OpenAPI: http://localhost:8000/docs/?format=openapi - Alternatywna dokumentacja API w formacie JSON.

