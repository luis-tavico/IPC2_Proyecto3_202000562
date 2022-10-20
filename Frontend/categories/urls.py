from django.urls import path
from . import views

urlpatterns = [
path('categorias', views.getCategories, name='categorias'), #El name sirve para acceder a una url
path('nuevaCategoria', views.newCategory, name='nuevaCategoria'),
path('editarCategoria/<str:id>', views.editCategory, name='editarCategoria'),
path('eliminarCategoria/<str:id>', views.deleteCategory, name='eliminarCategoria'),
path('configuraciones/<str:id>', views.getConfigurations, name='configuraciones'), #El name sirve para acceder a una url
path('nuevaConfiguracion', views.newConfiguration, name='nuevaConfiguracion'),
path('editarConfiguracion/<str:id>', views.editConfiguration, name='editarConfiguracion'),
path('eliminarConfiguracion/<str:id>', views.deleteConfiguration, name='eliminarConfiguracion'),
path('recursos/<str:id>', views.getResources, name='recursos'), #El name sirve para acceder a una url
path('nuevoRecurso', views.newResource, name='nuevoRecurso'),
#path('editarRecurso/<str:id>', views.editResource, name='editarRecurso'),
path('eliminarRecurso/<str:id>', views.deleteResource, name='eliminarRecurso'),
]