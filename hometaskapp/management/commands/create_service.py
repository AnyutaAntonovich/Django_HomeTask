from django.core.management.base import BaseCommand
from hometaskapp.models import Service


class Command(BaseCommand):
    help = "Create service."

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='count')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        for i in range(1, count + 1):
            service = Service(name=f'Name service{i}',
                              price=f'{i}',
                              description=f'Description of service {i}',
                              count=f'{i}')
            service.save()
        self.stdout.write('Ok')
