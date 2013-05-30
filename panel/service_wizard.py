from django import forms
from django.contrib.formtools.wizard.views import SessionWizardView
from django.forms import RadioSelect, CheckboxSelectMultiple


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
    ('pip_requirements', 'Install packages listed in requirements.txt')
)

POST_INSTALL_CHOICES = (
    ('syncdb', 'Run syncdb command'),
)


class SourceForm(forms.Form):
    source = forms.ChoiceField(widget=RadioSelect, choices=SOURCES_CHOICES)
    vcs_url = forms.CharField(max_length=255, required=False)


class DatabaseForm(forms.Form):
    database = forms.ChoiceField(widget=RadioSelect, choices=DATABASE_CHOICES)
    dsn_url = forms.CharField(max_length=255, required=False)


class SpecialOptionsForm(forms.Form):
    choices = forms.ChoiceField(
        widget=CheckboxSelectMultiple,
        choices=SPECIAL_OPTION_CHOICES
    )


class PostInstallForm(forms.Form):
    choices = forms.ChoiceField(
        widget=CheckboxSelectMultiple,
        choices=POST_INSTALL_CHOICES,
    )


FORMS = [("source", SourceForm),
         ("database", DatabaseForm),
         ("special", SpecialOptionsForm),
         ("post_install", PostInstallForm)]

TEMPLATES = {"source": "panel/service_wizard/source.html",
             "database": "panel/service_wizard/database.html",
             "special": "panel/service_wizard/special.html",
             "post_install": "panel/service_wizard/post_install.html"}


class DjangoServiceWizard(SessionWizardView):
    def get_template_names(self):
        return [TEMPLATES[self.steps.current]]

    def done(self, form_list, **kwargs):
        pass
