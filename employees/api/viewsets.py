from rest_framework.viewsets import ModelViewSet

from .serializers import EmployeeSerializer
from ..models import Employee


class EmployeeViewSet(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
