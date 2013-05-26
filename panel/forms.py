from django.contrib.auth.models import User
from django.forms import ModelForm
from accounts.models import DjangoAccount


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


