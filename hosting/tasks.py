import os
import errno

from celery import task, chain
from celery.utils.log import get_task_logger

from hosting.models import HOSTING__HOME_PATH, HOSTING__VIRTUALENVS_PATH, \
    HOSTING__NGINX_CONFIG_PATH, \
    HOSTING__NGINX_USER, HOSTING__UWSGI_CONFIG_PATH

logger = get_task_logger(__name__)


@task()
def deploy_django_hosting_service(service, *args, **kwargs):
    """
    @type service DjangoHostingService
    """
    os.chroot(service.get_home_path())
    c = chain(
        create_hosting_www_user.s(service),
        add_nginx_to_user_group.s(service),
        create_hosting_home_dir.s(service),
        create_hosting_log_dir.s(service),
        create_hosting_virtualenv.s(service),
        create_django_uwsgi_config.s(service),
        create_nginx_config.s(service),
        install_requirements.s(service),
    )
    c()


@task()
def create_hosting_www_user(service, *args, **kwargs):
    """
    @type service DjangoHostingService
    """
    logger.info('[%s] Creating hosting www user...' % service.get_id())
    os.system(
        'sudo useradd --home-dir %s --shell /usr/sbin/nologin --user-group %s' % (
            service.get_home_path(),
            service.get_www_user()
        )
    )
    return service


@task()
def add_nginx_to_user_group(service, *args, **kwargs):
    """
    @type service DjangoHostingService
    """
    logger.info('[%s] Adding nginx to user group...' % service.get_id())
    os.system(
        'sudo usermod -a -G %s %s' % (
            service.get_www_group(),
            HOSTING__NGINX_USER
        )
    )
    return service


@task()
def create_hosting_home_dir(service, *args, **kwargs):
    """
    @type service DjangoHostingService
    """
    logger.info('[%s] Creating hosting home dir...' % service.get_id())
    home_path = service.get_home_path()
    try:
        os.mkdir(home_path, 0770)
    except OSError as exc:
        if exc.errno == errno.EEXIST and os.path.isdir(home_path):
            os.chmod(home_path, 0770)
        else:
            raise

    return service


@task()
def create_hosting_log_dir(service, *args, **kwargs):
    """
    @type service DjangoHostingService
    """
    logger.info('[%s] Creating hosting log dir...' % service.get_id())
    log_dir = service.get_log_path()
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
    virtualenv_path = service.get_virtualenv_path()
    try:
        os.mkdir(virtualenv_path, 0770)
    except OSError as exc:
        if exc.errno == errno.EEXIST and os.path.isdir(virtualenv_path):
            os.chmod(virtualenv_path, 0770)
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
    if service.wsgi_module is not None:
        config += "module = %s\n" % service.wsgi_module
    else:
        config += "module = django.core.handlers.wsgi:WSGIHandler()\n"
    config += "env = DJANGO_SETTINGS_MODULE=%s\n" % service.settings_module
    config += "virtualenv = %s%s\n" % (
        HOSTING__VIRTUALENVS_PATH, service.get_id()
    )
    config += "chdir = %s%s\n" % (HOSTING__HOME_PATH, service.get_id())

    # todo: add pythonpath

    config_path = "%s%s/%s.conf" % (
        HOSTING__UWSGI_CONFIG_PATH,
        service.python_version.major_version,
        service.get_id()
    )
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

    config_path = "%s%s.conf" % (
        HOSTING__NGINX_CONFIG_PATH,
        service.get_id()
    )
    with open(config_path, 'w') as config_file:
        config_file.write(config)

    return service


@task()
def install_requirements(service, *args, **kwargs):
    """
    @type service DjangoHostingService
    """
    if service.requirements_file:
        if os.path.isfile(service.requirements_file):
            logger.info(
                "Installing requirements file: %s ..." % service.requirements_file
            )
            os.system(
                'sudo workon %s && pip install -r %s' % (
                    service.get_id(),
                    service.requirements_file
                )
            )

    return service
