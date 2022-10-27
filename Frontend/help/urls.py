from django.urls import path
from . import views

urlpatterns = [
path('AcercaDe', views.About, name='AcercaDe'), #El name sirve para acceder a una url
]