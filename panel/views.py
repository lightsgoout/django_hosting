from django.contrib.auth.decorators import login_required
from django.template.response import TemplateResponse
from hosting.models import DjangoHostingService


@login_required
def index(request, extra_context=None):
    django_services = DjangoHostingService.objects.filter(
        owner=request.user
    )

    return TemplateResponse(request, 'panel/home.html', context={
        'django_services': django_services,
        'pointer': 'home',
        'django_tariff': request.user.django_account.django_tariff,
        'django_vhosts_total': len(django_services),
        'django_vhosts_available': request.user.django_account.django_tariff.vhost_count
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

