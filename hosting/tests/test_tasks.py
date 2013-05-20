from django.test import TestCase
from django.test.utils import override_settings
from mock import patch
from hosting.tasks import create_hosting_www_user, add_nginx_to_user_group, \
    create_hosting_home_dir, create_hosting_log_dir, \
    create_hosting_virtualenv, create_django_uwsgi_config, \
    create_nginx_config, install_requirements
from hosting.tests import fixtures


@override_settings(BROKER_BACKEND='memory')
@override_settings(BROKER_URL='')
class TestDjangoHostingServiceDeploy(TestCase):
    service = None

    def setUp(self):
        self.service = fixtures.create_django_hosting_service()

    @patch('os.system')
    def test_create_hosting_www_user(self, system_mock):
        create_hosting_www_user(self.service)

    @patch('os.system')
    def test_add_nginx_to_user_group(self, system_mock):
        add_nginx_to_user_group(self.service)

    @patch('os.mkdir')
    @patch('os.chmod')
    @patch('os.path')
    def test_create_hosting_home_dir(self, os_path, os_chmod, os_mkdir):
        create_hosting_home_dir(self.service)

    @patch('os.mkdir')
    @patch('os.chmod')
    @patch('os.path')
    def test_create_hosting_log_dir(self, os_path, os_chmod, os_mkdir):
        create_hosting_log_dir(self.service)

    @patch('os.mkdir')
    @patch('os.chmod')
    @patch('os.path')
    def test_create_hosting_virtualenv(self, os_path, os_chmod, os_mkdir):
        create_hosting_virtualenv(self.service)

    @patch('__builtin__.open')
    def test_create_django_uwsgi_config(self, open_mock):
        create_django_uwsgi_config(self.service)

    @patch('__builtin__.open')
    def test_create_nginx_config(self, open_mock):
        create_nginx_config(self.service)

    @patch('os.system')
    def test_create_nginx_config(self, system_mock):
        install_requirements(self.service)
