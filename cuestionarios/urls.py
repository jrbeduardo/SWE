from django.urls import path
from .views import *

urlpatterns = [
    path('home/', Home.as_view(), name='home'),
    path('busqueda/', realizar_busqueda, name='realizar_busqueda'),
    path('crear_reactivo/', crear_reactivo, name='crear_reactivo'),
    path('crear_tema/', CrearTema.as_view(), name='crear_tema'),
    path('editar_reactivo/<int:id>', editar_reactivo, name='editar_reactivo'),
    path('eliminar_reactivo/<int:id>', eliminar_reactivo, name='eliminar_reactivo'),      
]
