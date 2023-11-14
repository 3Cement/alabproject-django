from django.db import models


class Patient(models.Model):
    """
    Represents information about a patient.

    Fields:
    - id (int): The unique identifier for the patient.
    - name (str): The patient's first name.
    - surname (str): The patient's last name.
    - sex (str): The patient's gender.
    - birth_date (Date): The patient's date of birth.
    """

    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    sex = models.CharField(max_length=10)
    birth_date = models.DateField()

    def __str__(self):
        return f"{self.name} {self.surname}"


class Test(models.Model):
    """
    Represents a laboratory test.

    Fields:
    - name (str): The name of the test.
    - reference (str): Reference information for the test.
    """

    name = models.CharField(max_length=255, primary_key=True)
    reference = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}"


class TestResult(models.Model):
    """
    Stores laboratory test results for patients.

    Fields:
    - patient (ForeignKey): The associated patient for the test result.
    - test (ForeignKey): The specific test performed.
    - order_id (int): The order ID for the test result.
    - test_value (str): The value obtained from the test.
    """

    patient = models.ForeignKey("Patient", on_delete=models.CASCADE)
    test = models.ForeignKey("Test", on_delete=models.CASCADE)
    order_id = models.IntegerField()
    test_value = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.patient} - {self.test} - Order ID: {self.order_id}"


class Order(models.Model):
    """
    Stores information about test orders for patients.

    Fields:
    - patient (ForeignKey): The associated patient for the order.
    - order_id (int): The order ID for the test.
    """

    patient = models.ForeignKey("Patient", on_delete=models.CASCADE)
    order_id = models.IntegerField()

    def __str__(self):
        return f"{self.patient} - Order ID: {self.order_id}"
