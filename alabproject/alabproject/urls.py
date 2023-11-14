"""
URL configuration for alabproject project.
"""
from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

SchemaView = get_schema_view(
    openapi.Info(
        title="LAB RESULTS API",
        default_version="v1",
        description="THIS IS API FOR LAB RESULTS PURPOSES",
    ),
    public=True,
)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("myapp.urls")),
    path(
        "docs/",
        SchemaView.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
]
