from django.shortcuts import render
from apps.Peliculas_Series.models import PeliculaSerie, Puntuacion
from django.db.models import Sum, Count, Avg

def Inicio_View(request):
    reseñas= Puntuacion.objects.order_by('?')[:3]
    
    mejores_peliculas = PeliculaSerie.objects.filter(tipo=1).annotate(promedio_puntuacion=Avg('puntuacion__puntaje')).order_by('-promedio_puntuacion')[:4]
    mejores_series = PeliculaSerie.objects.filter(tipo=2).annotate(promedio_puntuacion=Avg('puntuacion__puntaje')).order_by('-promedio_puntuacion')[:4]
    
    
    permiso= request.user.is_superuser or request.user.groups.filter(name="Contribuidores")  
    
    print(permiso)  
    context={'peliculas': mejores_peliculas, 'series': mejores_series, 'reseñas': reseñas, 'admin': permiso}    
    return render(request, 'index.html', context)