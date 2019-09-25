# Insert models here

from django.db import models
from django.urls import reverse


class Client(models.Model):
    client_name = models.CharField(null=False, unique=True, max_length=255)
    contact_name = models.CharField(max_length=255)
    email_address = models.CharField(null=False, max_length=255)
    phone_number = models.CharField(null=False, max_length=255)
    street_name = models.CharField(max_length=255)
    suburb = models.CharField(max_length=255)
    postcode = models.CharField(max_length=255)
    state = models.CharField(max_length=255)

    indexes = [
        models.Index(fields=['client_name']),
        models.Index(fields=['suburb']),
        models.Index(fields=['email_address'])
    ]

    def get_absolute_url(self):
        return reverse("clients:client-detail", kwargs={"id": self.id})
