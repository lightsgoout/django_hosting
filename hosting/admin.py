from django.contrib import admin
from hosting.models import DjangoHostingService, \
    DjangoHostingTariff, Domain

admin.site.register(DjangoHostingTariff)
admin.site.register(DjangoHostingService)
admin.site.register(Domain)
