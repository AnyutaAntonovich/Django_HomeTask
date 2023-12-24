from django.core.management.base import BaseCommand
from hometaskapp.models import User


class Command(BaseCommand):
    help = "Create user."

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='count')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        for i in range(1, count + 1):
            user_ = User(name=f'Name{i}',
                        email=f'mail{i}@mail.ru',
                        password=f'{i}',
                        telephone=f'Telephone{i}',
                        adress=f'Adress{i}')
            user_.save()
        self.stdout.write('Ok')
