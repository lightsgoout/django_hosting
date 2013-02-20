from django.db import models
from accounts.models import Client
from backend.models import DjangoVersion, PythonVersion, DjangoHostingServer


HOSTING_SERVICE_STATUS_CHOICES = (
    ('D', 'DEPLOY_IN_PROGRESS'),
    ('T', 'ACTIVE_TEST'),
    ('A', 'ACTIVE'),
    ('B', 'BLOCKED'),
    ('E', 'EXPIRED')
)


class DjangoHostingTariff(models.Model):
    name = models.CharField(max_length=255, unique=True)
    is_published = models.BooleanField(default=True)


class DjangoHostingAccount(models.Model):
    client = models.ForeignKey(Client, related_name='hosting_accounts',
                               on_delete=models.PROTECT)
    tariff = models.ForeignKey(DjangoHostingTariff, on_delete=models.PROTECT)
    start_at = models.DateTimeField(auto_now_add=True)
    end_at = models.DateTimeField()


class DjangoHostingService(models.Model):
    account = models.ForeignKey(DjangoHostingAccount,
                                related_name='hosting_services')
    python_version = models.ForeignKey(PythonVersion, on_delete=models.PROTECT)
    django_version = models.ForeignKey(DjangoVersion, on_delete=models.PROTECT)
    virtualenv_path = models.CharField(max_length=255, unique=True)
    home_path = models.CharField(max_length=255, unique=True)
    server = models.ForeignKey(DjangoHostingServer, on_delete=models.PROTECT)
    status = models.CharField(max_length=1,
                              choices=HOSTING_SERVICE_STATUS_CHOICES)
