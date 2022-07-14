from django.db import models

# Create your models here.
class Curso(models.Model): 
    #hereda de Models porque Curso es un modelo que estoy creando. modelo: dato en la base de datos
    nombre = models.CharField(max_length=50) #tipo/campo de texto y su longitud
    comision= models.IntegerField() #campo enteros

    def __str__(self):
        return self.nombre+" "+str(self.comision)

class Estudiante(models.Model):
    nombre= models.CharField(max_length=50)

    apellido= models.CharField(max_length=50)

    email= models.EmailField()

    def __str__(self):
        return self.nombre+" "+str(self.apellido)

class Profesor(models.Model):
    nombre= models.CharField(max_length=50)

    apellido= models.CharField(max_length=50)

    email= models.EmailField()

    profesion= models.CharField(max_length=50)

    def __str__(self):
        return self.nombre+" "+str(self.apellido)

class Entregable(models.Model):
    nombre= models.CharField(max_length=50)

    fecha_entrega= models.DateField()

    entregado= models.BooleanField()


class Familia(models.Model):
    nombre= models.CharField(max_length=50)

    apellido= models.CharField(max_length=50)

    anio_de_nacimiento= models.DateField() 

    edad= models.IntegerField(null=True) 

    hoy=models.DateField(max_length=50, null=True)


class Playlist(models.Model):
    nombre_cancion= models.CharField(max_length=50)

    artista= models.CharField(max_length=50)

    album= models.CharField(max_length=50) 

    def __str__(self):
        return self.nombre_cancion+" - "+str(self.artista)




