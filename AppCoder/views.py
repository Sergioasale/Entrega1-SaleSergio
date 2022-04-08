from django.http import HttpResponse
from AppCoder.models import Personal

def personal(self):
    
    personal = Personal(nombre = "Desarrollo web", apellido = "rata", Legajo= "35353", Email = "rata@raton.com", Equipo_asignado = "VyO 202", profesion= "ser rata")
    personal.save()
    documentoDeTexto = f"--->personal:{personal.nombre}, apellido:{personal.apellido}, legajo:{personal.Legajo}, email:{personal.Email}, equipoAsignado:{personal.Equipo_asignado}, profesion:{personal.profesion}  "
    return HttpResponse(documentoDeTexto)
