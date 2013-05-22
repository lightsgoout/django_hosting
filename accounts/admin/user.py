from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.models import BillingInformation, DjangoAccount


class BillingInformationInline(admin.StackedInline):
    model = BillingInformation
    can_delete = False


class DjangoAccountInline(admin.StackedInline):
    model = DjangoAccount
    can_delete = False


class ExtendedUserAdmin(UserAdmin):
    inlines = (
        BillingInformationInline,
        DjangoAccountInline,
    )
