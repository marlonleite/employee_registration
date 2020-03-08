from rest_framework.viewsets import ModelViewSet

from .serializers import EmployeeSerializer
from ..models import Employee


class EmployeeViewSet(ModelViewSet):
    """
    EmployeeViewSet :GET, POST, PATCH, DEL
    """
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    http_method_names = ['get', 'post', 'patch', 'delete']
