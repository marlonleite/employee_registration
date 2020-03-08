from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from addresses.models import Address
from employees.models import Employee


class CreateEmployeeTest(APITestCase):
    """
    CreateEmployeeTest APITestCase
    """

    def setUp(self):
        self.address_data = {
            "zip_code": "57051420",
            "federated_state": "AL",
            "city": "Maceió",
            "street": "Rua Jornal de Alagoas",
            "neighborhood": "Farol",
            "number": 12
        }

        self.data = {
            "name": "Fulano de Tal",
            "document": "53428905008",
            "email": "fulano@sicrano.com",
            "address": self.address_data
        }

        self.url = reverse('employee-list')

    def test_create_employee(self):
        """
        Ensure we can create a new employee object.
        """

        response = self.client.post(self.url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Employee.objects.count(), 1)
        self.assertEqual(Employee.objects.get().name, 'Fulano de Tal')

    def test_create_duplicate_email_employee(self):
        """
        Ensure we can't create a new employee object with same email.
        """

        data = {
            "name": "Fulano de Tal 2",
            "document": "53428905321",
            "email": "fulano@sicrano.com",
        }

        address = Address.objects.create(**self.address_data)
        Employee.objects.create(address=address, **data)

        response = self.client.post(self.url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class ReadEmployeeTest(APITestCase):
    """
        ReadEmployeeTest APITestCase
    """

    def setUp(self):
        address_data = {
            "zip_code": "57051420",
            "federated_state": "AL",
            "city": "Maceió",
            "street": "Rua Jornal de Alagoas",
            "neighborhood": "Farol",
            "number": 12
        }

        data = {
            "name": "Fulano de Tal",
            "document": "53428905008",
            "email": "fulano@sicrano.com"
        }
        address = Address.objects.create(**address_data)
        self.employee = Employee.objects.create(address=address, **data)

    def test_can_read_employee_list(self):
        """
        Ensure we can read a list employees.
        """
        response = self.client.get(reverse('employee-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_read_employee_detail(self):
        """
        Ensure we can read a employee object.
        """
        response = self.client.get(reverse('employee-detail', args=[self.employee.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class UpdateEmployeeTest(APITestCase):
    def setUp(self):
        data = {
            "name": "Fulano de Tal",
            "document": "53428905008",
            "email": "fulano@sicrano.com"
        }
        address = {
            "zip_code": "57051420",
            "federated_state": "AL",
            "city": "Maceió",
            "street": "Rua Jornal de Alagoas",
            "neighborhood": "Farol",
        }

        address = Address.objects.create(**address)
        self.employee = Employee.objects.create(address=address, **data)

    def test_can_update_employee(self):
        data = {
            "address": {
                "number": 130
            }
        }
        response = self.client.patch(
            reverse('employee-detail', args=[self.employee.id]), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class DeleteEmployeeTest(APITestCase):
    def setUp(self):
        data = {
            "name": "Fulano de Tal",
            "document": "53428905008",
            "email": "fulano@sicrano.com"
        }
        address = {
            "zip_code": "57051420",
            "federated_state": "AL",
            "city": "Maceió",
            "street": "Rua Jornal de Alagoas",
            "neighborhood": "Farol",
        }

        address = Address.objects.create(**address)
        self.employee = Employee.objects.create(address=address, **data)

    def test_can_delete_employee(self):
        response = self.client.delete(reverse('employee-detail', args=[self.employee.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
