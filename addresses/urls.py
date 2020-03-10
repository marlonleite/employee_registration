from django.urls import path

from .api.viewsets import ConsultAddressApi, ConsultAddressZipCodeApi

urlpatterns = [
    path('<int:zip_code>/', ConsultAddressZipCodeApi.as_view(), name="address-zip_code"),
    path('', ConsultAddressApi.as_view(), name="address"),
]