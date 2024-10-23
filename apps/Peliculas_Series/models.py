from django.db import models

from apps.Actores_Directores.models import Director
from apps.Actores_Directores.models import Actor
from AltaPeli.models import Premio
from django.contrib.auth.models import User

##Resolución de conflicto
from django.conf import settings


# Create your models here.

# Modelo Genero
class Genero(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
    
    
# Modelo Tipo
class Tipo(models.Model):
    nombre = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre
    

# Modelo Pelicula/Serie
class PeliculaSerie(models.Model):
    nombre = models.CharField(max_length=255, blank=False)
    tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE, blank=False)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE, blank=False)
    duracion = models.IntegerField(default=0)
    anio_estreno = models.DateField()
    director = models.ForeignKey(Director, on_delete=models.CASCADE, blank=False)
    trailer_url= models.URLField(
        max_length=500,
        default="https://altapelibucket.s3.us-east-2.amazonaws.com/RickRoll.mp4",
        blank=True
        )
    portada_img= models.ImageField(
        upload_to="peliculas/",
        blank=True,
        null=True,
        default="peliculas/Pelicula_Default.png"
    )

    def __str__(self):
        return self.nombre
    

# Modelo Reparto (Tabla Intermedia entre Peliculas y Actores)
class Reparto(models.Model):
    pelicula_serie = models.ForeignKey(PeliculaSerie, on_delete=models.CASCADE)
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE)
    
    
# Modelo Puntuación (Tabla Intermedia entre Peliculas y Usuario)
class Puntuacion(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    pelicula_serie = models.ForeignKey(PeliculaSerie, on_delete=models.CASCADE)
    puntaje = models.IntegerField()
    comentario = models.TextField(max_length=400)
    
    class Meta:
        unique_together = ('usuario', 'pelicula_serie')

    def __str__(self):
        return f'Puntuación de {self.usuario} para {self.pelicula_serie}'
    
    
# Tabla Intermedia entre Actor, Premio y Película
class ActorPeliculaPremio(models.Model):
    pelicula = models.ForeignKey(PeliculaSerie, on_delete=models.CASCADE)
    premio = models.ForeignKey(Premio, on_delete=models.CASCADE)
    
    
    
    
# Tabla Intermedia entre Director, Premio y Película
class DirectorPeliculaPremio(models.Model):
    pelicula = models.ForeignKey(PeliculaSerie, on_delete=models.CASCADE)
    premio = models.ForeignKey(Premio, on_delete=models.CASCADE)