from django.urls import path
from . import views

urlpatterns = [
path('acercaDe', views.about, name='acercaDe'), #El name sirve para acceder a una url
path('documentacion', views.document, name='documentacion'),
]