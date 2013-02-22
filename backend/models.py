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


class DjangoHostingServer(models.Model):
    hostname = models.CharField(max_length=255, unique=True)
    supported_python_versions = models.ManyToManyField(PythonVersion)
    is_published = models.BooleanField(default=True)
