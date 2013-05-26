from django import forms
from django.forms import RadioSelect


SOURCES_CHOICES = (
    ('git', 'Clone project using git'),
    ('hg', 'Clone project using mercurial'),
    ('svn', 'Clone project using svn'),
    ('empty', 'Create empty django project'),
)

DATABASE_CHOICES = (
    ('mysql', 'Create new MySQL database'),
    ('pgsql', 'Create new PostgreSQL database'),
    ('dsn', 'Auto-connect to database using specified link'),
    ('form', 'Auto-connect to database using specified credentials'),
)

SPECIAL_OPTION_CHOICES = (
    ('pip', 'Install specified packages via pip'),
)

POST_INSTALL_CHOICES = (
    ('syncdb', 'Run syncdb command'),
)


class SourceForm(forms.Form):
    source = forms.ChoiceField(widget=RadioSelect, choices=SOURCES_CHOICES)


# FORMS = [("source", service_wizard.SourceForm),
#          ("paytype", myapp.forms.PaymentChoiceForm),
#          ("cc", myapp.forms.CreditCardForm),
#          ("confirmation", myapp.forms.OrderForm)]
