from django.db import models
from hosting.models import DjangoHostingService


class GithubSettings(models.Model):
    hosting = models.OneToOneField(DjangoHostingService, related_name='github')
    login = models.CharField(max_length=128, unique=True)
    password = models.CharField(max_length=255)
    path = models.CharField(max_length=511, unique=True)
