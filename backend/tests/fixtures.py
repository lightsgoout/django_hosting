from backend.models import PythonVersion, DjangoVersion, DjangoHostingServer


def create_python_version(version_family="2.7.x", is_stable=True,
                          is_discontinued=False, is_published=True):
    return PythonVersion.objects.create(
        version_family=version_family,
        is_stable=is_stable,
        is_discontinued=is_discontinued,
        is_published=is_published
    )


def create_django_version(version_family="1.5.x", is_stable=True,
                          is_discontinued=False, is_published=True,
                          supported_python_versions=()):
    django = DjangoVersion.objects.create(
        version_family=version_family,
        is_stable=is_stable,
        is_discontinued=is_discontinued,
        is_published=is_published
    )
    if len(supported_python_versions):
        django.supported_python_versions.add(*supported_python_versions)
    else:
        python1 = create_python_version(version_family="2.7.x")
        python2 = create_python_version(version_family="2.6.x")
        django.supported_python_versions.add(python1, python2)

    return django


def create_django_hosting_server(hostname="t00.testserver.com",
                                 is_published=True,
                                 supported_python_versions=()):
    server = DjangoHostingServer.objects.create(
        hostname=hostname,
        is_published=is_published,
    )
    if len(supported_python_versions):
        server.supported_python_versions.add(*supported_python_versions)
    else:
        python1 = create_python_version(version_family="2.7.x")
        python2 = create_python_version(version_family="2.6.x")
        server.supported_python_versions.add(python1, python2)

    return server
