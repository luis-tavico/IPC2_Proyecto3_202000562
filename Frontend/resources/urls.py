from django.urls import path
from . import views

urlpatterns = [
path('recursos', views.getResources, name='recursos'), #El name sirve para acceder a una url
path('crearRecurso', views.createResource, name='crearRecurso'),
path('editarRecurso/<str:id>', views.editResource, name='editarRecurso'),
path('eliminarRecurso/<str:id>', views.deleteResource, name='eliminarRecurso'),
]