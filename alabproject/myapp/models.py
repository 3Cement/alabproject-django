from django.db import models


class Patient(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    sex = models.CharField(max_length=10)
    birth_date = models.DateField()

    def __str__(self):
        return f"{self.name} {self.surname}"


class Test(models.Model):
    name = models.CharField(max_length=255, primary_key=True)
    reference = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class TestResult(models.Model):
    patient = models.ForeignKey("Patient", on_delete=models.CASCADE)
    test = models.ForeignKey("Test", on_delete=models.CASCADE)
    order_id = models.IntegerField()
    test_value = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.patient} - {self.test} - Order ID: {self.order_id}"


class Order(models.Model):
    patient = models.ForeignKey("Patient", on_delete=models.CASCADE)
    order_id = models.IntegerField()

    def __str__(self):
        return f"{self.patient} - Order ID: {self.order_id}"
