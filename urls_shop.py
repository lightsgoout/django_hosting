from django.conf.urls import patterns, url, include
from registration.views import register
from shop.models import UserRegistrationForm
import shop.views


urlpatterns = patterns(
    '',
    url(r'^$',
        shop.views.landing,
        name='landing'),
    url(r'^accounts/register/$',
        register,
        {
            'backend': 'shop.models.UserRegistrationBackend',
            'form_class': UserRegistrationForm
        },
        name='registration_register'),
    url(r'^accounts/', include('registration.backends.default.urls')),
)
