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
    path('playlist_formulario/', playlist_formulario, name= 'playlist_formulario'),
    path('busqueda_cancion/', busqueda_cancion, name= 'busqueda_cancion'),
    path('buscar_cancion/', buscar_cancion, name= 'buscar_cancion'),
    path('artista_formulario/', artista_formulario, name= 'artista_formulario'),
    path('busqueda_artista/', busqueda_artista, name= 'busqueda_artista'),
    path('buscar_artista/', buscar_artista, name= 'buscar_artista'),
    path('album_formulario/', album_formulario, name= 'album_formulario'),
    path('busqueda_album/', busqueda_album, name= 'busqueda_album'),
    path('buscar_album/', buscar_album, name= 'buscar_album'),
]