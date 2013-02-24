from django.core.exceptions import ValidationError
from django.test import TestCase
from mock import Mock
from nose.tools import raises
from hosting.tests import fixtures


class TestDjangoHostingService(TestCase):
    service = None

    def setUp(self):
        self.service = fixtures.create_django_hosting_service()

    @raises(ValidationError)
    def test_django_python_support(self):
        """
        Test that selected django version supports selected python version
        """
        self.service.python_version = fixtures.create_python_version(
            version_family="1.1.x"
        )
        self.service.server.is_python_version_supported = Mock()
        self.service.full_clean()

    @raises(ValidationError)
    def test_server_python_support(self):
        """
        Test that selected server version supports selected python version
        """
        self.service.python_version = fixtures.create_python_version(
            version_family="1.1.x"
        )
        self.service.django_version.is_python_version_supported = Mock()
        self.service.full_clean()

    @raises(ValidationError)
    def test_server_must_be_published(self):
        """
        Ensure that django server is published
        """
        self.service.server.is_published = False
        self.service.full_clean()


