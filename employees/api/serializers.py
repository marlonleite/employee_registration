from rest_framework import serializers

from addresses.api.serializers import AddressSerializer
from addresses.models import Address
from ..models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    """
    Serializer to Employee Model
    """
    address = AddressSerializer()

    class Meta:
        model = Employee
        fields = ['id', 'name', 'document', 'email', 'address']
        extra_kwargs = {
            'document': {'error_messages': {
                'max_length': "Ensure this field has no more than 11 digits."}},
        }

    def validate_document(self, attr):
        if len(attr) < 11:
            raise serializers.ValidationError(
                "Ensure this field has at least 11 digits.")
        return attr

    def validate_email(self, attr):
        if Employee.objects.filter(email=attr).exists():
            raise serializers.ValidationError(
                "This email is already in use.")
        return attr

    def create(self, validated_data):
        address_data = validated_data.pop('address')
        employee = Employee.objects.create(**validated_data)
        if address_data:
            address = Address.objects.create(**address_data)
            employee.address = address
            employee.save()

        return employee

    def update(self, instance, validated_data):
        address_data = validated_data.get('address')

        if address_data:
            instance.address.__dict__.update(**address_data)
            instance.address.save()

        instance.__dict__.update(**validated_data)
        instance.save()
        return instance
