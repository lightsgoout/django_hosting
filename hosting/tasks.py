import os
import errno

from celery import task, chain
from celery.utils.log import get_task_logger

from hosting.models import HOSTING__HOME_PATH, HOSTING__VIRTUALENVS_PATH, \
    HOSTING__LOG_RELATIVE_PATH, HOSTING__NGINX_CONFIG_PATH

logger = get_task_logger(__name__)


@task()
def deploy_django_hosting_service(service, *args, **kwargs):
    """
    @type service DjangoHostingService
    """

    c = chain(
        create_hosting_home_dir.s(service),
        create_hosting_log_dir.s(service),
        create_hosting_virtualenv.s(service),
        create_django_uwsgi_config.s(service),
        create_nginx_config.s(service),
    )
    c()


@task()
def create_hosting_home_dir(service, *args, **kwargs):
    """
    @type service DjangoHostingService
    """
    logger.info('[%s] Creating hosting home dir...' % service.get_id())
    try:
        os.mkdir(service.home_path, 0770)
    except OSError as exc:
        if exc.errno == errno.EEXIST and os.path.isdir(service.home_path):
            os.chmod(service.home_path, 0770)
        else:
            raise

    return service


@task()
def create_hosting_log_dir(service, *args, **kwargs):
    """
    @type service DjangoHostingService
    """
    logger.info('[%s] Creating hosting log dir...' % service.get_id())
    log_dir = "%s%s" % (service.home_path, HOSTING__LOG_RELATIVE_PATH)
    try:
        os.mkdir(log_dir, 0770)
    except OSError as exc:
        if exc.errno == errno.EEXIST and os.path.isdir(log_dir):
            os.chmod(log_dir, 0770)
        else:
            raise

    return service


@task()
def create_hosting_virtualenv(service, *args, **kwargs):
    """
    @type service DjangoHostingService
    """
    logger.info('[%s] Creating hosting virtualenv...' % service.get_id())
    try:
        os.mkdir(service.virtualenv_path, 0770)
    except OSError as exc:
        if exc.errno == errno.EEXIST and os.path.isdir(service.home_path):
            os.chmod(service.virtualenv_path, 0770)
        else:
            raise

    return service


@task()
def create_django_uwsgi_config(service, *args, **kwargs):
    """
    @type service DjangoHostingService
    """
    logger.info('[%s] Creating django uwsgi config...' % service.get_id())
    config = "[uwsgi]\n"
    config += "protocol = uwsgi\n"
    config += "master = true\n"
    config += "processes = %s\n" % service.server.core_count
    config += "socket = /tmp/%s.sock\n" % service.get_id()
    config += "chmod-socket = 666\n"
    config += "vhost = true\n"
    config += "no-site = true\n"
    config += "uid = %s\n" % service.get_www_user()
    config += "gid = %s\n" % service.get_www_group()
    config += "module = django.core.handlers.wsgi:WSGIHandler()\n"
    config += "env = DJANGO_SETTINGS_MODULE=%s\n" % service.settings_module
    config += "virtualenv = %s%s\n" % (
        HOSTING__VIRTUALENVS_PATH, service.get_id()
    )
    config += "chdir = %s%s\n" % (HOSTING__HOME_PATH, service.get_id())

    # todo: add pythonpath

    config_path = "%s%s.conf" % (HOSTING__NGINX_CONFIG_PATH, service.get_id())
    with open(config_path, 'w') as config_file:
        config_file.write(config)

    return service


@task()
def create_nginx_config(service, *args, **kwargs):
    """
    @type service DjangoHostingService
    """
    logger.info('[%s] Creating nginx config...' % service.get_id())
    config = "server {\n"
    config += "\tlisten 80;\n"
    config += "\tserver_name %s;\n" % service.domain
    config += "\taccess_log %s;\n" % service.get_access_log_file()
    config += "\terror_log %s;\n" % service.get_error_log_file()
    config += "\n"
    config += "\tlocation / {\n"
    config += "\t\tuwsgi_pass unix:/tmp/%s.sock;\n" % service.get_id()
    config += "\t\tinclude /etc/nginx/uwsgi_params;\n"
    config += "\t}\n"
    config += "\n"
    if service.django_static_url is not None:
        config += "\tlocation %s {\n" % service.django_static_url
        config += "\t\troot %s;\n" % service.get_django_static_path()
        config += "\t}\n"
    if service.django_media_url is not None:
        config += "\tlocation %s {\n" % service.django_media_url
        config += "\t\troot %s;\n" % service.get_django_media_path()
        config += "\t}\n"
    config += "}\n"

    config_path = "%s%s.conf" % (HOSTING__NGINX_CONFIG_PATH, service.get_id())
    with open(config_path, 'w') as config_file:
        config_file.write(config)

    return service
