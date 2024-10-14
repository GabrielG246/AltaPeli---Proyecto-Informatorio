from django.urls import path
from . import views


urlpatterns = [
    path('', views.PeliculasSeriesView),
    path('crear_contenido/', views.VistaCrearContenido.as_view(), name="crear_contenido")
]