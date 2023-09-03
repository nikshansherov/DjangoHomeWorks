from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, HttpResponseRedirect
from datetime import date, timedelta
from .forms import *
from .models import *


def index(request):
    return render(request, 'myapp/index.html')


def product_add(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            price = form.cleaned_data['price']
            quantity = form.cleaned_data['quantity']
            description = form.cleaned_data['description']
            image = form.cleaned_data['image']
            fs = FileSystemStorage()
            product = Product(name=name, price=price, quantity=quantity, description=description,
                              image=image, added_date=date.today())
            product.save()
            form = ProductForm()
    else:
        form = ProductForm()
    return render(request, 'myapp/product_add.html', {'form': form})


def product_selection(request):
    products = Product.objects.all()
    return render(request, "myapp/product_selection.html", {"products": products})


def product_change(request, id):
    product = Product.objects.get(id=id)
    if request.method == "POST" and "FILES":
        product.name = request.POST.get("name")
        product.price = request.POST.get("price")
        product.quantity = request.POST.get("quantity")
        product.description = request.POST.get("description")
        product.image = request.FILES.get("image")
        fs = FileSystemStorage()
        product.save()
        return HttpResponseRedirect("/")
    else:
        return render(request, "myapp/product_change.html", {"product": product})


def product_delete(request, id):
    product = Product.objects.get(id=id)
    product.delete()
    return HttpResponseRedirect("/")


def client_add(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            address = form.cleaned_data['address']
            client = Client(name=name, email=email, phone=phone, address=address, registration_date=date.today())
            client.save()
            form = ClientForm()
    else:
        form = ClientForm()
    return render(request, 'myapp/client_add.html', {'form': form})


def client_selection(request):
    clients = Client.objects.all()
    return render(request, "myapp/client_selection.html", {"clients": clients})


def client_change(request, id):
    client = Client.objects.get(id=id)
    if request.method == "POST":
        client.name = request.POST.get("name")
        client.email = request.POST.get("email")
        client.phone = request.POST.get("phone")
        client.address = request.POST.get("address")
        client.save()
        return HttpResponseRedirect("/")
    else:
        return render(request, "myapp/client_change.html", {"client": client})


def client_delete(request, id):
    client = Client.objects.get(id=id)
    client.delete()
    return HttpResponseRedirect("/")


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
