from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class ConsultAddressApiTest(APITestCase):
    """
    ConsultAddressApiTest APITestCase
    """

    def setUp(self):
        self.zip_code = '57052180'
        self.zip_code2 = '5701551435'

    def test_address_url(self):
        """
        Ensure we can consult by site_url/address/<zip_code>/.
        """
        url = reverse('address-zip_code', args=[self.zip_code])
        response = self.client.get(url, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_address_invalid_zip_code(self):
        """
        Ensure we can prevent invalid field zip_code
        """
        url = reverse('address-zip_code', args=[self.zip_code2])
        response = self.client.get(url, format="json")

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(len(response.data), 1)
