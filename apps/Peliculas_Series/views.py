from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, FormView, UpdateView
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Sum, Count, Avg

from .models import PeliculaSerie, Tipo
from .forms import FormularioCrearContenido, FormularioPuntuarContenido

from .models import Tipo, Genero, Puntuacion
from apps.Actores_Directores.models import Director


def permiso_de_administrador(user):
    return user.is_superuser or user.groups.filter(name='Contribuidores').exists()




# Create your views here.

def PeliculasSeriesView(request):
    contenido= PeliculaSerie.objects.all()
    peliculas= PeliculaSerie.objects.filter(tipo_id=1)
    series= PeliculaSerie.objects.filter(tipo_id=2)
    
    return render(request, 'peliculas_series/Listado.html')


# <==== CRUD CONTENIDO ADMINISTRADOR ====> #

# Vista CREATE Contenido (Contribuidor)
class AdminVistaCrearContenido(UserPassesTestMixin, CreateView):
    model= PeliculaSerie
    form_class= FormularioCrearContenido
    template_name= 'peliculas_series/AdminCrearContenido.html'
    success_url= reverse_lazy('comunidad')
    
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
    
    def test_func(self):
        return self.request.user.is_superuser or self.request.user.groups.filter(name='Contribuidores').exists()

# Vista DELETE Contenido (Contribuidor)
class AdminVistaEliminarContenido(UserPassesTestMixin, DeleteView):
    model= PeliculaSerie
    template_name= 'peliculas_series/AdminEliminarContenido.html'
    success_url= reverse_lazy('admin_listar_contenido')
    
    def test_func(self):
        return self.request.user.is_superuser or self.request.user.groups.filter(name='Contribuidores').exists()
    
    
# Vista READ Contenido (Contribuidor)
@user_passes_test(permiso_de_administrador)
def AdminVistaListarContenido(request):
    contenido= PeliculaSerie.objects.all()
    context= {'contenidos': contenido}
    return render(request, 'peliculas_series/AdminListarContenido.html', context)

# Vista UPDATE Contenido (Contribuidor)
class AdminVistaModificarContenido(UserPassesTestMixin, UpdateView):
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
    
    def test_func(self):
        return self.request.user.is_superuser or self.request.user.groups.filter(name='Contribuidores').exists()
    

# <==== VISUALIZACIÓN DE CONTENIDO (USUARIOS) ====> #

# Vista de Contenido (Usuario)
def VistaListarContenido(request, pk):
    contenido= PeliculaSerie.objects.filter(tipo_id=pk)
    tipo= Tipo.objects.filter(id=pk)
    

    
    context= {'contenidos': contenido, 'titulo': tipo}
    return render(request, 'peliculas_series/Listar_Contenido.html', context)

# Vista Detalle de Contenido (Usuario)
def VistaDetalleContenido(request, pk):
    contenido = PeliculaSerie.objects.get(id=pk)
    reseñas = Puntuacion.objects.filter(pelicula_serie=contenido)
    

    puntaje_promedio = Puntuacion.objects.filter(pelicula_serie=contenido).aggregate(promedio_puntaje=Avg('puntaje'))
    puntuacion = round(puntaje_promedio['promedio_puntaje']) if puntaje_promedio['promedio_puntaje'] is not None else 0
    
    if request.user.is_authenticated:
        usuario = request.user
    else: 
        usuario = 0

    context = {
        'contenido': contenido,
        'reseñas': reseñas,
        'puntuacion': puntuacion,
        'usuario': usuario
    }
    
    return render(request, 'peliculas_series/Detalle_Contenido.html', context)


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
        
        if reseña.usuario.id == self.request.user.id or self.request.user.is_superuser or self.request.user.groups.filter(name='Contribuidor').exists():
            return True

        return False
            
            
    

    
@login_required
def VistaModificarReseña(request, pk):
    reseña= Puntuacion.objects.get(id=pk)
    
    if not (request.user == reseña.usuario):
        #Por falta de tiempo solo va a redirigir al Home
        return redirect('PaginaPrincipal')
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


def buscar_pelicula_serie(request):
    query = request.GET.get('q')  # Obtenemos el término de búsqueda
    resultados = PeliculaSerie.objects.all()

    if query:
        resultados = resultados.filter(nombre__icontains=query)  # Filtrar por nombre que contenga el término de búsqueda

    return render(request, 'peliculas_series/resultados_busqueda.html', {'resultados': resultados, 'query': query})
