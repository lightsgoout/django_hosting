from django.contrib.auth.decorators import login_required
from django.template.response import TemplateResponse
from hosting.models import DjangoHostingService
from panel.forms import AccountForm, UserForm, DjangoHostingServiceForm


@login_required
def index(request, extra_context=None):
    django_services = DjangoHostingService.objects.filter(
        owner=request.user
    )

    vhosts_available = request.user.account.django_tariff.vhost_count
    vhosts_total = len(django_services)
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
        'django_tariff': request.user.account.django_tariff,
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
    form = DjangoHostingServiceForm()

    return TemplateResponse(request, 'panel/services.html', context={
        'django_services': django_services,
        'pointer': 'services',
        'form': form
    })


@login_required
def settings_account(request):
    if request.method == 'POST':
        account_form = AccountForm(request.POST, instance=request.user.account)
        user_form = UserForm(request.POST, instance=request.user)
        if account_form.is_valid():
            account_form.save()
        if user_form.is_valid():
            user_form.save()
    else:
        account_form = AccountForm(instance=request.user.account)
        user_form = UserForm(instance=request.user)

    return TemplateResponse(request, 'panel/settings/account.html', context={
        'forms': (account_form, user_form)
    })


@login_required
def settings_billing(request):
    return TemplateResponse(request, 'panel/settings/billing.html', context={
    })

