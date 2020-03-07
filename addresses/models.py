from django.db import models


class Address(models.Model):
    street = models.CharField(max_length=150)
    number = models.IntegerField()
    neighborhood = models.CharField(max_length=50)
    city = models.CharField(max_length=100)
    federated_state = models.CharField(max_length=2)
    zip_code = models.CharField(max_length=8)

    def __str__(self):
        return "{} {} {} - {}-{} {}".format(
            self.street,
            self.number,
            self.neighborhood,
            self.city,
            self.federated_state,
            self.zip_code,
        )
