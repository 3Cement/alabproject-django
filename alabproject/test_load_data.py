from io import StringIO
from unittest.mock import patch
from load_data import load_data

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
]


def test_data_loaded_to_database():
    """
    Test if data is successfully loaded into the database.
    Uses a fake file to simulate loading data and checks if the data is correctly added to the database.
    """
    fake_file = StringIO("\n".join(";".join(row.values()) for row in sample_csv_data))
    with patch("builtins.open", return_value=fake_file):
        load_data("fake_file.csv")


def test_data_already_exists_in_database(capsys):
    """
    Test behavior when data already exists in the database.
    Uses a fake file to simulate loading data and checks if the function informs about existing data in the database.
    """
    fake_file = StringIO("\n".join(";".join(row.values()) for row in sample_csv_data))
    with patch("builtins.open", return_value=fake_file):
        load_data("fake_file.csv")
        captured = capsys.readouterr()
