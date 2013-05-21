import datetime
from django.contrib.auth.models import User
from django.test.utils import override_settings
from backend.tests.fixtures import create_python_version, \
    create_django_version, create_django_hosting_server
from hosting.models import DjangoHostingTariff, \
    DjangoHostingService, Domain


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
        has_backup=has_backup,
        workers_per_host=2
    )


def create_domain(domain=None, owner=None):
    import uuid

    uid = uuid.uuid4()
    if domain is None:
        domain = "test-%s" % uid.hex

    if owner is None:
        owner = create_client()

    d = Domain.objects.create(domain=domain, owner=owner)
    return d


@override_settings(BROKER_BACKEND='memory')
@override_settings(BROKER_URL='')
def create_django_hosting_service(tariff=None, owner=None, start_at=None,
                                  end_at=None, python_version=None,
                                  django_version=None, server=None,
                                  status='T', domain=None):
    if tariff is None:
        tariff = create_django_hosting_tariff()
    if owner is None:
        owner = create_client()
    if start_at is None:
        start_at = datetime.datetime.now()
    if end_at is None:
        end_at = '2025-01-01'
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
    if domain is None:
        domain = create_domain(owner=owner)

    return DjangoHostingService.objects.create(
        tariff=tariff,
        owner=owner,
        start_at=start_at,
        end_at=end_at,
        python_version=python_version,
        django_version=django_version,
        server=server,
        status=status,
        domain=domain,
    )
