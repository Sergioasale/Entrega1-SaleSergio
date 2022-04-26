from django.urls import path

from AppCoder import views

from django.contrib.auth.views import LogoutView

urlpatterns = [
   
    path('', views.inicio, name="Inicio"), #esta era nuestra primer view
    path('tareas', views.tareas, name="Tareas"),
    path('personal', views.personal, name="Personal"),
    path('personal/list', views.PersonalList.as_view(), name='PList'),
    path(r'^(?P<pk>\d+)$', views.PersonalDetalle.as_view(), name='PDetail'),
    path(r'^nuevo$', views.PersonalCreacion.as_view(), name='PNew'),
    path(r'^editar/(?P<pk>\d+)$', views.PersonalUpdate.as_view(), name='PEdit'),
    path(r'^borrar/(?P<pk>\d+)$', views.PersonalDelete.as_view(), name='PDelete'),
    path('equipos', views.equipos, name="Equipos"),
    path('stock', views.Stock, name="Stock"),
    #path('cursoFormulario', views.cursoFormulario, name="CursoFormulario"),
    #path('profesorFormulario', views.profesorFormulario, name="ProfesorFormulario"),
    #path('busquedaCamada',  views.busquedaCamada, name="BusquedaCamada"),
    path('buscar/', views.buscar),
    path('tarea/list', views.TareaList.as_view(), name='List'),
    path('tareas/detalle', views.TareaDetalle.as_view(), name='tDetail'),
    path('tareas/nueva', views.TareaCreacion.as_view(), name='tNew'),
    path('tareas/editar', views.TareaUpdate.as_view(), name='tEdit'),
    path('tareas/borrar', views.TareaDelete.as_view(), name='tDelete'),
    path('busquedaPersonal', views.busquedaPersonal, name='busquedaPersonal'),
    path('login', views.login_request, name="Login"),
    path('register', views.register, name='Register'),
    path('logout', LogoutView.as_view(template_name='AppCoder/logout.html'), name='Logout'),
    path('about',views.about, name="about"),
    path('ayuda', views.ayuda, name="ayuda"),
    path('index', views.index ,name="Index"),
    path('userDetalle', views.userDetalle ,name="UserDetalle"),
    path('agregarAvatar', views.agregarAvatar, name="AgregarAvatar"),
    path('editarPerfil', views.editarPerfil, name="EditarPerfil"),


    
   
]

