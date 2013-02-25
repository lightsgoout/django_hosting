from os import mkdir
import os
import errno

from celery import task, chain
from setuptools.command.easy_install import chmod

from hosting.models import HOSTING__HOME_PATH, HOSTING__VIRTUALENVS_PATH


@task()
def deploy_django_hosting_service(service):
    c = chain(
        create_hosting_home_dir.s(service),
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
    pass


