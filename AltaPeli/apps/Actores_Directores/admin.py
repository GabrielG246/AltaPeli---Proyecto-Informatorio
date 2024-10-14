from django.contrib import admin

from .models import Director, Actor

# Register your models here.
admin.site.register(Actor)
admin.site.register(Director)
