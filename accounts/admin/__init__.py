from django.contrib import admin
from django.contrib.auth.models import User
from accounts.admin.user import ExtendedUserAdmin

admin.site.unregister(User)
admin.site.register(User, ExtendedUserAdmin)
