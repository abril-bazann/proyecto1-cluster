import email
from django.shortcuts import render
from AppCoder.models import Familia, Curso, Profesor
from django.http import HttpResponse
from django.template import Context, Template, loader
from datetime import datetime
import datetime
from AppCoder.forms import Curso_form, Profe_form

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

'''def curso_formulario(request):
    if (request.method=="POST"):
        nombre= request.POST.get("curso")
        comision= request.POST.get("comision")
        curso=Curso(nombre=nombre, comision=comision)
        curso.save()
        return render (request, "AppCoder/inicio.html")

    return render(request, "AppCoder/curso_formulario.html") VISTA PRA FORM HTML'''

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
