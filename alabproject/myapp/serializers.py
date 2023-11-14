from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import Patient, Test, TestResult, Order
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email"]


class TokenSerializer(serializers.Serializer):
    access = serializers.CharField()
    refresh = serializers.CharField()


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ["id", "name", "surname", "sex", "birth_date"]


class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = "__all__"


class TestResultSerializer(serializers.ModelSerializer):
    test = TestSerializer()

    class Meta:
        model = TestResult
        fields = ["test", "test_value"]

    def get_test(self, obj):
        return {
            "name": obj.test.name,
            "value": obj.test_value,
            "reference": obj.test.reference,
        }


class OrderSerializer(serializers.ModelSerializer):
    results = TestResultSerializer(source="testresult_set", many=True)

    class Meta:
        model = Order
        fields = ["orderId", "results"]


class CustomResponseSerializer(serializers.Serializer):
    patient = PatientSerializer()
    orders = OrderSerializer(source="order_set", many=True)
