import logging

import requests
from django.conf import settings
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from requests import ReadTimeout, ConnectionError
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class ConsultAddressZipCodeApi(APIView):
    """
    Show a address view by zip code
    """

    @method_decorator(cache_page(60 * 60 * 2))
    def get(self, request, zip_code):
        try:
            url = f"{settings.GOCEP_URL}/api/{zip_code}"
            response = requests.get(url)

        except (ConnectionError, ReadTimeout) as e:
            logging.error("Connection error")
            return Response({"error": "Connection error"},
                            status.HTTP_500_INTERNAL_SERVER_ERROR
                            )

        return Response(response.json(), response.status_code)


class ConsultAddressApi(APIView):
    """
    Show a address view by url query params
    """

    @method_decorator(cache_page(60 * 60 * 2))
    def get(self, request, format=None):
        """
        :parameter url: federated_state, city, street

        """
        address_data = {}
        for k, v in request.query_params.items():
            address_data.update({k: v})

        allowed_keys = {"federated_state", "city", "street"}

        if allowed_keys != address_data.keys():
            message = "Required fields federated_state, city, street."
            return Response({'message': message}, status.HTTP_400_BAD_REQUEST)

        url = f"{settings.GOCEP_URL}/api/"
        response = requests.get(url, address_data)

        return Response(response.json(), response.status_code)
