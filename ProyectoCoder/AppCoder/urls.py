from unicodedata import name
from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

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
    path('leer_profesores/', leer_profesores, name= 'leer_profesores'),
    path('eliminar_profesor/<nombre_profesor>', eliminar_profesor, name= 'eliminar_profesor'),
    path('editar_profesor/<nombre_profesor>', editar_profesor, name= 'editar_profesor'),

    #--------------
'''    path('formulario/', formulario, name= 'formulario'),
    path('busqueda_formulario/', busqueda_formulario, name= 'busqueda_formulario'),
    path('buscar_formulario/', buscar_formulario, name= 'buscar_formulario'),'''
    #-----------
    path('estudiante/list/', Estudiante_list.as_view(), name= 'List'),
    path('estudiante/<pk>/', Estudiante_detalle.as_view(), name= 'Detail'),
    path('estudiantes/nuevo/', Estudiante_creacion.as_view(), name= 'Create'),
    path('estudiante/editar/<pk>', Estudiante_update.as_view(), name= 'Edit'),
    path('estudiante/borrar/<pk>', Estudiante_delete.as_view(), name= 'Delete'),
    #-----------
    path('login/', login_request, name= 'login'),
    path('register/', register, name= 'register'),
    path('logout/', LogoutView.as_view(template_name="AppCoder/logout.html"), name= 'logout'),
    path('editar_perfil/', editar_perfil, name= 'editar_perfil'),
    path('agregar_avatar/', agregar_avatar, name= 'agregar_avatar'),

]