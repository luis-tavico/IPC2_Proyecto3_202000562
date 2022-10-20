from django.urls import path
from . import views
urlpatterns = [
path('clientes', views.getCustomers, name='clientes'), #El name sirve para acceder a una url
path('nuevoCliente', views.newCustomer, name='nuevoCliente'),
path('editarCliente/<str:id>', views.editCustomer, name='editarCliente'),
path('eliminarCliente/<str:id>', views.deleteCustomer, name='eliminarCliente'),
#path('instancias', views.getInstances, name='instancias'), #El name sirve para acceder a una url
#path('nuevaInstancia', views.newInstance, name='nuevaInstancia'),
#path('editarInstancia/<str:id>', views.editInstance, name='editarInstancia'),
#path('eliminarInstancia/<str:id>', views.deleteInstance, name='eliminarInstancia'),
]