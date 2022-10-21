from django.urls import path
from . import views
urlpatterns = [
path('clientes', views.getCustomers, name='clientes'), #El name sirve para acceder a una url
path('crearCliente', views.createCustomer, name='crearCliente'),
path('editarCliente/<str:id>', views.editCustomer, name='editarCliente'),
path('eliminarCliente/<str:id>', views.deleteCustomer, name='eliminarCliente'),
path('instancias/<str:nit>', views.getInstances, name='instancias'), #El name sirve para acceder a una url
path('crearInstancia', views.createInstance, name='crearInstancia'),
path('editarInstancia/<str:id>', views.editInstance, name='editarInstancia'),
path('eliminarInstancia/<str:id>', views.deleteInstance, name='eliminarInstancia'),
]