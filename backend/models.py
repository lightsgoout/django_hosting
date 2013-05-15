from django.db import models


class PythonVersion(models.Model):
    PYTHON_MAJOR_VERSIONS = (
        ('python2.4', 'python2.4'),
        ('python2.5', 'python2.5'),
        ('python2.6', 'python2.6'),
        ('python2.7', 'python2.7'),
        ('python3.0', 'python3.0'),
        ('python3.1', 'python3.1'),
        ('python3.2', 'python3.2'),
        ('python3.3', 'python3.3'),
    )

    version_family = models.CharField(max_length=15, unique=True)
    major_version = models.CharField(
        max_length=15,
        choices=PYTHON_MAJOR_VERSIONS
    )
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
    core_count = models.PositiveSmallIntegerField(default=1)

    def __unicode__(self):
        return "Django server %s" % self.hostname
