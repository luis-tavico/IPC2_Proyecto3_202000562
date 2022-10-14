from django.urls import path
from . import views

urlpatterns = [
    path('', views.mainMenu, name='inicio'), 
]