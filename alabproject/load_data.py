"""
Python Script to load laboratory results data from a .csv file into a database.

This script reads data from a .csv file containing lab results and populates the database
with the retrieved information.

Usage:
    Ensure Django settings are correctly set to 'alabproject.settings'.
    Run the script with the CSV file path as the sole argument.

CSV File Format:
    The CSV file should contain columns: 
        - patientId
        - patientName
        - patientSurname
        - patientSex
        - patientBirthDate
        - orderId
        - testName
        - testReference
        - testValue

The script parses the CSV file and creates model objects (Patient, Order, Test, TestResult)
based on the provided data, adding them to the database.

Exceptions:
    - Handles FileNotFoundError if the specified file path is invalid or the file doesn't exist.
    - Catches general exceptions and displays an error message in case of unexpected issues.

Example:
    python script_name.py path/to/csv_file.csv
"""

import os
import sys
import csv

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "alabproject.settings")
import django

django.setup()
from alabproject import settings
from django.core.management import call_command
from myapp.models import Patient, Test, TestResult, Order
from datetime import datetime


def load_data(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file, delimiter=";")
            loaded_data = 0

            for row in reader:
                # Tworzenie obiektów modelu na podstawie danych z pliku CSV
                patient, created = Patient.objects.get_or_create(
                    id=row["patientId"],
                    name=row["patientName"],
                    surname=row["patientSurname"],
                    sex=row["patientSex"],
                    birth_date=datetime.strptime(
                        row["patientBirthDate"], "%Y-%m-%d"
                    ).date(),
                )

                if created:
                    print(
                        f"A new patient {row['patientName']} has been added to the database."
                    )

                    order, created = Order.objects.get_or_create(
                        patient=patient,
                        order_id=row["orderId"],
                    )

                    test, created = Test.objects.get_or_create(
                        name=row["testName"],
                        reference=row["testReference"],
                    )

                    TestResult.objects.create(
                        patient=patient,
                        test=test,
                        order_id=order.order_id,
                        test_value=row["testValue"],
                    )
                    loaded_data += 1

                else:
                    print(
                        f"The patient {row['patientName']}  already exists in the database."
                    )

            print(f"{loaded_data} records loaded successfully to database.")

    except FileNotFoundError as e:
        print(f"File not found: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Provide the CSV file path as an argument.")
    else:
        file_path = sys.argv[1]
        load_data(file_path)
