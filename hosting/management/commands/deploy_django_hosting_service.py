from django.core.management.base import BaseCommand, CommandError
from hosting.models import DjangoHostingService
from hosting.tasks import deploy_django_hosting_service


class Command(BaseCommand):
    args = '<service_id service_id ...>'
    help = 'Enqueue django hosting for deployment'

    def handle(self, *args, **options):
        for service_id in args:
            try:
                service = DjangoHostingService.objects.get(pk=int(service_id))
                if service.is_deployed():
                    raise CommandError('DjangoHostingService "%s" '
                                       'already deployed' % service_id)
                deploy_django_hosting_service.delay(service)
            except DjangoHostingService.DoesNotExist:
                raise CommandError('DjangoHostingService "%s" does not exist' %
                                   service_id)

            self.stdout.write('%s: OK' % service)
