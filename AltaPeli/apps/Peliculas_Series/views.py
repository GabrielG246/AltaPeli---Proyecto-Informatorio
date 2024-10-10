from django.shortcuts import render



# Create your views here.
def PeliculasSeriesView(request):
    return render(request, 'peliculas_series/Listado.html')