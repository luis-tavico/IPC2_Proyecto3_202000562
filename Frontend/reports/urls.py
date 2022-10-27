from django.urls import path
from . import views

urlpatterns = [
path('facturas', views.getBills, name='facturas'), #El name sirve para acceder a una url
path('reporteFactura/<str:numero>', views.invoiceReport, name='reporteFactura'), 
]