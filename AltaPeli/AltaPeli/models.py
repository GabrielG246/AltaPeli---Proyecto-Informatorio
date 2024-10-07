from django.db import models

# Modelo Categoría de Premio
class PremioCategoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

# Modelo Premio
class Premio(models.Model):
    nombre = models.CharField(max_length=255)
    categoria = models.ForeignKey(PremioCategoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre