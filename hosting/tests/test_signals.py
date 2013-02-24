from django.test import TestCase
from hosting.models import DjangoHostingService, HOSTING_ACCOUNT_BLOCKED, \
    HOSTING_SERVICE_DEPLOY_IN_PROGRESS, HOSTING_ACCOUNT_ACTIVE, \
    HOSTING__VIRTUALENVS_PATH, HOSTING__HOME_PATH
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
            virtualenv_path='test1',
            home_path='test1',
            server=django_server,
        )
        fixtures.create_django_hosting_service(
            account=account,
            python_version=python_version,
            django_version=django_version,
            virtualenv_path='test2',
            home_path='test2',
            server=django_server,
        )
        return account

    def test_update_django_hosting_service_status_keep_deploying(self):
        """
        Ensure service's DEPLOY_IN_PROGRESS status not changes, if account's
        one is set to ACTIVE, or TEST_ACTIVE
        """
        account = self._fix_up()
        # prepare services, like they're already deploying
        for service in DjangoHostingService.objects.filter(account=account):
            service.status = HOSTING_SERVICE_DEPLOY_IN_PROGRESS
            service.save()
        account.status = HOSTING_ACCOUNT_ACTIVE
        account.save()
        for service in DjangoHostingService.objects.filter(account=account):
            self.assertEqual(
                HOSTING_SERVICE_DEPLOY_IN_PROGRESS,
                service.status
            )

    def test_update_django_hosting_service_status(self):
        """
        Ensure services are set to BLOCKED or EXPIRED if account is BLOCKED
        or EXPIRED
        """
        account = self._fix_up()
        account.status = HOSTING_ACCOUNT_BLOCKED
        account.save()
        for service in DjangoHostingService.objects.filter(account=account):
            self.assertEqual(account.status, service.status)

    def test_auto_populate_virtualenv_and_home_path(self):
        """
        Ensure service's virtualenv_path and home_path is auto-populated
        based on PK.
        """
        service = fixtures.create_django_hosting_service(
            virtualenv_path=None,
            home_path=None,
        )
        self.assertEqual(
            service.virtualenv_path,
            "%s%s" % (HOSTING__VIRTUALENVS_PATH, service.pk)
        )
        self.assertEqual(
            service.home_path,
            "%s%s" % (HOSTING__HOME_PATH, service.pk)
        )
