from django.core.management.base import BaseCommand
from myapp.models import Client
from datetime import date

class Command(BaseCommand):
    help = 'Create clients'

    def handle(self, *args, **kwargs):
        # client = Client(name=f'name_', email=f'email_@mail.ru',
        #                 phone=f'phone_', address=f'phone',
        #                 registration_date=f'lfnf')
        # client.save()
        # self.stdout.write(f'{client.name} {client.email}')
        for i in range(10):
            client = Client(name=f'name_{i}', email=f'email_{i}@mail.ru',
                            phone=f'phone_{i}', address=f'phone_{i}',
                            registration_date=date.today())
            client.save()
            self.stdout.write(f'{client}')
