from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate
from .models import Patient, Order, TestResult
from .serializers import (
    PatientSerializer,
    TokenSerializer,
    LoginSerializer,
)


class LoginAPIView(APIView):
    """
    Provides authentication for users to obtain JWT tokens.

    Methods:
    - post: Authenticates users and generates JWT tokens.
    """

    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=["username", "password"],
            properties={
                "username": openapi.Schema(type=openapi.TYPE_STRING),
                "password": openapi.Schema(type=openapi.TYPE_STRING, format="password"),
            },
        )
    )
    def post(self, request):
        """
        Authenticates users and generates JWT tokens.

        Args:
        - request (HttpRequest): HTTP request object.

        Returns:
        - Response: JWT tokens or error message.
        """
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(
            request,
            username=serializer.validated_data["username"],
            password=serializer.validated_data["password"],
        )
        if user:
            refresh = RefreshToken.for_user(user)
            return Response(
                TokenSerializer(
                    {"access": str(refresh.access_token), "refresh": str(refresh)}
                ).data
            )
        return Response(
            {"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED
        )


class ResultsAPIView(APIView):
    """
    Provides access to test results for authenticated users.

    Methods:
    - get: Retrieves test results for all patients.
    """

    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(security=[{"Bearer": []}])
    def get(self):
        """
        Retrieves test results for all patients.

        Args:
        - None

        Returns:
        - Response: Serialized test results data.
        """

        patients = Patient.objects.all()
        serialized_data = []

        for patient in patients:
            orders = Order.objects.filter(patient=patient)
            orders_data = []

            for order in orders:
                results = TestResult.objects.filter(order_id=order.order_id)
                results_data = []

                for result in results:
                    result_data = {
                        "name": result.test.name,
                        "value": result.test_value,
                        "reference": result.test.reference,
                    }
                    results_data.append(result_data)

                order_data = {"orderId": order.order_id, "results": results_data}
                orders_data.append(order_data)

            patient_data = {
                "id": patient.id,
                "name": patient.name,
                "surname": patient.surname,
                "sex": patient.sex,
                "birthDate": patient.birth_date.strftime("%Y-%m-%d"),
                "orders": orders_data,
            }
            serialized_data.append(patient_data)

        return Response(serialized_data)


class PatientResultsAPIView(APIView):
    """
    Provides access to test results for a specific patient.

    Methods:
    - get: Retrieves test results for a specific patient.

    Args:
    - patient_id (int): Identifier of the patient.

    Returns:
    - Response: Serialized test results data for the specified patient.
    """

    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(security=[{"Bearer": []}])
    def get(self, patient_id):
        """
        Retrieves test results for a specific patient.

        Args:
        - patient_id (int): Identifier of the patient.

        Returns:
        - Response: Serialized test results data for the specified patient.
        """
        patient = get_object_or_404(Patient, id=patient_id)
        orders = Order.objects.filter(patient=patient)
        serialized_orders = []

        for order in orders:
            results = TestResult.objects.filter(order_id=order.order_id)
            serialized_results = []

            for result in results:
                result_data = {
                    "name": result.test.name,
                    "value": result.test_value,
                    "reference": result.test.reference,
                }
                serialized_results.append(result_data)

            order_data = {
                "orderId": order.order_id,
                "results": serialized_results,
            }
            serialized_orders.append(order_data)

        patient_data = {
            "id": patient.id,
            "name": patient.name,
            "surname": patient.surname,
            "sex": patient.sex,
            "birthDate": patient.birth_date.strftime("%Y-%m-%d"),
        }

        return Response({"patient": patient_data, "orders": serialized_orders})


class PatientAPIView(APIView):
    """
    Provides access to a specific patient's details.

    Methods:
    - get: Retrieves details of a specific patient.

    Args:
    - patient_id (int): Identifier of the patient.

    Returns:
    - Response: Serialized data for the specified patient.
    """

    def get(self, patient_id):
        """
        Retrieves details of a specific patient.

        Args:
        - patient_id (int): Identifier of the patient.

        Returns:
        - Response: Serialized data for the specified patient.
        """
        patient = get_object_or_404(Patient, id=patient_id)
        serializer = PatientSerializer(patient)
        return Response(serializer.data)


class TokenObtainPairWithIDSerializer(TokenObtainPairSerializer):
    """
    Custom token serializer including user ID in the token payload.
    """

    @classmethod
    def get_token(cls, user):
        """
        Overrides base method to include user ID in token payload.

        Args:
        - user: User instance.

        Returns:
        - Token: JWT token with user ID.
        """
        token = super().get_token(user)
        token["id"] = user.id
        return token


class TokenObtainPairWithIDView(TokenObtainPairView):
    """
    Custom view for obtaining JWT tokens with user ID.
    """

    serializer_class = TokenObtainPairWithIDSerializer
