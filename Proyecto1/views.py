from datetime import datetime
from django.http import HttpResponse
import datetime
from django.template import Context, Template


def saludar(request):
	return HttpResponse('Hola mundo!!')

def segunda_vista(request):
    return HttpResponse('ya entendí, esto es muy simple')

def dia_de_hoy(request):
    dia=datetime.datetime.today()
    cadena='hoy es:' +str(dia)
    return HttpResponse(cadena)

def saludo_con_nombre(self, nombre):
    return HttpResponse("<h1>hola mi nombre es: "+nombre+"</h1>")

def calcula_anio_de_nacimiento(self, edad):
    return HttpResponse("<h1>hola nací en el "+str(int(datetime.datetime.now().year)-int(edad))+"</h1>")

def probando_html(self):
    mi_archivo=open('C:/Users/abril/OneDrive/Documentos/cluster_py/Proyecto1/plantillas/template1.html')

    plantilla=Template(mi_archivo.read()) #leemos el archivo y lo guardamos en una variable. se convierte en un template
    mi_archivo.close() #cierro archivo
    contexto=Context() #creamos contexto(diccionario) vacío

    documento=plantilla.render(contexto) #renderizar: convertir un  texto en algo que pueda ser procesado por un navegador

    return HttpResponse(documento)
