from os import mkdir
import os
import errno

from celery import task, chain
from setuptools.command.easy_install import chmod

from hosting.models import HOSTING__HOME_PATH, HOSTING__VIRTUALENVS_PATH, HOSTING__LOG_RELATIVE_PATH


@task()
def deploy_django_hosting_service(service):
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
    try:
        mkdir(service.home_path, mode=0770)
    except OSError as exc:
        if exc.errno == errno.EEXIST and os.path.isdir(service.home_path):
            chmod(service.home_path, mode=0770)
        else:
            raise


@task()
def create_hosting_log_dir(service, *args, **kwargs):
    log_dir = "%s%s" % (service.home_path, HOSTING__LOG_RELATIVE_PATH)
    try:
        mkdir(log_dir, mode=0770)
    except OSError as exc:
        if exc.errno == errno.EEXIST and os.path.isdir(log_dir):
            chmod(log_dir, mode=0770)
        else:
            raise


@task()
def create_hosting_virtualenv(service, *args, **kwargs):
    try:
        mkdir(service.virtualenv_path, mode=0770)
    except OSError as exc:
        if exc.errno == errno.EEXIST and os.path.isdir(service.home_path):
            chmod(service.virtualenv_path, mode=0770)
        else:
            raise


@task()
def create_django_uwsgi_config(service, *args, **kwargs):
    config = "[uwsgi]\n"
    config += "chdir = %s%%n\n" % HOSTING__HOME_PATH
    config += "workers = %d\n" % service.account.tariff.workers_per_host
    config += "harakiri = %d\n" % service.account.tariff.cpu_per_process
    config += "limit-as = %d\n" % service.account.tariff.ram_per_process
    config += "limit-nproc = 0\n"
    config += "master = false\n"
    config += "socket = /tmp/%n.sock\n"
    config += "virtualenv = %s%%n\n" % HOSTING__VIRTUALENVS_PATH
    #config += "env = DJANGO_SETTINGS_MODULE=%n.settings\n"
    #config += "module = django.core.handlers.wsgi:WSGIHandler()\n"


@task()
def create_nginx_config(service, *args, **kwargs):
    config = "server {\n"
    config += "listen 80;\n"
    config += "server_name %s;\n" % service.domain
    config += "access_log %s;\n" % service.get_access_log_file()
    config += "error_log %s;\n" % service.get_error_log_file()
    config += "\n"
    config += "location / {\n"
    config += "uwsgi_pass unix:/tmp/%s.sock\n;" % service.pk
    config += "include /etc/nginx/uwsgi_params;\n"
    config += "}\n"
    config += "\n"
    if service.django_static_url is not None:
        config += "location %s {\n" % service.django_static_url
        config += "root %s;\n" % service.get_django_static_path()
        config += "}\n"
    if service.django_media_url is not None:
        config += "location %s {\n" % service.django_media_url
        config += "root %s;\n" % service.get_django_media_path()
        config += "}\n"



