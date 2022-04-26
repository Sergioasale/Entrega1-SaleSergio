from django.contrib import admin
from  .models import * #importamos el archivo models

# Register your models here.
#registramos los modelos

admin.site.register(Tarea)

admin.site.register(Equipos)

admin.site.register(Personal)

admin.site.register(Stocks)

admin.site.register(Avatar)