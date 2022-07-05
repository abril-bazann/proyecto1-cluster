from django.shortcuts import render
from AppCoder.models import Curso, Familia
from django.http import HttpResponse
from django.template import Context, Template, loader
from datetime import datetime
import datetime

# Create your views here.

def mama(self):
    mama=Familia(nombre='Daniela', apellido='Lascano', anio_de_nacimiento=str(int(datetime.datetime.now().year)-int(56)), edad=56, hoy=str(datetime.datetime.today()))
    mama.save()

    cadena=f'Mi nombre es {mama.nombre} {mama.apellido}, nací en el {mama.anio_de_nacimiento}, tengo {mama.edad} años y hoy es {mama.hoy}'

    return HttpResponse(cadena)

def papa(self):
    papa=Familia(nombre='José Luis', apellido='Bazán', anio_de_nacimiento=str(int(datetime.datetime.now().year)-int(61)), edad=61, hoy=str(datetime.datetime.today()))
    papa.save()
    
    cadena=f'Mi nombre es {papa.nombre} {papa.apellido}, nací en el {papa.anio_de_nacimiento}, tengo {papa.edad} años y hoy es {papa.hoy}'

    return HttpResponse(cadena)

def tia(self):
    tia=Familia(nombre='Maria José', apellido='Lascano', anio_de_nacimiento=str(int(datetime.datetime.now().year)-int(47)), edad=47, hoy=str(datetime.datetime.today()))
    tia.save()
    
    cadena=f'Mi nombre es {tia.nombre} {tia.apellido}, nací en el {tia.anio_de_nacimiento}, tengo {tia.edad} años y hoy es {tia.hoy}'

    return HttpResponse(cadena)
    



