from django import forms
from .models import Planificacion
from .models import Historial
from .models import CustomUser  # Importa el modelo CustomUser
from django.shortcuts import render, redirect
class PlanificacionForm(forms.ModelForm):
    class Meta:
        model = Planificacion
        fields = ['destino', 'tiempodeviaje', 'ruta', 'descripcion', 'usuario']

class HistorialForm(forms.ModelForm):
    class Meta:
        model = Historial
        fields = ['diagnostico' , 'alergias', 'afecciones', 'medicamento']  
    # Utiliza el modelo CustomUser en lugar de User
    usuario = forms.ModelChoiceField(queryset=CustomUser.objects.all())


