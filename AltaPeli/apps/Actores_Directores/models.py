from django.apps import apps
from django.db import models






# Create your models here.

# Modelo Director
class Director(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=255)
    fecha_nacimiento = models.DateField()

    def __str__(self):
        return f'{self.nombre} {self.apellido}'
    
    
# Modelo Actor
class Actor(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    edad = models.PositiveSmallIntegerField()

    def __str__(self):
        return f'{self.nombre} {self.apellido}'
    
    
    
    
