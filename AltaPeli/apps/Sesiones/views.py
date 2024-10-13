from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required



## Función para gestionar el registro de usuarios.
def registroUsuarios(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario) ## Autentica el usuario post registro
            return redirect('login')
    else:
        form = CustomUserCreationForm()
        
    return render(request, 'sesiones/registro.html', {'form': form})



## Función para gestionar el inicio de sesion
class CustomLoginView(LoginView):
    template_name = 'sesiones\login.html'
    
    def get_success_url(self):
        return '/'

## Función para controlar la modificación de un perfil+
@login_required
def editar_perfil(request):
    if request.method == 'POST':
        formulario = UserChangeForm(request.POST, isinstance=request.user)
        if formulario.is_valid():
            formulario.save()
            return redirect('home')
    else:
        form = UserChangeForm(isinstance = request.user)
    
    return render(request, 'sesiones/editar_perfil.html', {'form': formulario})