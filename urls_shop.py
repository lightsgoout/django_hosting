from django.conf.urls import patterns, url
import shop.views


urlpatterns = patterns(
    '',
    url(r'^$',
        shop.views.landing,
        name='landing'),
)
