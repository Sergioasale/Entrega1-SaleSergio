from django.db import models

# Create your models here.
class Tarea(models.Model):

    tarea=models.CharField(max_length=40)
    personal_asignado=models.CharField(max_length=40)
    nombre_equipo = models.IntegerField()

    def __str__(self):
        return f"tarea: {self.tarea} - personal_asignado {self.personal_asignado} - nombre_equipo {self.nombre_equipo} "

class Equipos(models.Model):
    nombre= models.CharField(max_length=30)
    marca= models.CharField(max_length=30)
    modelo= models.CharField(max_length=30)
    numero_de_serie= models.CharField(max_length=30)
    numero_de_motor=models.CharField(max_length=30)

    def __str__(self):
        return f"nombre: {self.nombre} - marca {self.marca} - modelo {self.modelo} - numero_de_serie {self.numero_de_serie} - numero_de_motor{self.numero_de_motor} "

class Personal(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    legajo= models.PositiveIntegerField()
    email= models.EmailField()
    profesion= models.CharField(max_length=30)

    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido {self.apellido} - eMail {self.email} - Profesion {self.profesion} - legajo {self.legajo}"

class Stocks(models.Model):
    nombre= models.CharField(max_length=30)
    cantidad_a_ingresar = models.PositiveIntegerField()
    numero_de_parte= models.CharField(max_length=30)
    codigo= models.CharField(max_length=30)

    def __str__(self):
        return f"nombre: {self.nombre} - cantidad_a_ingresar {self.cantidad_a_ingresar} - numero_de_parte {self.numero_de_parte} - codigo {self.codigo}"

from django.contrib.auth.models import User

class Avatar(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    imagen = models.ImageField(upload_to='avatares', null=True, blank = True)

    def __str__(self):
        return f"{self.user} - {self.imagen}"