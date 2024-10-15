from django.contrib import admin

# Register your models here.
from apps.Peliculas_Series import models

admin.site.register(models.Genero)
admin.site.register(models.Tipo)
admin.site.register(models.PeliculaSerie)
admin.site.register(models.Reparto)
admin.site.register(models.Puntuacion)
admin.site.register(models.ActorPeliculaPremio)
admin.site.register(models.DirectorPeliculaPremio)