from django.urls import path, include
from rest_framework import routers

from .api.viewsets import EmployeeViewSet

router = routers.DefaultRouter()

router.register(r'employees', EmployeeViewSet, basename="employee")

urlpatterns = [
    path('', include(router.urls)),
]
