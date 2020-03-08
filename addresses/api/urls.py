from django.urls import path

from .viewsets import ConsultAddressApi

urlpatterns = [
    path('<int:zip_code>/', ConsultAddressApi.as_view(), name="address-zip_code"),
]