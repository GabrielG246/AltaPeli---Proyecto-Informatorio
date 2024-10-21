from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, FormView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import PeliculaSerie, Tipo
from .forms import FormularioCrearContenido, FormularioPuntuarContenido

from .models import Tipo, Genero, Puntuacion
from apps.Actores_Directores.models import Director



# Create your views here.
def PeliculasSeriesView(request):
    contenido= PeliculaSerie.objects.all()
    peliculas= PeliculaSerie.objects.filter(tipo_id=1)
    series= PeliculaSerie.objects.filter(tipo_id=2)
    
    print(peliculas)
    print(series)
    return render(request, 'peliculas_series/Listado.html')

# Vista para Formulario (CrearContenido)
class AdminVistaCrearContenido(CreateView):
    model= PeliculaSerie
    form_class= FormularioCrearContenido
    template_name= 'peliculas_series/AdminCrearContenido.html'
    success_url= reverse_lazy('admin_crear_contenido')
    
    def form_valid(self, form):
        return super().form_valid(form)

    def form_invalid(self, form):
        # Aquí puedes imprimir los errores o hacer un logging
        print(form.errors)
        return super().form_invalid(form)
    
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['tipos']= Tipo.objects.all()
        context['generos']= Genero.objects.all()
        context['directores']= Director.objects.all()
        return context
    
    
class AdminVistaEliminarContenido(DeleteView):
    model= PeliculaSerie
    template_name= 'peliculas_series/AdminEliminarContenido.html'
    success_url= reverse_lazy('admin_listar_contenido')
    
    
def AdminVistaListarContenido(request):
    contenido= PeliculaSerie.objects.all()
    context= {'contenidos': contenido}
    return render(request, 'peliculas_series/AdminListarContenido.html', context)

def VistaListarContenido(request, pk):
    contenido= PeliculaSerie.objects.filter(tipo_id=pk)
    tipo= Tipo.objects.filter(id=pk)

    
    context= {'contenidos': contenido, 'titulo': str(tipo[0])}
    return render(request, 'peliculas_series/Listar_Contenido.html', context)

def VistaDetalleContenido(request, pk):
    contenido= PeliculaSerie.objects.get(id=pk)

    context= {'contenido': contenido}
    
    return render(request, 'peliculas_Series/Detalle_Contenido.html', context)


class VistaPuntuarContenido(LoginRequiredMixin, FormView):
    model= Puntuacion
    form_class= FormularioPuntuarContenido
    template_name= 'peliculas_Series/Puntuar_Contenido.html'
    success_url= reverse_lazy("PaginaPrincipal")

    
    def get_context_data(self, **kwargs):
        # Obtener Contexto
        context= super().get_context_data(**kwargs)
        
        # Capturar Id de Usuario y Id de Contenido
        usuario_id= self.request.user.id
        contenido_id= self.kwargs.get("pk")
        
        # Consultar Contenido
        contenido= PeliculaSerie.objects.get(id=contenido_id)
        esta_puntuado= Puntuacion.objects.filter(usuario=usuario_id, pelicula_serie=contenido_id).exists()
        
        if esta_puntuado:
            puntuacion= Puntuacion.objects.get(usuario=usuario_id, pelicula_serie=contenido_id)
            context["puntuacion"]= puntuacion
        
        # Asignar Contenido como Contexto
        context["contenido"]= contenido
        context["puntuado"]= esta_puntuado
        
        return context
    

    def get_form_kwargs(self):
        kwargs= super().get_form_kwargs()
        
        kwargs["usuario"]= self.request.user.id
        kwargs["pelicula_serie"]= self.kwargs.get("pk")
        
        return kwargs
        
def VistaComunidad(request):
    
    reseñas= Puntuacion.objects.select_related('usuario', 'pelicula_serie').all()
    
    context={
        "reseñas": reseñas
    }
    
    return render(request, "peliculas_series/VistaComunidad.html", context)