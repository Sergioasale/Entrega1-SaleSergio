from django.http.request import QueryDict
from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from AppCoder.models import Avatar, Stocks, Tarea, Personal #Equipos, Stock
from AppCoder.forms import AvatarFormulario, TareaFormulario, PersonalFormulario, StockFormulario, UserRegisterForm, UserEditForm

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

def about(request):

      return render(request, "AppCoder/about.html")

def ayuda(request):

      return render(request, "AppCoder/ayuda.html")

def logout(request):

      return render(request, "AppCoder/logout.html")



def Stock(request):

      if request.method == 'POST':

            miFormulario = StockFormulario(request.POST) #aquí mellega toda la información del html

            print(miFormulario)

            if miFormulario.is_valid:   #Si pasó la validación de Django

                  informacion = miFormulario.cleaned_data

                  Stock = Stocks (nombre=informacion['nombre'], cantidad_a_ingresar=informacion['cantidad_a_ingresar'], numero_de_parte=informacion['numero_de_parte'], codigo=informacion['codigo']) 

                  Stock.save()

                  return render(request, "AppCoder/inicio.html") #Vuelvo al inicio o a donde quieran

      else: 

            miFormulario= StockFormulario() #Formulario vacio para construir el html

      return render(request, "AppCoder/stock.html", {"miFormulario":miFormulario})

def tareas(request):

      if request.method == 'POST':

            miFormulario = TareaFormulario(request.POST) #aquí mellega toda la información del html

            print(miFormulario)

            if miFormulario.is_valid:   #Si pasó la validación de Django

                  informacion = miFormulario.cleaned_data

                  tarea = Tarea (tarea=informacion['tarea'], nombre_equipo=informacion['nombre_equipo'], personal_asignado=informacion['personal_asignado']) 

                  tarea.save()

                  return render(request, "AppCoder/inicio.html") #Vuelvo al inicio o a donde quieran

      else: 

            miFormulario= TareaFormulario() #Formulario vacio para construir el html

      return render(request, "AppCoder/tareas.html", {"miFormulario":miFormulario})

def tareasDetalle(request):

      tarea = Tarea.objects.all() #trae todos los profesores

      contexto= {"tarea":tareas} 

      return render(request, "AppCoder/tareaDetalle.html",contexto)


def eliminarTareas(request, personal_nombre):

    tarea = Tarea.objects.get(tarea= tarea.tarea)
    tarea.delete()

    # vuelvo al menú
    tarea = Tarea.objects.all()  # trae todos los profesores

    contexto = {"tarea": tareas}

    return render(request, "AppCoder/tareaDetalle.html", contexto)

def editarTareas(request, tarea_tarea):

    # Recibe el nombre del profesor que vamos a modificar
    tarea = Tarea.objects.get(tarea=tarea_tarea)

    # Si es metodo POST hago lo mismo que el agregar
    if request.method == 'POST':

        # aquí me llega toda la información del html
        miFormulario = TareaFormulario(request.POST)

        print(miFormulario)

        if miFormulario.is_valid:  # Si pasó la validación de Django

            informacion = miFormulario.cleaned_data

            tareas.nombre = informacion['tarea']
            tareas.personal_asignado = informacion['personal_asignado']
            tareas.nombre_equipo = informacion['nombre_equipo']

            tareas.save()

            # Vuelvo al inicio o a donde quieran
            return render(request, "AppCoder/inicio.html")
    # En caso que no sea post
    else:
        # Creo el formulario con los datos que voy a modificar
        miFormulario = TareaFormulario(initial={'tarea': tarea.tarea, 'personal_asignado': tarea.personal_asignado, "nombre_equipo" : tarea.nombre_equipo})

    # Voy al html que me permite editar
    return render(request, "AppCoder/editarPersonal.html", {"miFormulario": miFormulario, "personal_nombre": personal_nombre})

def busquedaPersonal(request):
      return render(request, "AppCoder/busquedaPersonal.html")


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



def PersonalDetalle(request):

      personal = Personal.objects.all() #trae todos los profesores

      contexto= {"Personal":personal} 

      return render(request, "AppCoder/personalDetalle.html",contexto)


def eliminarPersonal(request, personal_nombre):

    personal = Personal.objects.get(nombre= personal.nombre)
    personal.delete()

    # vuelvo al menú
    personal = Personal.objects.all()  # trae todos los profesores

    contexto = {"Personal": personal}

    return render(request, "AppCoder/personalDetalle.html", contexto)

def editarPersonal(request, personal_nombre):

    # Recibe el nombre del profesor que vamos a modificar
    personal = Personal.objects.get(nombre=personal_nombre)

    # Si es metodo POST hago lo mismo que el agregar
    if request.method == 'POST':

        # aquí me llega toda la información del html
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

def busquedaPersonal(request):
      return render(request, "AppCoder/busquedaPersonal.html")

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

class PersonalList(ListView):

    model = Personal
    template_name = "AppCoder/personal_list.html"

class TareaList(ListView):

    model = Tarea
    template_name = "AppCoder/tareas_list.html"


from django.views.generic.detail import DetailView

class PersonalDetalle(DetailView):

    model = Personal
    template_name = "AppCoder/personalDetalle.html"

class TareaDetalle(DetailView):

    model = Tarea
    template_name = "AppCoder/tareaDetalle.html"

from django.views.generic.edit import CreateView


class TareaCreacion(CreateView):

    model = Tarea
    success_url = "/AppCoder/tarea/list"
    fields = ['tarea', 'nombre_equipo','personal_asignado']

class PersonalCreacion(CreateView):

    model = Personal
    success_url = "/AppCoder/personal/list"
    fields = ['nombre', 'apellido','legajo','email', 'profesion']

from django.urls import reverse_lazy

from django.views.generic.edit import UpdateView

class TareaUpdate(UpdateView):

    model = Tarea
    success_url = "/AppCoder/tarea/list"
    fields = ['nombre', 'nombre_equipo', 'personal_asignado']

class PersonalUpdate(UpdateView):

    model = Personal
    success_url = "/AppCoder/personal/list"
    fields = ['nombre', 'apellido','legajo','email', 'profesion']


from django.views.generic.edit import DeleteView

class TareaDelete(DeleteView):

    model = Tarea
    success_url = "/AppCoder/tarea/list"

class PersonalDelete(DeleteView):

    model = Personal
    success_url = "/AppCoder/personal/list"

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
                avatares=Avatar.objects.filter(user = request.user.id)
                
                for i in range(len(avatares)):
                    if avatares[i] =='':
                
                        return render(request, "AppCoder/inicio.html")
                
                    else:
                        return render(request, "AppCoder/inicio.html", {"url":avatares[0].imagen.url})
               
            else:
                return render(request, "AppCoder/mensaje.html", {"mensaje":"Datos incorrectos, por favor intenta loguearte nuevamente"})
           
        else:

            return render(request, "AppCoder/mensaje.html", {"mensaje":"Datos incorrectos, por favor intenta loguearte nuevamente"})

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

def index(request):

    return render(request, "AppCoder/index.html")

def mensaje(request):

    return render(request, "AppCoder/mensaje.html")


@login_required
def inicio(request):
    
    avatares=Avatar.objects.filter(user = request.user.id)

    for i in range(len(avatares)):
        if avatares[i] =='':
                
            return render(request, "AppCoder/inicio.html")
                
        else:
            return render(request, "AppCoder/inicio.html", {"url":avatares[0].imagen.url})
    return render(request, "AppCoder/inicio.html")

@login_required
def editarPerfil(request):

    usuario = request.user

    if request.method == 'POST':

        miFormulario = UserEditForm(request.POST)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password2']
            usuario.last_name = informacion['last_name']
            usuario.first_name = informacion['first_name']
            usuario.save()

            return render(request, "AppCoder/mensaje.html", {"mensaje":"Haz cambiado tus datos correctamente!"})

    else:

        miFormulario = UserEditForm(initial={'email': usuario.email})

    return render(request, "AppCoder/editarPerfil.html", {"miFormulario": miFormulario, "usuario": usuario})

@login_required
def userDetalle(request):

    return render(request, "AppCoder/userDetalle.html")

from django.contrib.auth.models import User
from django.contrib.auth.decorators import user_passes_test

@user_passes_test(lambda u: u.is_superuser)
def agregarAvatar(request):
    if request.method == "POST":
        miFormulario = AvatarFormulario(request.POST, request.FILES) #Aca llega toda la informacion
        avatares=Avatar.objects.filter(user = request.user.id)
        if miFormulario.is_valid():
            u=User.objects.get(username=request.user)
            avatar=Avatar(user=u, imagen=miFormulario.cleaned_data["imagen"])
            avatar.save()
            return render(request, "AppCoder/inicio.html", {"url":avatares[0].imagen.url}) #vuelve al inicio

    else:
        miFormulario = AvatarFormulario() #formulario para construir el html            
      
    return render(request, "AppCoder/agregarAvatar.html", {"miFormulario":miFormulario})