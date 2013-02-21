from django.template.response import TemplateResponse


def landing(request, extra_context=None):
    return TemplateResponse(request, 'shop/landing.html')


def signup_complete(request, extra_context=None):
    pass
