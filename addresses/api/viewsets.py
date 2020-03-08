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
    def get(self, request, zip_code):
        """
        Method Get address
        :param zip_code: <int>
        :return: dict address
        """
        try:
            url = f"{settings.GOCEP_URL}/api/{zip_code}"
            response = requests.get(url)

        except (ConnectionError, ReadTimeout) as e:
            logging.error("Connection error")
            return Response({"error": "Connection error"},
                            status.HTTP_500_INTERNAL_SERVER_ERROR
                            )

        return Response(response.json(), response.status_code)
