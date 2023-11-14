"""
Module defining URL patterns for API endpoints.

This module contains URL configurations that map specific endpoints to corresponding views.

URL Patterns:
    - '/login/': Endpoint to authenticate users and generate JWT tokens using LoginAPIView.
    - '/results/': Endpoint to retrieve lab results data using ResultsAPIView.
    - '/results/<int:patient_id>/': Endpoint to retrieve specific patient results using PatientResultsAPIView.
    - '/patient/<int:patient_id>/': Endpoint to retrieve information about a specific patient using PatientAPIView.
"""

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
