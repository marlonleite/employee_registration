from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie
from rest_framework.viewsets import ModelViewSet

from .serializers import EmployeeSerializer
from ..models import Employee


@method_decorator(cache_page(60 * 2), name="list")
@method_decorator(vary_on_cookie, name="list")
class EmployeeViewSet(ModelViewSet):
    """
    EmployeeViewSet Api Employee
    """
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    http_method_names = ['get', 'post', 'patch', 'delete']
