# Generated by Django 4.2.7 on 2023-11-13 19:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Patient",
            fields=[
                ("patient_id", models.IntegerField(primary_key=True, serialize=False)),
                ("patient_name", models.CharField(max_length=255)),
                ("patient_surname", models.CharField(max_length=255)),
                ("patient_sex", models.CharField(max_length=10)),
                ("patient_birth_date", models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name="Test",
            fields=[
                (
                    "test_name",
                    models.CharField(max_length=255, primary_key=True, serialize=False),
                ),
                ("test_reference", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="TestResult",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("order_id", models.IntegerField()),
                ("test_value", models.CharField(max_length=255)),
                (
                    "patient",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="myapp.patient"
                    ),
                ),
                (
                    "test",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="myapp.test"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Order",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("order_id", models.IntegerField()),
                (
                    "patient",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="myapp.patient"
                    ),
                ),
            ],
        ),
    ]