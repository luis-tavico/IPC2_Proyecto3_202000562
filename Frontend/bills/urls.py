from django.urls import path
from . import views

urlpatterns = [
path('generarFactura', views.generateInvoice, name='generarFactura'),
]