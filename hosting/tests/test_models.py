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

    @raises(ValidationError)
    def test_invalid_settings_module(self):
        """
        Test settings module validation
        """
        self.service.settings_module = '../../settings.py'
        self.service.full_clean()

    def test_valid_settings_module(self):
        """
        Test valid settings cases
        """
        self.service.settings_module = 'settings'
        self.service.full_clean()
        self.service.settings_module = 'settings.py'
        self.service.full_clean()
        self.service.settings_module = 'settings.production'
        self.service.full_clean()

    @raises(ValidationError)
    def test_invalid_wsgi_module(self):
        """
        Test wsgi module validation
        """
        self.service.wsgi_module = '../../wsgi.py'
        self.service.full_clean()

    def test_valid_wsgi_module(self):
        """
        Test valid wsgi cases
        """
        self.service.wsgi_module = 'wsgi'
        self.service.full_clean()
        self.service.wsgi_module = 'wsgi.py'
        self.service.full_clean()
        self.service.wsgi_module = 'deploy.wsgi'
        self.service.full_clean()

    @raises(ValidationError)
    def test_invalid_requirements_file(self):
        """
        Test requirements file validation
        """
        self.service.requirements_file = '../requirements.txt'
        self.service.full_clean()

    def test_valid_requirements_cases(self):
        """
        Test valid requirements cases
        """
        self.service.requirements_file = 'requirements.txt'
        self.service.full_clean()
        self.service.requirements_file = 'deploy/requirements.txt'
        self.service.full_clean()
