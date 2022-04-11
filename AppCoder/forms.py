from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class TareaFormulario(forms.Form):
    #Especificar los campos
    tarea = forms.CharField()
    personal_asignado = forms.CharField()
    nombre_equipo = forms.IntegerField()
    comienzo_de_trabajo= forms.DateTimeField()
    final_de_trabajo = forms.DateTimeField()

class EquiposFormulario(forms.Form):
    #Especificar los campos
    nombre = forms.CharField()
    marca = forms.CharField()
    modelo = forms.CharField()
    numero_de_serie= forms.CharField()
    numero_de_motor = forms.CharField()

class PersonalFormulario(forms.Form):   
    nombre= forms.CharField(max_length=30)
    apellido= forms.CharField(max_length=30)
    legajo= forms.IntegerField()
    email= forms.EmailField()
    equipo_asignado= forms.CharField(max_length=30)
    profesion= forms.CharField(max_length=30)


class StockFormulario(forms.Form):   
    nombreotipo= forms.CharField(max_length=30)
    fechadeingreso= forms.DateField()
    cantidadaingresar= forms.IntegerField()
    numerodeparte= forms.CharField(max_length=30)

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        # Saca los mensajes de ayuda
        help_texts = {k:"" for k in fields}
