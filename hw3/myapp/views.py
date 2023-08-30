from django.shortcuts import render
from django.http import HttpResponse
from .models import Order
from datetime import date, timedelta


def index(request):
    return render(request, 'myapp/index.html')


def client_orders(request, client_id):
    cont = {}
    for order in Order.objects.all():
        if order.customer.id == client_id:
            client_name = order.customer.name
            pr_list = []
            for product in order.products.all():
                pr_list.append(product.name)
            cont[f'Заказ № {order.id}'] = pr_list
    context = {'orders': cont, 'client': client_name}
    return render(request, 'myapp/client_orders.html', context)


def client_orders_period(request, client_id, period):
    time = date.today() - timedelta(days=period)
    cont = {}
    for order in Order.objects.all():
        if order.date_ordered >= time:
            if order.customer.id == client_id:
                client_name = order.customer.name
                product_list = []
                for product in order.products.all():
                    if product.name not in product_list:
                        product_list.append(product.name)
    context = {'product_list': product_list, 'client': client_name, 'period': period}
    return render(request, 'myapp/client_orders_period.html', context)
