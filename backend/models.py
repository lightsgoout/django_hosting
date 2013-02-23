from django.db import models


class PythonVersion(models.Model):
    version_family = models.CharField(max_length=15, unique=True)
    is_stable = models.BooleanField(default=True)
    is_discontinued = models.BooleanField(default=False)
    is_published = models.BooleanField(default=True)


class DjangoVersion(models.Model):
    version_family = models.CharField(max_length=15, unique=True)
    is_stable = models.BooleanField(default=True)
    is_discontinued = models.BooleanField(default=False)
    is_published = models.BooleanField(default=True)
    supported_python_versions = models.ManyToManyField(PythonVersion)

    def is_python_version_supported(self, python_version):
        return DjangoVersion.objects.filter(
            supported_python_versions__version_family=
            python_version.version_family
        ).count() > 0


class DjangoHostingServer(models.Model):
    hostname = models.CharField(max_length=255, unique=True)
    supported_python_versions = models.ManyToManyField(PythonVersion)
    is_published = models.BooleanField(default=True)
