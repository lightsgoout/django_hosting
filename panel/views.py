from django.contrib.auth.decorators import login_required
from django.template.response import TemplateResponse
from hosting.models import DjangoHostingService


@login_required
def index(request, extra_context=None):
    django_services = DjangoHostingService.objects.filter(
        owner=request.user
    )

    vhosts_available = 4#request.user.django_account.django_tariff.vhost_count
    vhosts_total = len(django_services)
    vhosts_total = 3
    usage_bar_level = 'ok'
    if not vhosts_available:
        usage_bar_value = 0
    else:
        usage_bar_value = int(round(100 / vhosts_available * vhosts_total))
        if usage_bar_value >= 100:
            usage_bar_level = 'danger'
            usage_bar_value = 100

    return TemplateResponse(request, 'panel/home.html', context={


        'django_services': django_services,
        'pointer': 'home',
        'django_tariff': request.user.django_account.django_tariff,
        'django_vhosts_total': vhosts_total,
        'django_vhosts_available': vhosts_available,
        'usage_bar_value': usage_bar_value,
        'usage_bar_level': usage_bar_level
    })


@login_required
def services(request):
    django_services = DjangoHostingService.objects.filter(
        owner=request.user
    )

    return TemplateResponse(request, 'panel/services.html', context={
        'django_services': django_services,
        'pointer': 'services'
    })


@login_required
def settings_account(request):
    return TemplateResponse(request, 'panel/settings/account.html', context={
    })


@login_required
def settings_billing(request):
    return TemplateResponse(request, 'panel/settings/billing.html', context={
    })

