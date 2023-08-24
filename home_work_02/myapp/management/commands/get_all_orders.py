from django.core.management.base import BaseCommand
from myapp.models import Order

class Command(BaseCommand):
    help = 'Get all orders'

    def handle(self, *args, **kwargs):
        for order in Order.objects.all():
            self.stdout.write(f'{order.pk} {order.customer.name} {order.total_price} {order.date_ordered}')
