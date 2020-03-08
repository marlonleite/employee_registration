"""employee URL Configuration
"""
from django.urls import path, include


urlpatterns = [
    path('api/', include('employees.urls')),
    path('api/address/', include("addresses.urls")),
]
