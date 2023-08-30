from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('client_orders/<int:client_id>', views.client_orders, name='client_orders'),
    path('client_orders_period/<int:client_id>/<int:period>',
         views.client_orders_period, name='client_orders_period'),
]
