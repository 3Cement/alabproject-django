from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import Patient, Order, TestResult
from .serializers import (
    PatientSerializer,
    TokenSerializer,
    LoginSerializer,
)
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class LoginAPIView(APIView):
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
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(security=[{"Bearer": []}])
    def get(self, request):
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
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(security=[{"Bearer": []}])
    def get(self, request, patient_id):
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
    def get(self, request, patient_id):
        patient = get_object_or_404(Patient, id=patient_id)
        serializer = PatientSerializer(patient)
        return Response(serializer.data)


class TokenObtainPairWithIDSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token["id"] = user.id
        return token


class TokenObtainPairWithIDView(TokenObtainPairView):
    serializer_class = TokenObtainPairWithIDSerializer
