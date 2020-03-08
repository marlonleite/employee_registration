from rest_framework import serializers

from ..models import Address


class AddressSerializer(serializers.ModelSerializer):
    """
    Serializer to Address Model
    """
    class Meta:
        model = Address
        fields = "__all__"
