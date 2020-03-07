from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=100)
    document = models.CharField(max_length=11)
    email = models.EmailField()

    def __str__(self):
        return self.name
