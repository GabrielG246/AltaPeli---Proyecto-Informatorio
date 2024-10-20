# Librerias para registro
from django.shortcuts import render, redirect
from .forms import FormularioRegistroUsuario, FormularioInicioSesion, FormularioPerfilUsuario
#Librerias para Login
from django.contrib.auth import authenticate, login
#Librerias para el perfil de usuario
from django.contrib.auth.decorators import login_required


## Función para gestionar el registro de usuarios.
def registro(request):
    if request.method == 'POST':
        print("se lo damos en 3")
        form = FormularioRegistroUsuario(request.POST, request.FILES)
        if form.is_valid():
            print("Yacasi")
            form.save()
            usuario = form.cleaned_data.get('usuario')
            print("Espera")
            return redirect('login')
    else:
        print("pinchó")
        form = FormularioRegistroUsuario()
        
    print("Falla del sistema")
    return render(request, 'sesiones/registro.html', {'form': form})

def login_usuario(request):
    if request.method == 'POST':
        form = FormularioInicioSesion(request.POST)
        if form.is_valid():
            usuario = form.cleaned_data['usuario']
            password = form.cleaned_data['password']
            
            print("Ya casi!")
            user = authenticate(request, usuario=usuario, password=password)
            print("Un poco más!")
            if user is not None:
                print ("Error de autenticación")
                login(request, user)
                print(f"Bienvenido! {usuario}")
                return redirect('perfil')
    else:
        form = FormularioInicioSesion()
        print("No pasa nada")
    
    print("Algo salio mal :(")
    return render(request, 'sesiones/login.html', {'form': form})

@login_required
def perfil_usuario(request):
    return render(request, 'sesiones/perfil.html', {'user': request.user})

@login_required
def editar_perfil(request):
    print(f"Hola! Request method: {request.method}")  # Verifica si el método es POST
    user = request.user
    
    if request.method == 'POST':
        form = FormularioPerfilUsuario(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('perfil')
        else:
            return render(request, 'sesiones/editar_perfil.html', {'form': form})
    else:
        form = FormularioPerfilUsuario(instance=user)
    
    return render(request, 'sesiones/editar_perfil.html', {'form':form})