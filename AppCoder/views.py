from django.http.request import QueryDict
from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from AppCoder.models import Tarea, Personal #Equipos, Stock
from AppCoder.forms import TareaFormulario, PersonalFormulario, UserRegisterForm

#Para el login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate

from django.contrib.auth.decorators import login_required

# Create your views here.

def tarea(request):

      tarea =  Tarea(tarea="reparar equipo", nombre_equipo="105")
      tarea.save()
      documentoDeTexto = f"--->Tarea: {tarea.tarea}   nombre_equipo: {tarea.nombre_equipo}   personal_asignado: {tarea.personal_asignado}"


      return HttpResponse(documentoDeTexto)


def inicio(request):

      return render(request, "AppCoder/inicio.html")



def equipos(request):

      return render(request, "AppCoder/Equipos.html")


def Stocks(request):

      return render(request, "AppCoder/Stock.html")


def tareas(request):

      if request.method == 'POST':

            miFormulario = TareaFormulario(request.POST) #aquí mellega toda la información del html

            print(miFormulario)

            if miFormulario.is_valid:   #Si pasó la validación de Django

                  informacion = miFormulario.cleaned_data

                  tarea = Tarea (tarea=informacion['tarea'], nombre_equipo=informacion['nombre_equipo']) 

                  tarea.save()

                  return render(request, "AppCoder/inicio.html") #Vuelvo al inicio o a donde quieran

      else: 

            miFormulario= TareaFormulario() #Formulario vacio para construir el html

      return render(request, "AppCoder/tareas.html", {"miFormulario":miFormulario})




def personal(request):

      if request.method == 'POST':

            miFormulario = PersonalFormulario(request.POST) #aquí mellega toda la información del html

            print(miFormulario)

            if miFormulario.is_valid:   #Si pasó la validación de Django

                  informacion = miFormulario.cleaned_data

                  personal = Personal (nombre=informacion['nombre'], apellido=informacion['apellido'], legajo=informacion["legajo"],
                  email=informacion['email'], profesion=informacion['profesion']) 

                  personal.save()

                  return render(request, "AppCoder/inicio.html") #Vuelvo al inicio o a donde quieran

      else: 

            miFormulario= PersonalFormulario() #Formulario vacio para construir el html

      return render(request, "AppCoder/personal.html", {"miFormulario":miFormulario})






def buscar(request):

      if  request.GET["nombre_equipo"]:

	      #respuesta = f"Estoy buscando el equipo nro: {request.GET['camada'] }" 
            nombre_equipo = request.GET['nombre_equipo'] 
            tareas = Tarea.objects.filter(nombre_equipo__icontains=nombre_equipo)

            return render(request, "AppCoder/inicio.html", {"tareas":tareas, "nombre_equipo":nombre_equipo})

      else: 

	      respuesta = "No enviaste datos"

            #No olvidar from django.http import HttpResponse
      
      return HttpResponse(respuesta)


def leerPersonal(request):

      personal = Personal.objects.all() #trae todos los profesores

      contexto= {"Personal":personal} 

      return render(request, "AppCoder/leerPersonal.html",contexto)


def eliminarPersonal(request, profesor_nombre):

    personal = Personal.objects.get(nombre= personal.nombre)
    personal.delete()

    # vuelvo al menú
    personal = Personal.objects.all()  # trae todos los profesores

    contexto = {"Personal": personal}

    return render(request, "AppCoder/leerPersonal.html", contexto)

def editarPersonal(request, personal_nombre):

    # Recibe el nombre del profesor que vamos a modificar
    personal = Personal.objects.get(nombre=personal_nombre)

    # Si es metodo POST hago lo mismo que el agregar
    if request.method == 'POST':

        # aquí mellega toda la información del html
        miFormulario = PersonalFormulario(request.POST)

        print(miFormulario)

        if miFormulario.is_valid:  # Si pasó la validación de Django

            informacion = miFormulario.cleaned_data

            personal.nombre = informacion['nombre']
            personal.apellido = informacion['apellido']
            personal.legajo = informacion['legajo']
            personal.email = informacion['email']
            personal.profesion = informacion['profesion']

            personal.save()

            # Vuelvo al inicio o a donde quieran
            return render(request, "AppCoder/inicio.html")
    # En caso que no sea post
    else:
        # Creo el formulario con los datos que voy a modificar
        miFormulario = PersonalFormulario(initial={'nombre': personal.nombre, 'apellido': personal.apellido, "legajo" : personal.legajo,
                                                   'email': personal.email, 'profesion': personal.profesion})

    # Voy al html que me permite editar
    return render(request, "AppCoder/editarPersonal.html", {"miFormulario": miFormulario, "personal_nombre": personal_nombre})

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

class TareaList(ListView):

    model = Tarea
    template_name = "AppCoder/tareas_list.html"

class TareaDetalle(DetailView):

    model = Tarea
    template_name = "AppCoder/tarea_detalle.html"

class TareaCreacion(CreateView):

    model = Tarea
    success_url = "/AppCoder/tarea/list"
    fields = ['tarea', 'nombre_equipo']

class TareaUpdate(UpdateView):

    model = Tarea
    success_url = "/AppCoder/tarea/list"
    fields = ['nombre', 'nombre_equipo']

class TareaDelete(DeleteView):

    model = Tarea
    success_url = "/AppCoder/tarea/list"


# Vista de login
def login_request(request):

    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():  # Si pasó la validación de Django

            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')

            user = authenticate(username= usuario, password=contrasenia)

            if user is not None:
                login(request, user)

                return render(request, "AppCoder/inicio.html", {"mensaje":f"Bienvenido {usuario}"})
            else:
                return render(request, "AppCoder/inicio.html", {"mensaje":"Datos incorrectos"})
           
        else:

            return render(request, "AppCoder/inicio.html", {"mensaje":"Formulario erroneo"})

    form = AuthenticationForm()

    return render(request, "AppCoder/login.html", {"form": form})


def register(request):

      if request.method == 'POST':

            form = UserCreationForm(request.POST)
            form = UserRegisterForm(request.POST)
            if form.is_valid():

                  username = form.cleaned_data['username']
                  form.save()
                  return render(request,"AppCoder/inicio.html" ,  {"mensaje":"Usuario Creado :)"})

      else:
            form = UserCreationForm()       
            form = UserRegisterForm()     

      return render(request,"AppCoder/registro.html" ,  {"form":form})


@login_required
def inicio(request):

    return render(request, "AppCoder/inicio.html")
