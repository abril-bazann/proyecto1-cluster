from django import forms

class Curso_form(forms.Form): #es un form, hereda de un form
    nombre=forms.CharField(max_length=50)
    comision=forms.IntegerField()

class Profe_form(forms.Form):
    nombre=forms.CharField(max_length=50)
    apellido=forms.CharField(max_length=50)
    email=forms.EmailField()
    profesion=forms.CharField(max_length=50)


class Playlist_form(forms.Form):
    nombre_cancion=forms.CharField(max_length=50)
    artista=forms.CharField(max_length=50)
    album=forms.CharField(max_length=50)

class Artista_form(forms.Form):
    nombre_completo=forms.CharField(max_length=50)
    nacionalidad=forms.CharField(max_length=50)
    arte=forms.CharField(max_length=50)

class Album_form(forms.Form):
    nombre_album=forms.CharField(max_length=50)
    creador=forms.CharField(max_length=50)
    año=forms.CharField(max_length=50)