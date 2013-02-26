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

    @raises(ValidationError)
    def test_virtualenv_trailing_slash(self):
        """
        Ensure that virtualenv_path contains trailing slash
        """
        self.service.virtualenv_path = "/test"
        self.service.full_clean()

    @raises(ValidationError)
    def test_home_path_trailing_slash(self):
        """
        Ensure that home_path contains trailing slash
        """
        self.service.home_path = "/test"
        self.service.full_clean()

    @raises(ValidationError)
    def test_secure_django_static_path_absolute_path(self):
        """
        Ensure that relative django static path is not permitted
        """
        self.service.django_static_path = '../test'
        self.service.full_clean()

    @raises(ValidationError)
    def test_secure_django_static_path_special_symbols(self):
        """
        Ensure that only basic symbols are permitted for django static path
        """
        self.service.django_static_path = '$asd'
        self.service.full_clean()

    @raises(ValidationError)
    def test_secure_django_media_path_absolute_path(self):
        """
        Ensure that relative django media path is not permitted
        """
        self.service.django_media_path = '../test'
        self.service.full_clean()

    @raises(ValidationError)
    def test_secure_django_media_path_special_symbols(self):
        """
        Ensure that only basic symbols are permitted for django media path
        """
        self.service.django_media_path = '$asd'
        self.service.full_clean()

    @raises(ValidationError)
    def test_secure_django_static_url_absolute_path(self):
        """
        Ensure that relative django static url is not permitted
        """
        self.service.django_static_url = '/../test/'
        self.service.full_clean()

    @raises(ValidationError)
    def test_secure_django_static_url_special_symbols(self):
        """
        Ensure that only basic symbols are permitted for django static url
        """
        self.service.django_static_url = '/$asd/'
        self.service.full_clean()

    @raises(ValidationError)
    def test_secure_django_media_url_absolute_path(self):
        """
        Ensure that relative django media url is not permitted
        """
        self.service.django_media_url = '/../test/'
        self.service.full_clean()

    @raises(ValidationError)
    def test_secure_django_media_url_special_symbols(self):
        """
        Ensure that only basic symbols are permitted for django media url
        """
        self.service.django_media_url = '/$asd/'
        self.service.full_clean()




