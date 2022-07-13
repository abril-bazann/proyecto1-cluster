from unicodedata import name
from django.urls import path
from .views import *

urlpatterns = [
    path('curso/', curso),
    path('cursos/', cursos, name= 'cursos' ),
    path('profesores/', profesores,name= 'profesores'),
    path('estudiantes/', estudiantes, name= 'estudiantes'),
    path('entregables/', entregables, name= 'entregables'),
    path('', inicio, name= 'inicio'),
    path('curso_formulario/', curso_formulario, name= 'curso_formulario'),
    path('profe_formulario/', profe_formulario, name= 'profe_formulario'),
    path('busqueda_comision/', busqueda_comision, name= 'busqueda_comision'),
    path('buscar/', buscar, name= 'buscar'),

]