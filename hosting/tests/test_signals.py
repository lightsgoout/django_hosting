from django.test import TestCase
from hosting.tests import fixtures


class TestSignals(TestCase):
    def _fix_up(self):
        account = fixtures.create_django_hosting_account(status='T')
        python_version = fixtures.create_python_version()
        django_version = fixtures.create_django_version(
            supported_python_versions=[python_version]

        )
        django_server = fixtures.create_django_hosting_server(
            supported_python_versions=[python_version]
        )
        fixtures.create_django_hosting_service(
            account=account,
            python_version=python_version,
            django_version=django_version,
            server=django_server,
        )
        fixtures.create_django_hosting_service(
            account=account,
            python_version=python_version,
            django_version=django_version,
            server=django_server,
        )
        return account






