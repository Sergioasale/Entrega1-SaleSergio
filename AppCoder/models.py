from django.db import models

class Personal(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    Legajo= models.PositiveIntegerField (default=0)
    Email= models.EmailField()
    Equipo_asignado= models.CharField(max_length=30)
    profesion= models.CharField(max_length=30)

class Equipos(models.Model):
    Nombre= models.CharField(max_length=30)
    Marca= models.CharField(max_length=30)
    Modelo= models.CharField(max_length=30)
    Numero_de_serie= models.PositiveIntegerField (default=0)
    Numero_de_motor= models.PositiveIntegerField (default=0)
    
class Tareas(models.Model):
    Trabajo_a_realizar= models.CharField(max_length=30)
    Personal_Asignado= models.CharField(max_length=30)
    Equipo= models.CharField(max_length=30)
    Comienzo_de_trabajo= models.DateField()
    Final_de_trabajo= models.DateField()
    
class Ingreso_Materiales(models.Model):
    NombreOtipo= models.CharField(max_length=30)
    FechaDeIngreso = models.DateField()
    CantidadAIngresar= models.PositiveIntegerField (default=0)
    NumeroDeParte= models.CharField(max_length=30)

