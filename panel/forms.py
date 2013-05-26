from django.contrib.auth.models import User
from django.forms import ModelForm
from accounts.models import DjangoAccount
from hosting.models import DjangoHostingService


class AccountForm(ModelForm):
    class Meta:
        model = DjangoAccount
        exclude = (
            'user',
            'django_tariff',
        )


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'email',
        )
        readonly_fields = (
            'email',
        )


class DjangoHostingServiceForm(ModelForm):
    class Meta:
        model = DjangoHostingService
        fields = (
            'python_version',
            'django_version',
            'domain',
            'django_static_path',
            'django_static_url',
            'django_media_path',
            'django_media_url',
            'settings_module',
            'wsgi_module',
            'requirements_file',
        )
