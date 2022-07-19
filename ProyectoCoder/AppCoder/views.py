import email
from django.shortcuts import render
from AppCoder.models import Familia, Curso, Profesor, Playlist, Artista, Album
from django.http import HttpResponse
from django.template import Context, Template, loader
from datetime import datetime
import datetime
from AppCoder.forms import Curso_form, Profe_form, Playlist_form, Artista_form, Album_form


# Create your views here.
def curso(self):
    curso=Curso(nombre='Sistemas', comision=37060)
    curso.save()
    texto=f'Curso creado: {curso.nombre} {curso.comision} '

    return HttpResponse(texto)

def inicio(request):
    return render (request, "AppCoder/inicio.html")

def cursos(request):
    return render (request, "AppCoder/cursos.html")

def profesores(request):
    return render (request, "AppCoder/profesores.html")

def estudiantes(request):
    return render(request, "AppCoder/estudiantes.html")

def entregables(request):
    return render (request, "AppCoder/entregables.html")


def mama(self):
    nombre='Daniela'
    apellido='Lascano'
    anio_de_nacimiento=str(int(datetime.datetime.now().year)-int(56))
    edad=56
    hoy=str(datetime.datetime.today())
    
    diccionario={'nombre_mama':nombre, 'apellido_mama': apellido, 'anio_de_nacimiento_mama': anio_de_nacimiento, 'edad_mama': edad, 'hoy': hoy}

    plantilla=loader.get_template('template2.html')

    documento=plantilla.render(diccionario) 

    return HttpResponse(documento)

def papa(self):
    nombre='José Luis'
    apellido='Bazán'
    anio_de_nacimiento=str(int(datetime.datetime.now().year)-int(61))
    edad=61
    hoy=str(datetime.datetime.today())
    
    diccionario={'nombre_papa':nombre, 'apellido_papa': apellido, 'anio_de_nacimiento_papa': anio_de_nacimiento, 'edad_papa': edad, 'hoy': hoy}

    plantilla=loader.get_template('template2.html')

    documento=plantilla.render(diccionario)

    return HttpResponse(documento)

def tia(self):
    nombre='María José'
    apellido='Lascano'
    anio_de_nacimiento=str(int(datetime.datetime.now().year)-int(48))
    edad=48
    hoy=str(datetime.datetime.today())
    
    diccionario={'nombre_tia':nombre, 'apellido_tia': apellido, 'anio_de_nacimiento_tia': anio_de_nacimiento, 'edad_tia': edad, 'hoy': hoy}

    plantilla=loader.get_template('template2.html')

    documento=plantilla.render(diccionario) 

    return HttpResponse(documento)

def curso_formulario(request):
    if (request.method=="POST"):
        form=Curso_form(request.POST)
        if form.is_valid():
            info= form.cleaned_data #dicc con la info sin lo demás
            nombre =info["nombre"]
            comision =info["comision"]
            curso=Curso(nombre=nombre, comision=comision)
            curso.save()
            return render (request, "AppCoder/inicio.html")
    else:
        form=Curso_form() #creo el form vacío
    return render(request, "AppCoder/curso_formulario.html", {"formulario":form}) #lo renderizo y se lo mando como un dicc para que lo pueda usar la template


def profe_formulario(request):
    if (request.method=="POST"):
        form=Profe_form(request.POST)
        if form.is_valid():
            info= form.cleaned_data #dicc con la info sin lo demás
            nombre =info["nombre"]
            apellido =info["apellido"]
            email =info["email"]
            profesion =info["profesion"]
            profe=Profesor(nombre=nombre, apellido=apellido, email=email, profesion=profesion)
            profe.save()
            return render (request, "AppCoder/inicio.html")
    else: #sino viene por GET
        form=Profe_form() #creo el form vacío
    return render(request, "AppCoder/profe_formulario.html", {"formulario":form}) #lo renderizo y se lo mando como un dicc para que lo pueda usar la template


def busqueda_comision(request):
    return render(request, "AppCoder/busqueda_comision.html")

def buscar(request):
    if request.GET["comision"]:
        camada=request.GET["comision"]
        cursos=Curso.objects.filter(comision=camada) #comision__icontains=camada: traerá comisiones que contienen los mismos numeros de la comision que se busca
        return render(request, "AppCoder/resultados_busqueda.html", {"cursos":cursos})
    else:
        return render(request, "AppCoder/busqueda_comision.html", {"error": "No se ingresó ninguna comisión"})


def playlist_formulario(request):
    if (request.method=="POST"):
        form=Playlist_form(request.POST)
        if form.is_valid():
            info= form.cleaned_data #dicc con la info sin lo demás
            nombre_cancion=info["nombre_cancion"]
            artista=info["artista"]
            album=info["album"]
            playlist=Playlist(nombre_cancion=nombre_cancion, artista=artista, album=album)
            playlist.save()
            return render (request, "AppCoder/inicio.html")
    else: #sino viene por GET
        form=Playlist_form() #creo el form vacío
    return render(request, "AppCoder/playlist_formulario.html", {"formulario":form}) #lo renderizo y se lo mando como un dicc para que lo pueda usar la template

def busqueda_cancion(request):
    return render(request, "AppCoder/busqueda_cancion.html")

def buscar_cancion(request):
    if request.GET["nombre_cancion"]:
        nombre_cancion=request.GET["nombre_cancion"]
        canciones=Playlist.objects.filter(nombre_cancion__icontains=nombre_cancion)
        return render(request, "AppCoder/resultados_busqueda_cancion.html", {"canciones":canciones})
    else:
        return render(request, "AppCoder/busqueda_cancion.html", {"error": "No se ingresó ninguna canción"})


#ARTISTA
def artista_formulario(request):
    if (request.method=="POST"):
        form=Artista_form(request.POST)
        if form.is_valid():
            info= form.cleaned_data #dicc con la info sin lo demás
            nombre_completo=info["nombre_completo"]
            nacionalidad=info["nacionalidad"]
            arte=info["arte"]
            artistas=Artista(nombre_completo=nombre_completo, nacionalidad=nacionalidad, arte=arte)
            artistas.save()
            return render (request, "AppCoder/inicio.html")
    else: #sino viene por GET
        form=Artista_form() #creo el form vacío
    return render(request, "AppCoder/artista_formulario.html", {"formulario":form}) #lo renderizo y se lo mando como un dicc para que lo pueda usar la template

def busqueda_artista(request):
    return render(request, "AppCoder/busqueda_artista.html")

def buscar_artista(request):
    if request.GET["nombre_completo"]:
        nombre_completo=request.GET["nombre_completo"]
        artistas=Artista.objects.filter(nombre_completo__icontains=nombre_completo)
        return render(request, "AppCoder/resultados_busqueda_artista.html", {"artistas":artistas})
    else:
        return render(request, "AppCoder/busqueda_artista.html", {"error": "No se ingresó ningún artista con ese nombre"})


#ALBUM
def album_formulario(request):
    if (request.method=="POST"):
        form=Album_form(request.POST)
        if form.is_valid():
            info= form.cleaned_data #dicc con la info sin lo demás
            nombre_album=info["nombre_album"]
            creador=info["creador"]
            año=info["año"]
            albums=Album(nombre_album=nombre_album, creador=creador, año=año)
            albums.save()
            return render (request, "AppCoder/inicio.html")
    else: #sino viene por GET
        form=Album_form() #creo el form vacío
    return render(request, "AppCoder/album_formulario.html", {"formulario":form}) #lo renderizo y se lo mando como un dicc para que lo pueda usar la template

def busqueda_album(request):
    return render(request, "AppCoder/busqueda_album.html")

def buscar_album(request):
    if request.GET["nombre_album"]:
        nombre_album=request.GET["nombre_album"]
        albums=Album.objects.filter(nombre_album__icontains=nombre_album)
        return render(request, "AppCoder/resultados_busqueda_album.html", {"albums":albums})
    else:
        return render(request, "AppCoder/busqueda_album.html", {"error": "No se ingresó ningún album con ese nombre"})



def leer_profesores(request):
    profesores=Profesor.objects.all()
    return render(request, "AppCoder/leer_profesores.html", {"profesores":profesores})