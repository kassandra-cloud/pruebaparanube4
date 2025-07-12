from django.shortcuts import render
from django.views.generic import TemplateView
import pyrebase
from blog.models import Historial
from blog.models import Planificacion
from django.shortcuts import render, redirect
from .forms import PlanificacionForm  # Importa el formulario
from .forms import HistorialForm # Importa el formulario
from django.shortcuts import get_object_or_404, render, redirect
from .models import CustomUser, UsuarioEliminado,HistorialUsuario
from django.contrib import messages
from pages.forms import CustomUserForm
def mostrarHistorial(request):
    historial = Historial.objects.all()
    return render(request, 'listado2.html', {'historial': historial})
def mostrarHistorial2(request):
    historial = Historial.objects.all()
    return render(request, 'listadofamiliar2.html', {'historial': historial})



def insertarHistorial(request):
    if request.method == 'POST':
        form = HistorialForm(request.POST)
        if form.is_valid():
            form.save()
            datos = { 'r' : 'Planificacion Realizada Correctamente!!' }
            return render(request, 'historial.html', datos)
    else:
        form = HistorialForm()
    return render(request, 'historial.html', {'form': form})
    


def insertar2Planificacion(request):
    if request.method == 'POST':
        form = PlanificacionForm(request.POST)
        if form.is_valid():
            form.save()
            datos = { 'r' : 'Planificacion Realizada Correctamente!!' }
            return render(request, 'planificacion.html', datos)
    else:
        form = PlanificacionForm()
    return render(request, 'planificacion.html', {'form': form})
    

def mostrarPlanificaciones(request):
    planificaciones = Planificacion.objects.all()
    return render(request, 'listado.html', {'planificaciones': planificaciones})
def mostrarPlanificaciones2(request):
    planificaciones = Planificacion.objects.all()
    return render(request, 'listadofamiliar.html', {'planificaciones': planificaciones})

config = {
  "apiKey": "AIzaSyC67hXjxlRqc8w-XhJ93MfsoOV2xIrDTTg",
  "authDomain": "taller-4c345.firebaseapp.com",
  "projectId": "taller-4c345",
  "storageBucket": "taller-4c345.appspot.com",
  "messagingSenderId": "774852381188",
  "appId": "1:774852381188:web:5b202e05af0a4b6dbc0351",
  "databaseURL": "https://taller-4c345-default-rtdb.firebaseio.com"
};
firebase=pyrebase.initialize_app(config)
db=firebase.database()
class BlogPageView(TemplateView):
    template_name="blog.html"



def lista_usuarios(request):
    usuarios = CustomUser.objects.all()
    return render(request, 'listausuarios.html', {'usuarios': usuarios})


def eliminar_usuario(request, usuario_id):
    usuario = get_object_or_404(CustomUser, id=usuario_id)

    # Crea un nuevo registro en UsuarioEliminado copiando los datos del usuario original
    UsuarioEliminado.objects.create(
        idusuario=usuario.id,
        username=usuario.username,
        email=usuario.email,
        role=usuario.role,
        # Agrega otros campos según sea necesario
    )
    
    # Elimina el usuario original
    usuario.delete()
    messages.success(request, f"El usuario {usuario.username} fue eliminado correctamente.")
    return redirect('listausuarios')  # Redirige a la lista de usuarios después de la eliminación

def confirmar_eliminacion(request, usuario_id):
    usuario = CustomUser.objects.get(id=usuario_id)
    return render(request, 'confirmaeliminacion.html', {'usuario': usuario})

def modificar_usuario(request, usuario_id):
    usuario = get_object_or_404(CustomUser, id=usuario_id)

    if request.method == 'POST':
        # Guardar los datos antiguos en la tabla de historial
        HistorialUsuario.objects.create(
            username_anterior=usuario.username,
            email_anterior=usuario.email,
            role_anterior=usuario.role,
            # Otros campos según sea necesario
            usuario=usuario
        )

        # Procesar el formulario y realizar la modificación
        form = CustomUserForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            # Puedes agregar mensajes de éxito aquí si lo deseas
            # Mensaje de éxito
            messages.success(request, '¡Usuario modificado con éxito!')
            return redirect('listausuarios')  # Redirige a la lista de usuarios después de la modificación
    else:
        form = CustomUserForm(instance=usuario)

    return render(request, 'modificardatos.html', {'form': form, 'usuario': usuario})