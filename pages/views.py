from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import render,redirect  # Importa la función render
from .forms import CustomUserForm
from django.contrib.auth import login,authenticate
from django.urls import reverse
import pyrebase
from django.http import JsonResponse
from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, redirect
from django.contrib import messages
from pages.forms import CustomUserForm
config = {
  "apiKey": "AIzaSyDF1R4sFm2errtHxJprQQrhOQFdR7PIc4c",
  "authDomain": "prueba-6bcea.firebaseapp.com",
  "projectId": "prueba-6bcea",
  "storageBucket": "prueba-6bcea.appspot.com",
  "messagingSenderId": "635691141851",
  "appId": "1:635691141851:web:bb4762f0b0f4cc09545afe",
  "databaseURL": "https://prueba-6bcea-default-rtdb.firebaseio.com" 

};

firebase=pyrebase.initialize_app(config)
db=firebase.database()

class InicioPageView(TemplateView):
    template_name = "inicio.html"

class RegistroPageView(TemplateView):
    template_name = "registro.html"
  
#se crea una validacion para que si el usuario no esta autentificado no se le muestre el inicio2  
class Inicio2PageView(TemplateView):
    template_name = "inicio2.html"
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
         return super().dispatch(*args, **kwargs)
    
   

class NavegacionPageView(TemplateView):
    template_name = "navegacion.html"

class Navegacion2PageView(TemplateView):
    template_name = "navegacion2.html"

   
class InicioUsuarioPageView(TemplateView):
    template_name = "iniciousuario.html"

class HistorialPageView(TemplateView):
    template_name = "historial.html"

class planificacionPageView(TemplateView):
    template_name = "planificacion.html"

class ListadoPageView(TemplateView):
    template_name = "listado.html"

class Listado2PageView(TemplateView):
    template_name = "listado2.html"

class InicioAdminPageView(TemplateView):
    template_name = "inicioadmin.html"

class ModificarDatosPageView(TemplateView):
    template_name = "modificardatos.html"

class ListadofamiliarPageView(TemplateView):
    template_name = "listadofamiliar.html"    

class Listadofamiliar2PageView(TemplateView):
    template_name = "listadofamiliar2.html"    

class NavegacionFamiliarPageView(TemplateView):
    template_name = "navegacionfamiliar.html"        
def agregar_usuario(request):
    mensaje = None

    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            mensaje = 'Usuario agregado correctamente!'
            return render(request, 'agregarusuario.html', {'form': CustomUserForm(), 'r': mensaje})
    else:
        form = CustomUserForm()

    return render(request, 'agregarusuario.html', {'form': form})


def is_admin(user):
    return user.is_authenticated and user.is_staff
#logica para el inicio de sesion
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirigir al usuario a la página deseada según su rol
                if user.role == 'familiar':
                    return redirect('inicio2')  #pagina para usuarios familiares
                elif user.role == 'usuario':
                    return redirect('iniciousuario')  #pagina  para usuarios
                elif user.is_staff:
                    return redirect('inicioadmin')

    else:
        form = AuthenticationForm()

    return render(request, 'registration/login.html', {'form': form})
#metodo de registro
def registro_usuario(request):
    if request.method == 'POST':
        formulario = CustomUserForm(request.POST)

        if formulario.is_valid():
            user = formulario.save()
            role = formulario.cleaned_data['role']

            # Asignar el rol al usuario
            user.role = role
            user.save()

            # Guardar algunos datos en Firebase
            user_data = {
                'username': user.username,
                'email': user.email,
                'rol': role
            }
            db.child('usuarios').child(user.id).set(user_data)

            # Redirigir al usuario a la página de inicio correspondiente al rol
            if role == 'familiar':
                return redirect('inicio2')
            elif role == 'usuario':
                return redirect('iniciousuario')

    data = {'form': CustomUserForm()}
    return render(request, 'registration/registrar.html', data)