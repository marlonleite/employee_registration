from django.db import models

from addresses.models import Address


class Employee(models.Model):
    name = models.CharField(max_length=100)
    document = models.CharField(max_length=11)
    email = models.EmailField()
    address = models.ForeignKey(
        Address, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name
