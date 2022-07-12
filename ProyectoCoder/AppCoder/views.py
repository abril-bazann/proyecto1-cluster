from django.shortcuts import render
from AppCoder.models import Familia, Curso
from django.http import HttpResponse
from django.template import Context, Template, loader
from datetime import datetime
import datetime

# Create your views here.
def curso(self):
    curso=Curso(nombre='Sistemas', comision=37060)
    curso.save()
    texto=f'Curso creado: {curso.nombre} {curso.comision} '

    return HttpResponse(texto)

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



