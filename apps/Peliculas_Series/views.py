from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, FormView, UpdateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Sum, Count

from .models import PeliculaSerie, Tipo
from .forms import FormularioCrearContenido, FormularioPuntuarContenido

from .models import Tipo, Genero, Puntuacion
from apps.Actores_Directores.models import Director




# Create your views here.

def PeliculasSeriesView(request):
    contenido= PeliculaSerie.objects.all()
    peliculas= PeliculaSerie.objects.filter(tipo_id=1)
    series= PeliculaSerie.objects.filter(tipo_id=2)
    
    return render(request, 'peliculas_series/Listado.html')


# <==== CRUD CONTENIDO ADMINISTRADOR ====> #

# Vista CREATE Contenido (Contribuidor)
class AdminVistaCrearContenido(CreateView):
    model= PeliculaSerie
    form_class= FormularioCrearContenido
    template_name= 'peliculas_series/AdminCrearContenido.html'
    success_url= reverse_lazy('admin_crear_contenido')
    
    def form_valid(self, form):
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)
    
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['tipos']= Tipo.objects.all()
        context['generos']= Genero.objects.all()
        context['directores']= Director.objects.all()
        return context

# Vista DELETE Contenido (Contribuidor)
class AdminVistaEliminarContenido(DeleteView):
    model= PeliculaSerie
    template_name= 'peliculas_series/AdminEliminarContenido.html'
    success_url= reverse_lazy('admin_listar_contenido')
    
    
# Vista READ Contenido (Contribuidor)
def AdminVistaListarContenido(request):
    contenido= PeliculaSerie.objects.all()
    context= {'contenidos': contenido}
    return render(request, 'peliculas_series/AdminListarContenido.html', context)

# Vista UPDATE Contenido (Contribuidor)
class AdminVistaModificarContenido(UpdateView):
    model= PeliculaSerie
    form_class= FormularioCrearContenido
    template_name= 'peliculas_series/AdminEditarContenido.html'
    success_url= reverse_lazy('admin_listar_contenido')
    
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        
        pk= self.kwargs['pk']
        contenido= PeliculaSerie.objects.get(id=pk)
        
        context['contenido']= contenido
        context['tipos']= Tipo.objects.all()
        context['generos']= Genero.objects.all()
        context['directores']= Director.objects.all()
        
        return context
    

# <==== VISUALIZACIÓN DE CONTENIDO (USUARIOS) ====> #

# Vista de Contenido (Usuario)
def VistaListarContenido(request, pk):
    contenido= PeliculaSerie.objects.filter(tipo_id=pk)
    tipo= Tipo.objects.filter(id=pk)
    

    
    context= {'contenidos': contenido, 'titulo': str(tipo[0])}
    return render(request, 'peliculas_series/Listar_Contenido.html', context)

# Vista Detalle de Contenido (Usuario)
def VistaDetalleContenido(request, pk):
    contenido= PeliculaSerie.objects.get(id=pk)
    reseñas= Puntuacion.objects.filter(pelicula_serie=contenido)
    puntaje_reseñas = Puntuacion.objects.filter(pelicula_serie=contenido).aggregate(total_puntaje=Sum('puntaje'))
    cant_reseñas = Puntuacion.objects.filter(pelicula_serie=contenido).aggregate(total_reseñas=Count('id'))
    
    total_puntaje = puntaje_reseñas['total_puntaje'] or 0
    total_reseñas = cant_reseñas['total_reseñas'] or 1
    
    puntuacion= round(total_puntaje/total_reseñas)
    
    usuario= request.user

    context= {
        'contenido': contenido,
        'reseñas': reseñas,
        'puntuacion': puntuacion,
        'usuario': usuario
        }
    
    return render(request, 'peliculas_Series/Detalle_Contenido.html', context)


# <==== CRUD EVENTO ====> #

# Vista CREATE Evento (Usuario Requerido)
@login_required
def VistaPuntuarContenido(request, pk):
    contenido = get_object_or_404(PeliculaSerie, id=pk)
    puntuado = Puntuacion.objects.filter(usuario=request.user, pelicula_serie=contenido).exists()

    puntuacion= None

    if puntuado:
        puntuacion= Puntuacion.objects.get(usuario=request.user, pelicula_serie=contenido)

    if request.method == 'POST':
        
        data= request.POST.copy()
        data['usuario']= request.user
        data['pelicula_serie']= contenido
        data['puntaje']= int(request.POST.get('puntaje'))
        data['comentario']= request.POST.get('comentario')
        
    
        form = FormularioPuntuarContenido(data)
        if form.is_valid():
            nueva_puntuacion = form.save(commit=False)
            nueva_puntuacion.save()
            
            return redirect('PaginaPrincipal')

    form = FormularioPuntuarContenido()

    context = {
        'contenido': contenido,
        'puntuado': puntuado,
        'form': form,
        'puntuacion': puntuacion
    }
    return render(request, 'peliculas_series/Puntuar_Contenido.html', context)

# Vista READ Evento (Usuario Requerido)

# Vista DELETE Evento (Usuario Requerido)
class VistaEliminarReseña(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model= Puntuacion
    template_name= 'peliculas_series/Eliminar_Reseña.html'
    success_url= reverse_lazy('PaginaPrincipal')
        
    
    def test_func(self):
        # Captura de Parámetros
        pk= self.kwargs.get('pk')
        
        reseña= Puntuacion.objects.get(id=pk)
        
        if reseña.usuario.id == self.request.user.id:
            return True
        return False
            

def VistaModificarReseña(request, pk):
    reseña= Puntuacion.objects.get(id=pk)
    
    
    if request.method == 'POST':
        post_data= request.POST.copy()
        
        post_data['usuario']= reseña.usuario
        post_data['pelicula_serie']= reseña.pelicula_serie
        post_data['puntaje']= int(post_data['puntaje'])
        post_data['comentario']= post_data['comentario']
        
        
        form = FormularioPuntuarContenido(post_data, instance=reseña)
        
        if form.is_valid():
            form.save()
            return redirect('PaginaPrincipal')

    else:
        
        form = FormularioPuntuarContenido(instance=reseña)
        

    return render(request, 'peliculas_series/Modificar_Reseña.html', {'form':form, 'reseña': reseña})

# Vista Comunidad (Evento)
def VistaComunidad(request):
    
    reseñas= Puntuacion.objects.select_related('usuario', 'pelicula_serie').all()
    usuario= request.user
    
    context={
        "reseñas": reseñas,
        "usuario": usuario
    }
    
    return render(request, "peliculas_series/VistaComunidad.html", context)