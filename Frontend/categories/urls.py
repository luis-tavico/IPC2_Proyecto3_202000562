from django.urls import path
from . import views

urlpatterns = [
path('categorias', views.getCategories, name='categorias'), #El name sirve para acceder a una url
path('crearCategoria', views.createCategory, name='crearCategoria'),
path('editarCategoria/<str:id>', views.editCategory, name='editarCategoria'),
path('eliminarCategoria/<str:id>', views.deleteCategory, name='eliminarCategoria'),
path('configuraciones/<str:id>', views.getConfigurations, name='configuraciones'), #El name sirve para acceder a una url
path('crearConfiguracion', views.createConfiguration, name='crearConfiguracion'),
path('editarConfiguracion/<str:id>', views.editConfiguration, name='editarConfiguracion'),
path('eliminarConfiguracion/<str:id>', views.deleteConfiguration, name='eliminarConfiguracion'),
path('recursosEnConfiguracion/<str:id>', views.getResources, name='recursosEnConfiguracion'), #El name sirve para acceder a una url
path('agregarRecursoConfiguracion', views.addResource, name='agregarRecursoConfiguracion'),
#path('editarRecurso/<str:id>', views.editResource, name='editarRecurso'),
path('eliminarRecursoConfiguracion/<str:id>', views.deleteResource, name='eliminarRecursoConfiguracion'),
]