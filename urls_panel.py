from django.conf.urls import patterns, url
import panel.views


urlpatterns = patterns(
    '',
    url(r'^$',
        panel.views.index,
        name='index'),
)
