from datetime import datetime
from django.http import HttpResponse
import datetime
from django.template import Context, Template, loader

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

    nom='Daniela'
    ape='Lascano'
    lista_de_notas=[1,2,3,4,5,6,7,8,9,10]
    #(recorre lista de notas)
    diccionario={'nombre':nom, 'apellido': ape, 'lista': lista_de_notas}

    plantilla=loader.get_template('template1.html')

    documento=plantilla.render(diccionario) #renderizar: convertir un  texto en algo que pueda ser procesado por un navegador

    return HttpResponse(documento)
