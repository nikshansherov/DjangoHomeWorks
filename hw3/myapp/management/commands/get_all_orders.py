from django.core.management.base import BaseCommand
from myapp.models import Order, Product

class Command(BaseCommand):
    help = 'Get all orders'

    def handle(self, *args, **kwargs):
        for order in Order.objects.all():
            pr_list = []
            for product in order.products.all():
                pr_list.append(product.name)
            self.stdout.write(f'{order.pk} {order.customer.id} {order.customer.name}'
                              f' {order.total_price} {order.date_ordered} {pr_list}')
