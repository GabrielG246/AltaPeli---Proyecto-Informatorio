# Librerias para registro
from django.shortcuts import render, redirect, get_object_or_404
from .forms import FormularioRegistroUsuario, FormularioInicioSesion, FormularioPerfilUsuario
from django.contrib import messages
#Librerias para Login
from django.contrib.auth import authenticate, login
#Librerias para el perfil de usuario
from django.contrib.auth.decorators import login_required, user_passes_test
from apps.Peliculas_Series.models import Puntuacion
from .models import User
from django.contrib.auth.models import Group


def permiso_de_administrador(user):
    return user.is_superuser or user.groups.filter(name='Contribuidores').exists()



## Función para gestionar el registro de usuarios.
def registro(request):
    if request.method == 'POST':
        form = FormularioRegistroUsuario(request.POST, request.FILES)
        if form.is_valid():

            form.save()
            usuario = form.cleaned_data.get('usuario')

            messages.success(request, 'Registro Exitoso! Inicia sesión.')
            return redirect('login')
        else:
            print("Errores en el formulario:", form.errors)
            for error in form.errors.values():
                messages.error(request, error)
                print(f"Error: {error}")
    else:

        form = FormularioRegistroUsuario()
        

    return render(request, 'sesiones/registro.html', {'form': form})

def login_usuario(request):
    if request.method == 'POST':
        form = FormularioInicioSesion(request.POST)
        if form.is_valid():
            usuario = form.cleaned_data['usuario']
            password = form.cleaned_data['password']
            

            user = authenticate(request, usuario=usuario, password=password)

            if user is not None:

                login(request, user)
                print(f"Bienvenido! {usuario}")
                return redirect('perfil')
    else:
        form = FormularioInicioSesion()

    

    return render(request, 'sesiones/login.html', {'form': form})

@login_required
def perfil_usuario(request):
    # Obtener todas las reseñas del usuario actual
    puntuaciones = Puntuacion.objects.filter(usuario=request.user).select_related('pelicula_serie')
    
        
    # Manejar la eliminación de una reseña
    if request.method == 'POST':
        puntuacion_id = request.POST.get('puntuacion_id')
        puntuacion = get_object_or_404(Puntuacion, id=puntuacion_id, usuario=request.user)
        puntuacion.delete()
        return redirect('perfil') 
    
    return render(request, 'sesiones/perfil.html', {
        'user': request.user, 'puntuaciones': puntuaciones,
    })

@login_required
def editar_perfil(request):
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



@login_required
@user_passes_test(permiso_de_administrador)
def admin_listar_usuarios(request):
    usuarios= User.objects.all()
    
    return render(request, 'sesiones/lista_usuarios.html', {'usuarios': usuarios})


#=== LÓGICA PARA CONTRIBUIDORES ===#
@login_required
@user_passes_test(permiso_de_administrador)
def agregar_a_contribuidores(request, pk):
    usuario= User.objects.get(id=pk)
    grupo= Group.objects.get(name="Contribuidores")
    grupo.user_set.add(usuario)
    return redirect("admin_usuarios")

@login_required
@user_passes_test(permiso_de_administrador)
def eliminar_de_contribuidores(request, pk):
    usuario= User.objects.get(id=pk)
    grupo= Group.objects.get(name="Contribuidores")
    grupo.user_set.remove(usuario)
    return redirect("admin_usuarios")


#=== LÓGICA PARA USUARIOS ===#
@login_required
@user_passes_test(permiso_de_administrador)
def activar_usuario(request, pk):
    usuario= User.objects.get(id=pk)
    usuario.is_active= True
    usuario.save()
    return redirect("admin_usuarios")

@login_required
@user_passes_test(permiso_de_administrador)
def desactivar_usuario(request, pk):
    usuario= User.objects.get(id=pk)
    usuario.is_active= False
    usuario.save()
    return redirect("admin_usuarios")