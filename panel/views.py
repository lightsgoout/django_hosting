from django.contrib.auth.decorators import login_required
from django.template.response import TemplateResponse
from hosting.models import DjangoHostingService


@login_required
def index(request, extra_context=None):
    django_services = DjangoHostingService.objects.filter(
        owner=request.user
    )

    return TemplateResponse(request, 'panel/index.html', context={
        'django_services': django_services,
    })
