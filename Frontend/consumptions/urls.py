from django.urls import path
from . import views

urlpatterns = [
path('consumos', views.getConsumptions, name='consumos'), #El name sirve para acceder a una url
#path('nuevoRecurso', views.newResource, name='nuevoRecurso'),
#path('editarRecurso/<str:id>', views.editResource, name='editarRecurso'),
#path('eliminarRecurso/<str:id>', views.deleteResource, name='eliminarRecurso'),
]