from django.contrib import admin
from hosting.models import DjangoHostingAccount, DjangoHostingService, \
    DjangoHostingTariff, Domain

admin.site.register(DjangoHostingAccount)
admin.site.register(DjangoHostingTariff)
admin.site.register(DjangoHostingService)
admin.site.register(Domain)
