from django.urls import path
from .views import (
    ResultsAPIView,
    PatientAPIView,
    LoginAPIView,
    PatientResultsAPIView,
)

urlpatterns = [
    path("login/", LoginAPIView.as_view(), name="login"),
    path("results/", ResultsAPIView.as_view(), name="results"),
    path(
        "results/<int:patient_id>/",
        PatientResultsAPIView.as_view(),
        name="patient_results",
    ),
    path("patient/<int:patient_id>/", PatientAPIView.as_view(), name="patient"),
]
