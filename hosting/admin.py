from django.contrib import admin
from hosting.models import DjangoHostingAccount, DjangoHostingService, DjangoHostingTariff

admin.site.register(DjangoHostingAccount)
admin.site.register(DjangoHostingTariff)
admin.site.register(DjangoHostingService)
