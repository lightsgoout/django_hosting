from django.conf.urls import patterns, url, include
import panel.views


urlpatterns = patterns(
    '',
    url(r'^$',
        panel.views.index,
        name='index'),
    url(r'^accounts/', include('registration.backends.default.urls')),
)
