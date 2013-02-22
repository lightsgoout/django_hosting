import datetime
from django.contrib.auth.models import User
from backend.tests.fixtures import create_python_version, create_django_version, create_django_hosting_server
from hosting.models import DjangoHostingAccount, DjangoHostingTariff, DjangoHostingService


def create_client(email="test@test.ru", is_active=True, first_name='Test',
                  last_name='Testovich'):
    return User.objects.create(
        username=email,
        email=email,
        is_active=is_active,
        first_name=first_name,
        last_name=last_name,
    )


def create_django_hosting_tariff(name="Django fake tariff", is_published=True,
                                 vhost_count=1, has_backup=True):
    return DjangoHostingTariff.objects.create(
        name=name,
        is_published=is_published,
        disk_quota=2048,
        inode_quota=2048000,
        cpu_per_process=30,
        ram_per_process=64,
        file_descriptors_per_process=100,
        vhost_count=vhost_count,
        has_backup=has_backup
    )


def create_django_hosting_account(tariff=None, client=None, start_at=None,
                                  end_at=None, status='T'):
    if tariff is None:
        tariff = create_django_hosting_tariff()
    if client is None:
        client = create_client()
    if start_at is None:
        start_at = datetime.datetime.now()
    if end_at is None:
        end_at = '2025-01-01'

    return DjangoHostingAccount.objects.create(
        tariff=tariff,
        client=client,
        start_at=start_at,
        end_at=end_at,
        status=status,
    )


def create_django_hosting_service(account=None, python_version=None,
                                  django_version=None, server=None,
                                  virtualenv_path="/.virtualenvs/10001",
                                  home_path="/.hosting/10001",
                                  status='T'):
    if account is None:
        account = create_django_hosting_account()
    if python_version is None:
        python_version = create_python_version()
    if django_version is None:
        django_version = create_django_version(supported_python_versions=[
            python_version
        ])
    if server is None:
        server = create_django_hosting_server(supported_python_versions=[
            python_version
        ])

    return DjangoHostingService.objects.create(
        account=account,
        python_version=python_version,
        django_version=django_version,
        virtualenv_path=virtualenv_path,
        home_path=home_path,
        server=server,
        status=status
    )

