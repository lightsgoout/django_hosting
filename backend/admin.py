from django.contrib import admin
from backend.models import PythonVersion, DjangoVersion

admin.site.register(PythonVersion)
admin.site.register(DjangoVersion)
