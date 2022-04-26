from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from AppCoder.models import Avatar


class TareaFormulario(forms.Form):
    #Especificar los campos
    tarea = forms.CharField()
    personal_asignado = forms.CharField()
    nombre_equipo = forms.IntegerField()

class EquiposFormulario(forms.Form):
    #Especificar los campos
    nombre = forms.CharField()
    marca = forms.CharField()
    modelo = forms.CharField()
    numero_de_serie= forms.CharField(max_length=30)
    numero_de_motor = forms.CharField(max_length=30)

class PersonalFormulario(forms.Form):   
    nombre= forms.CharField(max_length=30)
    apellido= forms.CharField(max_length=30)
    legajo= forms.IntegerField()
    email= forms.EmailField()
    profesion= forms.CharField(max_length=30)


class StockFormulario(forms.Form):   
    nombre= forms.CharField(max_length=30)
    cantidad_a_ingresar= forms.IntegerField()
    numero_de_parte= forms.CharField(max_length=30)
    codigo= forms.CharField(max_length=30)

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        # Saca los mensajes de ayuda
        help_texts = {k:"" for k in fields}

class UserEditForm(UserCreationForm):

    # Obligatorios
    email = forms.EmailField(label="Ingrese su email:")
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput(attrs={'readonly': 'readonly', "class":"btn-dark"}))
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput(attrs={'readonly': 'readonly', "class":"btn-dark"}))

    last_name = forms.CharField(label="Apellido")
    first_name = forms.CharField(label="Nombre")

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2', 'last_name', 'first_name']

    def __init__(self, *args, **kwargs):
        super(UserEditForm, self).__init__(*args, **kwargs)
        self.fields["password1"].required = False
        self.fields["password2"].required = False

class AvatarFormulario(forms.ModelForm):

    class Meta:
        model = Avatar
        fields = ['user', 'imagen']