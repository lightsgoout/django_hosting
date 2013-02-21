from django import forms
from django.contrib.auth import login
from registration.backends.default import DefaultBackend
from registration.forms import RegistrationForm


def order_fields(*field_list):
    def decorator(form):
        original_init = form.__init__

        def init(self, *args, **kwargs):
            original_init(self, *args, **kwargs)
            for field in field_list[::-1]:
                self.fields.insert(0, field, self.fields.pop(field))

        form.__init__ = init
        return form

    return decorator


class UserRegistrationBackend(DefaultBackend):
    def register(self, request, **kwargs):
        kwargs['username'] = kwargs['email']
        return super(UserRegistrationBackend, self).register(request, **kwargs)

    def activate(self, request, activation_key):
        user = super(UserRegistrationBackend, self).activate(request,
                                                             activation_key)
        login(request, user)
        return user


@order_fields('first_name', 'last_name')
class UserRegistrationForm(RegistrationForm):
    first_name = forms.CharField(max_length=255, label="First name")
    last_name = forms.CharField(max_length=255, label="Last name")
    username = forms.CharField(widget=forms.HiddenInput, required=False)
