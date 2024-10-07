from django.db import models
from apps.Peliculas_Series.models import PeliculaSerie
from .models import User

# Create your models here.

class TipoLista(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class ListaPeliculas(models.Model):
    pelicula = models.ForeignKey(PeliculaSerie, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    lista = models.ForeignKey(TipoLista, on_delete=models.CASCADE)