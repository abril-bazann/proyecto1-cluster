from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}

class UserEditForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput)
    first_name= forms.CharField(max_length=50)
    last_name= forms.CharField(max_length=50)
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name']
        help_texts = {k:"" for k in fields}

class AvatarForm(forms.Form):
    imagen= forms.ImageField(label="Imagen")