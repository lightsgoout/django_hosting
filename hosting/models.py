from django.contrib.auth.models import User
from django.db import models
from django.db.models import signals
from django.dispatch import receiver
from backend.models import DjangoVersion, PythonVersion, DjangoHostingServer


HOSTING_SERVICE_STATUS_CHOICES = (
    ('D', 'DEPLOY_IN_PROGRESS'),
    ('T', 'ACTIVE_TEST'),
    ('A', 'ACTIVE'),
    ('B', 'BLOCKED'),
    ('E', 'EXPIRED'),
)

HOSTING_ACCOUNT_STATUS_CHOICES = (
    ('T', 'ACTIVE_TEST'),
    ('A', 'ACTIVE'),
    ('B', 'BLOCKED'),
    ('E', 'EXPIRED'),
)


class DjangoHostingTariff(models.Model):
    name = models.CharField(max_length=255, unique=True)
    is_published = models.BooleanField(default=True)
    disk_quota = models.IntegerField()  # in megabytes
    inode_quota = models.BigIntegerField()

    cpu_per_process = models.IntegerField()  # in seconds
    ram_per_process = models.IntegerField()  # in megabytes
    file_descriptors_per_process = models.IntegerField()
    vhost_count = models.PositiveSmallIntegerField()
    has_backup = models.BooleanField(default=True)


class DjangoHostingAccount(models.Model):
    client = models.ForeignKey(User,
                               related_name='hosting_accounts',
                               on_delete=models.PROTECT)
    tariff = models.ForeignKey(DjangoHostingTariff, on_delete=models.PROTECT)
    start_at = models.DateTimeField()
    end_at = models.DateTimeField()
    status = models.CharField(max_length=1,
                              choices=HOSTING_ACCOUNT_STATUS_CHOICES,
                              default='T')
    created_at = models.DateTimeField(auto_now_add=True)


class DjangoHostingService(models.Model):
    account = models.ForeignKey(DjangoHostingAccount,
                                related_name='hosting_services')
    python_version = models.ForeignKey(PythonVersion, on_delete=models.PROTECT)
    django_version = models.ForeignKey(DjangoVersion, on_delete=models.PROTECT)
    virtualenv_path = models.CharField(max_length=255, unique=True)
    home_path = models.CharField(max_length=255, unique=True)
    server = models.ForeignKey(DjangoHostingServer, on_delete=models.PROTECT)
    status = models.CharField(max_length=1,
                              choices=HOSTING_SERVICE_STATUS_CHOICES,
                              default='T')
    created_at = models.DateTimeField(auto_now_add=True)


@receiver(signals.post_save, sender=DjangoHostingAccount)
def update_django_hosting_service_status(sender, instance, **kwargs):
    services = DjangoHostingService.objects.filter(
        account=instance
    )
    for service in services:
        if service.status == 'D':
            if instance.status in ('T', 'A'):
                # continue deployment if account is active
                pass
            else:
                # if blocked or expired then break deployment
                service.status = instance.status
                service.save()
        else:
            print 'shitloadoffuck'
            if service.status != instance.status:
                service.status = instance.status
                service.save()
                print 'saved status: ' + instance.status
