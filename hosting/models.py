from django.contrib.auth.models import User
from django.db import models
from django.db.models import signals
from django.dispatch import receiver
from backend.models import DjangoVersion, PythonVersion, DjangoHostingServer

HOSTING__HOME_PATH = "/home/hosting/"
HOSTING__VIRTUALENVS_PATH = HOSTING__HOME_PATH + ".virtualenvs/"

HOSTING_SERVICE_DEPLOY_IN_PROGRESS = 'D'
HOSTING_SERVICE_ACTIVE_TEST = 'T'
HOSTING_SERVICE_ACTIVE = 'A'
HOSTING_SERVICE_BLOCKED = 'B'
HOSTING_SERVICE_EXPIRED = 'E'

HOSTING_SERVICE_STATUS_CHOICES = (
    (HOSTING_SERVICE_DEPLOY_IN_PROGRESS, 'DEPLOY_IN_PROGRESS'),
    (HOSTING_SERVICE_ACTIVE_TEST, 'ACTIVE_TEST'),
    (HOSTING_SERVICE_ACTIVE, 'ACTIVE'),
    (HOSTING_SERVICE_BLOCKED, 'BLOCKED'),
    (HOSTING_SERVICE_EXPIRED, 'EXPIRED'),
)

HOSTING_ACCOUNT_ACTIVE_TEST = HOSTING_SERVICE_ACTIVE_TEST
HOSTING_ACCOUNT_ACTIVE = HOSTING_SERVICE_ACTIVE
HOSTING_ACCOUNT_BLOCKED = HOSTING_SERVICE_BLOCKED
HOSTING_ACCOUNT_EXPIRED = HOSTING_SERVICE_EXPIRED

HOSTING_ACCOUNT_STATUS_CHOICES = (
    (HOSTING_ACCOUNT_ACTIVE_TEST, 'ACTIVE_TEST'),
    (HOSTING_ACCOUNT_ACTIVE, 'ACTIVE'),
    (HOSTING_ACCOUNT_BLOCKED, 'BLOCKED'),
    (HOSTING_ACCOUNT_EXPIRED, 'EXPIRED'),
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

    def __unicode__(self):
        return self.name


class DjangoHostingAccount(models.Model):
    client = models.ForeignKey(User,
                               related_name='hosting_accounts',
                               on_delete=models.PROTECT)
    tariff = models.ForeignKey(DjangoHostingTariff, on_delete=models.PROTECT)
    start_at = models.DateTimeField()
    end_at = models.DateTimeField()
    status = models.CharField(max_length=1,
                              choices=HOSTING_ACCOUNT_STATUS_CHOICES,
                              default=HOSTING_ACCOUNT_ACTIVE_TEST)
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return '%s\'s %s' % (self.client, self.tariff)


class DjangoHostingService(models.Model):
    account = models.ForeignKey(DjangoHostingAccount,
                                related_name='hosting_services')
    python_version = models.ForeignKey(PythonVersion, on_delete=models.PROTECT)
    django_version = models.ForeignKey(DjangoVersion, on_delete=models.PROTECT)
    virtualenv_path = models.CharField(max_length=255, unique=True, blank=True,
                                       null=True)
    home_path = models.CharField(max_length=255, unique=True, blank=True,
                                 null=True)
    server = models.ForeignKey(DjangoHostingServer, on_delete=models.PROTECT)
    status = models.CharField(max_length=1,
                              choices=HOSTING_SERVICE_STATUS_CHOICES,
                              default=HOSTING_SERVICE_ACTIVE_TEST)
    created_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        from django.core.exceptions import ValidationError

        if not self.server.is_python_version_supported(self.python_version):
            raise ValidationError(
                '%s does not support %s' % (self.server, self.python_version)
            )
        if not self.django_version.is_python_version_supported(
                self.python_version
        ):
            raise ValidationError(
                '%s does not support %s' % (self.django_version,
                                            self.python_version)
            )

        if not self.server.is_published:
            raise ValidationError('%s is not published' % self.server)

    def __unicode__(self):
        def get_status(status):
            if status == HOSTING_SERVICE_ACTIVE:
                return 'ACTIVE'
            if status == HOSTING_SERVICE_DEPLOY_IN_PROGRESS:
                return 'DEPLOY_IN_PROGRESS'
            if status == HOSTING_SERVICE_ACTIVE_TEST:
                return 'ACTIVE_TEST'
            if status == HOSTING_ACCOUNT_BLOCKED:
                return 'BLOCKED'
            if status == HOSTING_ACCOUNT_EXPIRED:
                return 'EXPIRED'

        s = "[%s] %s %s at %s" % (get_status(self.status), self.pk,
                                  self.account, self.server.hostname)
        return s


@receiver(signals.post_save, sender=DjangoHostingService)
def populate_django_hosting_service_virtualenv_and_path(sender, instance,
                                                        **kwargs):
    if not instance.virtualenv_path or not instance.home_path:
        instance.virtualenv_path = "%s%s" % (HOSTING__VIRTUALENVS_PATH,
                                             instance.pk)
        instance.home_path = "%s%s" % (HOSTING__HOME_PATH, instance.pk)
        instance.save()


@receiver(signals.post_save, sender=DjangoHostingAccount)
def update_django_hosting_service_status(sender, instance, **kwargs):
    services = DjangoHostingService.objects.filter(
        account=instance
    )
    for service in services:
        if service.status == HOSTING_SERVICE_DEPLOY_IN_PROGRESS:
            if instance.status in (HOSTING_ACCOUNT_ACTIVE_TEST,
                                   HOSTING_ACCOUNT_ACTIVE):
                # continue deployment if account is active
                pass
            else:
                # if blocked or expired then break deployment
                service.status = instance.status
                service.save()
        else:
            if service.status != instance.status:
                service.status = instance.status
                service.save()
