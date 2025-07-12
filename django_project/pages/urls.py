from django.urls import path
from .views import InicioPageView, RegistroPageView, Inicio2PageView, NavegacionPageView, Navegacion2PageView,registro_usuario,InicioUsuarioPageView, HistorialPageView, ListadoPageView, planificacionPageView, Listado2PageView
from .views import login_view,InicioAdminPageView,agregar_usuario,ModificarDatosPageView,ListadofamiliarPageView,Listadofamiliar2PageView,NavegacionFamiliarPageView
from blog.views import lista_usuarios,eliminar_usuario,confirmar_eliminacion,modificar_usuario
urlpatterns = [
    path("inicio/", InicioPageView.as_view(), name = "inicio"),  
    path("listadofamiliar/", ListadofamiliarPageView.as_view(), name = "listadofamiliar"),  
    path("listadofamiliar2/", Listadofamiliar2PageView.as_view(), name = "listadofamiliar2"),  
    path("navegacionfamiliar/", NavegacionFamiliarPageView.as_view(), name = "navegacionfamiliar"),  
    path("registro2/", RegistroPageView.as_view(), name = "registro"),
    path("inicio2", Inicio2PageView.as_view(), name = "inicio2"), 
    path("navegacion/", NavegacionPageView.as_view(), name = "navegacion"),
    path("navegacion2/", Navegacion2PageView.as_view(), name = "navegacion2"),
    path("inicioadmin/", InicioAdminPageView.as_view(), name = "inicioadmin"),
    path("registro/", registro_usuario, name="registro_usuario"),
    path("iniciousuario",InicioUsuarioPageView.as_view(),name="iniciousuario"),
    path('', login_view, name='login'),
    path("historial",HistorialPageView.as_view(),name="historial"),
    path("listado",ListadoPageView.as_view(),name="listado"),
    path("listado2",Listado2PageView.as_view(),name="listado2"),
    path("planificacion",planificacionPageView.as_view(),name="planificacion"),
    path("modificardatos/",ModificarDatosPageView.as_view(),name="modificardatos"),
    path('agregarusuario/',agregar_usuario, name='agregarusuario'),
    path('listausuario/', lista_usuarios, name='listausuarios'),
    path('eliminar_usuario/<int:usuario_id>/', eliminar_usuario, name='eliminar_usuario'),
    path('confirmar_eliminacion/<int:usuario_id>/', confirmar_eliminacion, name='confirmar_eliminacion'),
    path('modificar_usuario/<int:usuario_id>/', modificar_usuario, name='modificar_usuario'),

  
  
]
