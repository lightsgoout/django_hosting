import os
from urlparse import urlparse
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import signals
from django.dispatch import receiver
from backend.models import DjangoVersion, PythonVersion, DjangoHostingServer

# All paths must end with trailing slash
from utils import is_path_secure, is_valid_python_module

HOSTING__NGINX_USER = "www-data"
HOSTING__NGINX_GROUP = "www-data"

HOSTING__HOME_PATH = "/home/hosting/"
HOSTING__VIRTUALENVS_PATH = HOSTING__HOME_PATH + ".virtualenvs/"
HOSTING__UWSGI_CONFIG_PATH = HOSTING__HOME_PATH + ".uwsgi/"
HOSTING__NGINX_CONFIG_PATH = HOSTING__HOME_PATH + ".nginx/"
HOSTING__LOG_RELATIVE_PATH = ".logs/"
HOSTING__ACCESS_LOG_FILE = "access.log"
HOSTING__ERROR_LOG_FILE = "error.log"

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


class AbstractHostingService(models.Model):
    class Meta:
        abstract = True

    def get_service_type(self):
        """
        Must be implemented in derived classes
        """
        raise NotImplementedError

    def get_id(self):
        return u"%s%s" % (self.get_service_type(), self.pk)


class Domain(models.Model):
    domain = models.CharField(max_length=255, unique=True)
    owner = models.ForeignKey(User,
                              related_name='domains',
                              on_delete=models.PROTECT)

    def clean(self):
        netloc = urlparse('http://' + self.domain)[1].lower()
        if netloc is None or netloc == '':
            raise ValidationError('Invalid domain: %s' % self.domain)

            # todo: validate netloc
            # todo: xn-- domains
            # todo: trailing dot at the end of domain (technically valid)

    def __unicode__(self):
        return self.domain


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
    workers_per_host = models.PositiveSmallIntegerField()

    def __unicode__(self):
        return self.name


class DjangoHostingService(AbstractHostingService):
    owner = models.ForeignKey(
        User,
        related_name='django_services',
        on_delete=models.PROTECT
    )
    tariff = models.ForeignKey(DjangoHostingTariff, on_delete=models.PROTECT)
    start_at = models.DateTimeField()
    end_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    python_version = models.ForeignKey(PythonVersion, on_delete=models.PROTECT)
    django_version = models.ForeignKey(DjangoVersion, on_delete=models.PROTECT)
    server = models.ForeignKey(DjangoHostingServer, on_delete=models.PROTECT)
    status = models.CharField(max_length=1,
                              choices=HOSTING_SERVICE_STATUS_CHOICES,
                              default=HOSTING_SERVICE_DEPLOY_IN_PROGRESS)
    domain = models.ForeignKey(Domain, on_delete=models.PROTECT)

    django_static_path = models.CharField(max_length=255, default='static',
                                          null=True, blank=True)
    django_static_url = models.CharField(max_length=255, default='/static/',
                                         null=True, blank=True)
    django_media_path = models.CharField(max_length=255, default='media',
                                         null=True, blank=True)
    django_media_url = models.CharField(max_length=255, default='/media/',
                                        null=True, blank=True)

    settings_module = models.CharField(max_length=255, default='settings')
    wsgi_module = models.CharField(max_length=255, null=True, blank=True)
    requirements_file = models.CharField(max_length=255, null=True, blank=True)

    def clean(self):
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

        if self.django_static_path is not None:
            if not is_path_secure(self.django_static_path):
                raise ValidationError(
                    'Django static path must be absolute and '
                    'contain only these characters: a-zA-Z0-9-_./'
                )

        if self.django_media_path is not None:
            if not is_path_secure(self.django_media_path):
                raise ValidationError(
                    'Django media path must be absolute and '
                    'contain only these characters: a-zA-Z0-9-_./'
                )

        if self.django_static_url is not None:
            if not self.django_static_url.startswith('/') or \
                    not self.django_static_url.endswith('/'):
                raise ValidationError(
                    'Django static url must begin and end with a slash'
                )
            if not is_path_secure(self.django_static_url):
                raise ValidationError(
                    'Django static url must be absolute and '
                    'contain only these characters: a-zA-Z0-9-_./'
                )

        if self.django_media_url is not None:
            if not self.django_media_url.startswith('/') or \
                    not self.django_media_url.endswith('/'):
                raise ValidationError(
                    'Django media url must begin and end with a slash'
                )
            if not is_path_secure(self.django_media_url):
                raise ValidationError(
                    'Django media url must be absolute and '
                    'contain only these characters: a-zA-Z0-9-_./'
                )

        if self.settings_module:
            if not is_valid_python_module(self.settings_module):
                raise ValidationError(
                    'Invalid python module: %s' % self.settings_module
                )

        if self.wsgi_module:
            if not is_valid_python_module(self.wsgi_module):
                raise ValidationError(
                    'Invalid python module: %s' % self.wsgi_module
                )

        if self.requirements_file:
            if not is_path_secure(self.requirements_file):
                raise ValidationError(
                    'Invalid requirements file: %s' % self.requirements_file
                )

    def __unicode__(self):
        def get_status(status):
            if status == HOSTING_SERVICE_ACTIVE:
                return u'ACTIVE'
            if status == HOSTING_SERVICE_DEPLOY_IN_PROGRESS:
                return u'DEPLOY_IN_PROGRESS'
            if status == HOSTING_SERVICE_ACTIVE_TEST:
                return u'ACTIVE_TEST'
            if status == HOSTING_SERVICE_BLOCKED:
                return u'BLOCKED'
            if status == HOSTING_SERVICE_EXPIRED:
                return u'EXPIRED'

        s = u"[%s] %s at %s" % (
            get_status(self.status),
            self.get_id(),
            self.server.hostname
        )
        return s

    def get_access_log_file(self):
        return "%s%s%s" % (
            self.home_path,
            HOSTING__LOG_RELATIVE_PATH,
            HOSTING__ACCESS_LOG_FILE
        )

    def get_error_log_file(self):
        return "%s%s%s" % (
            self.home_path,
            HOSTING__LOG_RELATIVE_PATH,
            HOSTING__ERROR_LOG_FILE
        )

    def get_django_static_path(self):
        return os.path.join(self.home_path, self.django_static_path)

    def get_django_media_path(self):
        return os.path.join(self.home_path, self.django_media_path)

    def is_deployed(self):
        return self.status != HOSTING_SERVICE_DEPLOY_IN_PROGRESS

    def get_service_type(self):
        return 'django'

    def get_www_user(self):
        return 'www-%s' % self.get_id()

    def get_www_group(self):
        return self.get_www_user()

    def is_ready_to_deploy(self):
        return True

    def get_home_path(self):
        return "%s%s/" % (HOSTING__VIRTUALENVS_PATH, self.get_id())

    def get_virtualenv_path(self):
        return "%s%s/" % (HOSTING__VIRTUALENVS_PATH, self.get_id())

    def get_log_path(self):
        return "%s%s/" % (self.get_home_path(), HOSTING__LOG_RELATIVE_PATH)


@receiver(signals.post_save, sender=DjangoHostingService)
def enqueue_deploy_django_hosting_service(sender, instance, **kwargs):
    """
    @type instance DjangoHostingService
    """
    if instance.is_ready_to_deploy():
        from tasks import deploy_django_hosting_service

        deploy_django_hosting_service.apply_async(
            (instance,)
        )
