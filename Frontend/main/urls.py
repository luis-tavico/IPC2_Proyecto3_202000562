from django.urls import path
from . import views

urlpatterns = [
    path('', views.mainMenu, name='inicio'), 
    path('archivoConfiguracion', views.loadFileConfiguration, name='archivoConfiguracion'), 
    path('archivoConsumos', views.loadFileConsumption, name='archivoConsumos'), 
]