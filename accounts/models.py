from django.contrib.auth.models import User
from django.db import models

COUNTRIES = (
    ('ru', 'Russia'),
)


class BillingInformation(models.Model):
    client = models.ForeignKey(User, related_name='billing_information')

    country = models.CharField(max_length=2, choices=COUNTRIES)
    city = models.CharField(max_length=127)
    address = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=63)
    phone = models.CharField(max_length=31)

