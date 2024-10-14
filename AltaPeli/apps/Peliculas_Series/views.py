from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .models import PeliculaSerie
from .forms import FormularioCrearContenido

from .models import Tipo, Genero
from apps.Actores_Directores.models import Director



# Create your views here.
def PeliculasSeriesView(request):
    return render(request, 'peliculas_series/Listado.html')

# Vista para Formulario (CrearContenido)
class VistaCrearContenido(CreateView):
    model= PeliculaSerie
    form_class= FormularioCrearContenido
    template_name= 'peliculas_series/CrearContenido.html'
    success_url= reverse_lazy('PaginaPrincipal')
    
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
    