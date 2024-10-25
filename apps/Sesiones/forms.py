from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from .models import User

class FormularioRegistroUsuario(UserCreationForm):
    nombre = forms.CharField(max_length=20, required=True, label='Nombre')
    apellido = forms.CharField(max_length=20, required=True, label='Apellido')
    usuario = forms.CharField(max_length=30, required=True, label='Usuario')
    email = forms.EmailField(required=True, label='Correo electrónico')
    imagen_perfil = forms.ImageField(required=False, label='Imagen de perfil')
    
    class Meta:
        model = User
        fields = ['nombre', 'apellido', 'usuario', 'email', 'password1', 'password2', 'imagen_perfil' ]

class FormularioInicioSesion(forms.Form):
    usuario = forms.CharField(max_length=30, label='Usuario', required=True)
    password = forms.CharField(label='Contraseña', max_length=128,widget=forms.PasswordInput, required=True)

User = get_user_model()

class FormularioPerfilUsuario(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ['nombre', 'apellido','usuario', 'email', 'profile_image',]
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'usuario': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'profile_image': forms.FileInput(attrs={'class': 'form-control-file'}),}

