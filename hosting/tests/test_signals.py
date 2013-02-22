from django.test import TestCase
from hosting.models import DjangoHostingService
from hosting.tests import fixtures


class TestSignals(TestCase):
    def test_update_django_hosting_service_status(self):
        """
        Ensure services are set to BLOCKED or EXPIRED if account is BLOCKED
        or EXPIRED
        """

        account = fixtures.create_django_hosting_account(status='T')
        python_version = fixtures.create_python_version()
        django_version = fixtures.create_django_version(
            supported_python_versions=[python_version]

        )
        django_server = fixtures.create_django_hosting_server(
            supported_python_versions=[python_version]
        )
        service1 = fixtures.create_django_hosting_service(
            account=account,
            python_version=python_version,
            django_version=django_version,
            virtualenv_path='test1',
            home_path='test1',
            server=django_server,
        )
        service2 = fixtures.create_django_hosting_service(
            account=account,
            python_version=python_version,
            django_version=django_version,
            virtualenv_path='test2',
            home_path='test2',
            server=django_server,
        )
        account.status = 'B'
        account.save()
        for service in DjangoHostingService.objects.filter(account=account):
            self.assertEqual(account.status, service.status)



