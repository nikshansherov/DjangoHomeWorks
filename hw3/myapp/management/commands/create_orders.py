from django.core.management.base import BaseCommand
from myapp.models import Client, Product, Order
from datetime import date
from random import randint

class Command(BaseCommand):
    help = 'Create order'

    def handle(self, *args, **kwargs):
        for client in Client.objects.all():
            for i in range(randint(1,5)):
                order = Order(customer=client, date_ordered=date.today())
                order.save()
                sum_price = 0
                for i in range(randint(1,10)):
                    temp = randint(1, 30)
                    order.products.add(temp)
                    product = Product.objects.filter(pk=temp).first()
                    sum_price += product.price
                order.total_price = sum_price
                order.save()
                self.stdout.write(f'{order}')
