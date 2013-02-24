from django.db import models


class PythonVersion(models.Model):
    version_family = models.CharField(max_length=15, unique=True)
    is_stable = models.BooleanField(default=True)
    is_discontinued = models.BooleanField(default=False)
    is_published = models.BooleanField(default=True)

    def __unicode__(self):
        return "Python %s" % self.version_family


class PythonBasedEntity(object):
    def is_python_version_supported(self, python_version):
        return self.__class__.objects.filter(
            supported_python_versions__version_family=
            python_version.version_family
        ).count() > 0


class DjangoVersion(models.Model, PythonBasedEntity):
    version_family = models.CharField(max_length=15, unique=True)
    is_stable = models.BooleanField(default=True)
    is_discontinued = models.BooleanField(default=False)
    is_published = models.BooleanField(default=True)
    supported_python_versions = models.ManyToManyField(PythonVersion)

    def __unicode__(self):
        return "Django %s" % self.version_family


class DjangoHostingServer(models.Model, PythonBasedEntity):
    hostname = models.CharField(max_length=255, unique=True)
    supported_python_versions = models.ManyToManyField(PythonVersion)
    is_published = models.BooleanField(default=True)

    def __unicode__(self):
        return "Django server %s" % self.hostname
