from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView
from .models import PeliculaSerie, Tipo
from .forms import FormularioCrearContenido

from .models import Tipo, Genero
from apps.Actores_Directores.models import Director



# Create your views here.
def PeliculasSeriesView(request):
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
    
    context= {'contenido': contenido, 'titulo': tipo[0]}
    return render(request, 'peliculas_series/Listar_Contenido.html', context)