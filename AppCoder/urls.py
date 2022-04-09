from django.urls import path

from AppCoder import views

from django.contrib.auth.views import LogoutView

urlpatterns = [
   
    path('', views.inicio, name="Inicio"), #esta era nuestra primer view
    path('tareas', views.tareas, name="Tareas"),
    path('personal', views.personal, name="Personal"),
    path('equipos', views.equipos, name="Equipos"),
    path('stock', views.Stocks, name="Stock"),
    #path('cursoFormulario', views.cursoFormulario, name="CursoFormulario"),
    #path('profesorFormulario', views.profesorFormulario, name="ProfesorFormulario"),
    #path('busquedaCamada',  views.busquedaCamada, name="BusquedaCamada"),
    path('buscar/', views.buscar),
    path('leerPersonal', views.leerPersonal, name = "LeerPersonal"),
    path('eliminarPersonal/<personal_nombre>/', views.eliminarPersonal, name="EliminarPersonal"),
    path('editarPersonal/<personal_nombre>/', views.editarPersonal, name="EditarPersonal"),
    path('tareas/list', views.TareaList.as_view(), name='List'),
    path(r'^(?P<pk>\d+)$', views.TareaDetalle.as_view(), name='Detail'),
    path(r'^nuevo$', views.TareaCreacion.as_view(), name='New'),
    path(r'^editar/(?P<pk>\d+)$', views.TareaUpdate.as_view(), name='Edit'),
    path(r'^borrar/(?P<pk>\d+)$', views.TareaDelete.as_view(), name='Delete'),
    path('login', views.login_request, name="Login"),
    path('register', views.register, name='Register'),
    path('logout', LogoutView.as_view(template_name='AppCoder/logout.html'), name='Logout')
    
   
]

