from django import forms

class Curso_form(forms.Form): #es un form, hereda de un form
    nombre=forms.CharField(max_length=50)
    comision=forms.IntegerField()

class Profe_form(forms.Form):
    nombre=forms.CharField(max_length=50)
    apellido=forms.CharField(max_length=50)
    email=forms.EmailField()
    profesion=forms.CharField(max_length=50)