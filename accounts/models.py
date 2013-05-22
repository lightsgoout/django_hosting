from django.contrib.auth.models import User
from django.db import models
from django.db.models import signals
from django.dispatch import receiver
from hosting.models import DjangoHostingTariff

COUNTRIES = (
    ('ru', 'Russia'),
)


class DjangoAccount(models.Model):
    user = models.OneToOneField(User, related_name='django_account')

    django_tariff = models.ForeignKey(
        DjangoHostingTariff,
        null=True
    )


class BillingInformation(models.Model):
    user = models.OneToOneField(User, related_name='billing_information')

    country = models.CharField(max_length=2, choices=COUNTRIES)
    city = models.CharField(max_length=127)
    address = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=63)
    phone = models.CharField(max_length=31)


@receiver(signals.post_save, sender=User)
def create_django_account(sender, instance, **kwargs):
    if not DjangoAccount.objects.filter(user=instance).exists():
        DjangoAccount.objects.create(user=instance)


@receiver(signals.post_save, sender=User)
def create_django_account(sender, instance, **kwargs):
    if not BillingInformation.objects.filter(user=instance).exists():
        BillingInformation.objects.create(user=instance)
