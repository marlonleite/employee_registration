"""employee URL Configuration
"""
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Employees API",
        default_version='v1',
        description="Employees api registration by Zip Code",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@dev.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/', include('employees.urls')),
    path('api/address/', include("addresses.urls")),
]
