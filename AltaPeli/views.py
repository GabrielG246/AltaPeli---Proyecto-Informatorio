from django.shortcuts import render
from apps.Peliculas_Series.models import PeliculaSerie

def Inicio_View(request):
    
    contenidos= PeliculaSerie.objects.order_by('?')[:5]
    peliculas= PeliculaSerie.objects.filter(tipo_id=1)
    series= PeliculaSerie.objects.filter(tipo_id=2)
    
    context={'contenidos': contenidos, 'peliculas': peliculas, 'series': series}    
    return render(request, 'index.html', context)