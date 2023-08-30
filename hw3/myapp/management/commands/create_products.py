from django.core.management.base import BaseCommand
from myapp.models import Client, Product
from datetime import date
from random import randint, randrange
from decimal import Decimal

class Command(BaseCommand):
    help = 'Create products'
    def handle(self, *args, **kwargs):
        for i in range(30):
            product = Product(name=f'name_{i}', description=f'description_{i}',
                            price=Decimal(randrange(100000))/100, quantity=f'{randint(0, 1000)}',
                            added_date=date.today())
            product.save()
            self.stdout.write(f'{product}')
