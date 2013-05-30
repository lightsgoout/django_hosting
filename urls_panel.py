from django.conf.urls import patterns, url, include
from panel.service_wizard import FORMS, DjangoServiceWizard
import panel.views

urlpatterns = patterns(
    '',
    url(r'^$',
        panel.views.index,
        name='panel_index'),
    url(r'^services/$',
        panel.views.services,
        name='panel_services'),
    url(r'^services/create/$',
        DjangoServiceWizard.as_view(FORMS),
        name='panel_service_create'),
    url(r'^settings/account/$',
        panel.views.settings_account,
        name='panel_settings_account'),
    url(r'^settings/billing/$',
        panel.views.settings_billing,
        name='panel_settings_billing'),
    url(r'^settings/password/$',
        panel.views.settings_password,
        name='panel_settings_password'),
    url(r'^accounts/', include('registration.backends.default.urls')),
)

