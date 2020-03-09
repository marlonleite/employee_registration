import logging

import requests
from django.conf import settings
from requests import ReadTimeout, ConnectionError
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class ConsultAddressApi(APIView):
    """
    View to consult Zip Code.
    """

    def get(self, request, zip_code=None):
        """
        Method Get address
        :param zip_code: <int>
        :return: dict address
        """
        if zip_code:

            try:
                url = f"{settings.GOCEP_URL}/api/{zip_code}"
                response = requests.get(url)

            except (ConnectionError, ReadTimeout) as e:
                logging.error("Connection error")
                return Response({"error": "Connection error"},
                                status.HTTP_500_INTERNAL_SERVER_ERROR
                                )
        else:

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
