from django.urls import path
from . import views

urlpatterns = [
path('generar', views.generate, name='generar'),
]