from django.conf import settings
from django.conf.urls import patterns, include, url


urlpatterns = patterns('')

if settings.ENDPOINT_MODE == 'SHOP':
    urlpatterns.extend([
        url(r'', include('urls_shop'))
    ])

elif settings.ENDPOINT_MODE == 'STAFF':
    from django.contrib import admin

    admin.autodiscover()
    urlpatterns.extend([
        url(r'', include(admin.site.urls)),
    ])

elif settings.ENDPOINT_MODE == 'PANEL':
    urlpatterns.extend([
        url(r'', include('urls_panel'))
    ])



