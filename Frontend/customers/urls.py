from django.urls import path
from . import views

urlpatterns = [
    path('clientes', views.getCustomers, name='clientes'), 
    path('nuevoCliente', views.newCustomer, name='nuevoCliente'), 
]