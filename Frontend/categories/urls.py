from django.urls import path
from . import views

urlpatterns = [
path('categorias', views.getCategories, name='categorias'), #El name sirve para acceder a una url
path('nuevaCategoria', views.newCategory, name='nuevaCategoria'),
]