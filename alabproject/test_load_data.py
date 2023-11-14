from io import StringIO
from datetime import datetime
import pytest
from unittest.mock import patch

# Import funkcji do testów
from load_data import load_data

# Dane testowe
sample_csv_data = [
    {
        "patientId": "1",
        "patientName": "John",
        "patientSurname": "Doe",
        "patientSex": "Male",
        "patientBirthDate": "1990-01-01",
        "orderId": "1",
        "testName": "Blood Test",
        "testReference": "BT001",
        "testValue": "Normal",
    },
    # Możesz dodać więcej danych testowych
]


# Testowanie poprawnego załadowania danych do bazy
def test_data_loaded_to_database():
    fake_file = StringIO("\n".join(";".join(row.values()) for row in sample_csv_data))
    with patch("builtins.open", return_value=fake_file):
        load_data("fake_file.csv")
        # Sprawdzenie czy dane zostały dodane poprawnie do bazy danych


# Testowanie sytuacji, gdy dane już istnieją w bazie danych
def test_data_already_exists_in_database(capsys):
    fake_file = StringIO("\n".join(";".join(row.values()) for row in sample_csv_data))
    with patch("builtins.open", return_value=fake_file):
        load_data("fake_file.csv")
        captured = capsys.readouterr()
        # Sprawdzenie czy funkcja informuje o istniejących już danych w bazie
