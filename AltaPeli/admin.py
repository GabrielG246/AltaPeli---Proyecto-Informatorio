from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Premio, PremioCategoria

# Register your models here.
admin.site.register(Premio)
admin.site.register(PremioCategoria)



