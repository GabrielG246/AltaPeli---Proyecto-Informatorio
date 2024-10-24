from django.shortcuts import render, get_object_or_404, redirect
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
    puntuaciones = Puntuacion.objects.filter(pelicula_serie=contenido)

    if request.method == 'POST':
        puntuacion_id = request.POST.get('puntuacion_id')
        puntuacion = get_object_or_404(Puntuacion, id=puntuacion_id, usuario=request.user)
        puntuacion.delete()
        return redirect('detalle_contenido', id=pk)
    
    context= {
        'contenido': contenido,
        'puntuaciones': puntuaciones,
        }
    
    return render(request, 'peliculas_Series/Detalle_Contenido.html', context)




@login_required
def VistaPuntuarContenido(request, pk):
    contenido = get_object_or_404(PeliculaSerie, id=pk)
    puntuado = Puntuacion.objects.filter(usuario=request.user, pelicula_serie=contenido).exists()

    print(f"Esta Puntuado { puntuado }")

    puntuacion= None

    if puntuado:
        puntuacion= Puntuacion.objects.get(usuario=request.user, pelicula_serie=contenido)
        print(puntuacion.puntaje)
        print(puntuacion.comentario)

    if request.method == 'POST':
        
        data= request.POST.copy()
        data['usuario']= request.user
        data['pelicula_serie']= contenido
        data['puntaje']= int(request.POST.get('puntaje'))
        data['comentario']= request.POST.get('comentario')
        
    
            # Si no puntuó, crea una nueva puntuación
        form = FormularioPuntuarContenido(data)
        if form.is_valid():
            nueva_puntuacion = form.save(commit=False)
            nueva_puntuacion.save()
            
            return redirect('detalle_contenido', pk=contenido.pk)  # Cambia esto por la vista a la que quieres redirigir

    # Si no es un POST, muestra el formulario con la puntuación existente (si hay)
    form = FormularioPuntuarContenido()

    context = {
        'contenido': contenido,
        'puntuado': puntuado,
        'form': form,
        'puntuacion': puntuacion
    }
    return render(request, 'peliculas_series/Puntuar_Contenido.html', context)

        
def VistaComunidad(request):
    
    reseñas= Puntuacion.objects.select_related('usuario', 'pelicula_serie').all()
    
    context={
        "reseñas": reseñas
    }
    
    return render(request, "peliculas_series/VistaComunidad.html", context)


def buscar_pelicula_serie(request):
    query = request.GET.get('q')  # Obtenemos el término de búsqueda
    resultados = PeliculaSerie.objects.all()

    if query:
        resultados = resultados.filter(nombre__icontains=query)  # Filtrar por nombre que contenga el término de búsqueda

    return render(request, 'peliculas_series/resultados_busqueda.html', {'resultados': resultados, 'query': query})
