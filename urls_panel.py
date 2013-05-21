from django.conf.urls import patterns, url, include
import panel.views


urlpatterns = patterns(
    '',
    url(r'^$',
        panel.views.index,
        name='panel_index'),
    url(r'^services/$',
        panel.views.services,
        name='panel_services'),
    url(r'^accounts/', include('registration.backends.default.urls')),
)
