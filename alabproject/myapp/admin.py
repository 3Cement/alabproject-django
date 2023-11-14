from django.contrib import admin
from .models import Patient, Test, TestResult, Order

admin.site.register(Patient)
admin.site.register(Test)
admin.site.register(TestResult)
admin.site.register(Order)
