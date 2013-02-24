from django.contrib import admin
from backend.models import PythonVersion, DjangoVersion, DjangoHostingServer

admin.site.register(PythonVersion)
admin.site.register(DjangoVersion)
admin.site.register(DjangoHostingServer)
