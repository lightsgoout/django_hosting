from django.contrib.auth.models import AbstractBaseUser
from django.db import models

COUNTRIES = (
    ('ru', 'Russia'),
)


class Client(AbstractBaseUser):
    is_organization = models.BooleanField(default=False)
    full_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True, db_index=True)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name', 'email']

    def get_full_name(self):
        return self.full_name

    def get_short_name(self):
        return self.email


class BillingInformation(models.Model):
    client = models.ForeignKey(Client, related_name='billing_information')

    country = models.CharField(max_length=2, choices=COUNTRIES)
    city = models.CharField(max_length=127)
    address = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=63)
    phone = models.CharField(max_length=31)

