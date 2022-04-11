from django.db import models

# Create your models here.
class Tarea(models.Model):

    tarea=models.CharField(max_length=40)
    personal_asignado=models.CharField(max_length=40)
    nombre_equipo = models.IntegerField(max_length=40)
    comienzo_de_trabajo=models.CharField(max_length=40)
    fin_de_trabajo=models.CharField(max_length=40)

    def __str__(self):
        return f"tarea: {self.tarea} - personal_asignado {self.personal_asignado} - nombre_equipo {self.nombre_equipo} - comienzo_de_trabajo {self.comienzo_de_trabajo} - fin_de_trabajo {self.fin_de_trabajo} "

class Equipos(models.Model):
    nombre= models.CharField(max_length=30)
    marca= models.CharField(max_length=30)
    modelo= models.CharField(max_length=30)
    numero_de_serie= models.CharField(max_length=30)
    numero_de_motor=models.PositiveBigIntegerField()

class Personal(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    legajo= models.PositiveIntegerField()
    email= models.EmailField()
    equipo_asignado= models.CharField(max_length=30)
    profesion= models.CharField(max_length=30)

    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido {self.apellido} - E-Mail {self.email} - Profesión {self.profesion}"

class Stock(models.Model):
    nombreotipo= models.CharField(max_length=30)
    fechadeingreso = models.DateField()  
    cantidadaingresar = models.PositiveIntegerField()
    numerodeparte= models.PositiveIntegerField()
