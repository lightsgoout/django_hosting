from django.contrib.auth.decorators import login_required
from django.template.response import TemplateResponse
from hosting.models import DjangoHostingAccount, DjangoHostingService


@login_required
def index(request, extra_context=None):
    django_accounts = DjangoHostingAccount.objects.filter(client=request.user)
    django_services = DjangoHostingService.objects.filter(
        account__pk__in=[x.pk for x in django_accounts]
    )

    return TemplateResponse(request, 'panel/index.html', context={
        'django_accounts': django_accounts,
        'django_services': django_services,
    })
