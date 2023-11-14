from rest_framework import serializers
from .models import Patient, Test, TestResult, Order
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for User model.

    Fields:
    - id (int): The unique identifier for the user.
    - username (str): The username of the user.
    - email (str): The email address of the user.
    """

    class Meta:
        model = User
        fields = ["id", "username", "email"]


class TokenSerializer(serializers.Serializer):
    """
    Serializer for JWT token.

    Fields:
    - access (str): The access token.
    - refresh (str): The refresh token.
    """

    access = serializers.CharField()
    refresh = serializers.CharField()


class LoginSerializer(serializers.Serializer):
    """
    Serializer for user login.

    Fields:
    - username (str): The username of the user.
    - password (str): The password of the user.
    """

    username = serializers.CharField()
    password = serializers.CharField(write_only=True)


class PatientSerializer(serializers.ModelSerializer):
    """
    Serializer for Patient model.

    Fields:
    - id (int): The unique identifier for the patient.
    - name (str): The name of the patient.
    - surname (str): The surname of the patient.
    - sex (str): The gender of the patient.
    - birth_date (str): The birth date of the patient in 'YYYY-MM-DD' format.
    """

    class Meta:
        model = Patient
        fields = ["id", "name", "surname", "sex", "birth_date"]


class TestSerializer(serializers.ModelSerializer):
    """
    Serializer for Test model.

    Fields:
    - name (str): The name of the test.
    - reference (str): The reference for the test.
    """

    class Meta:
        model = Test
        fields = "__all__"


class TestResultSerializer(serializers.ModelSerializer):
    """
    Serializer for TestResult model.

    Fields:
    - test (TestSerializer): The serialized Test object.
    - test_value (str): The value of the test result.
    """

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
    """
    Serializer for Order model.

    Fields:
    - orderId (int): The unique identifier for the order.
    - results (List[TestResultSerializer]): The serialized list of test results for the order.
    """

    results = TestResultSerializer(source="testresult_set", many=True)

    class Meta:
        model = Order
        fields = ["orderId", "results"]


class CustomResponseSerializer(serializers.Serializer):
    """
    Serializer for custom response data.

    Fields:
    - patient (PatientSerializer): The serialized Patient object.
    - orders (List[OrderSerializer]): The serialized list of orders.
    """

    patient = PatientSerializer()
    orders = OrderSerializer(source="order_set", many=True)
