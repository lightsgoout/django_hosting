from django.test import TestCase
from backend.tests import fixtures


class TestDjangoVersion(TestCase):
    def test_is_python_version_supported(self):
        python_version = fixtures.create_python_version()
        django_version = fixtures.create_django_version(
            supported_python_versions=[python_version]
        )
        self.assertTrue(django_version.is_python_version_supported(
            python_version
        ))

        python_24 = fixtures.create_python_version(version_family="2.4.x")
        self.assertFalse(django_version.is_python_version_supported(
            python_24
        ))


