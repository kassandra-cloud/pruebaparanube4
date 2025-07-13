from blog.models import CustomUser  # Ajusta la importación según la ubicación de CustomUser

from django.contrib.auth.forms import UserCreationForm
from django import forms

from blog.models import CustomUser
from django.contrib.auth.forms import UserCreationForm
from django import forms

#se agrega un campo para el usuario personalizado y se crea una opcion para seleccionar roles
class CustomUserForm(UserCreationForm):
    role = forms.ChoiceField(choices=CustomUser.ROLES)
    # Agrega los campos de apellido, email y teléfono
    last_name = forms.CharField(max_length=30, required=True, help_text='Required. 30 characters or fewer.')
    email = forms.EmailField(max_length=254, required=True, help_text='Required. Enter a valid email address.')
    phone_number = forms.CharField(max_length=15, required=True, help_text='Required. Enter a valid phone number.')

    class Meta:
        model = CustomUser
        fields = ('username', 'password1', 'password2', 'role', 'last_name', 'email', 'phone_number')

       