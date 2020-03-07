from rest_framework.serializers import ModelSerializer

from addresses.api.serializers import AddressSerializer
from employees.models import Employee


class EmployeeSerializer(ModelSerializer):
    address = AddressSerializer()

    class Meta:
        model = Employee
        fields = ['id', 'name', 'document', 'email', 'address']
