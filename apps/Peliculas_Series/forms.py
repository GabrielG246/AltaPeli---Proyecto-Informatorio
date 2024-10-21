from django import forms
from .models import PeliculaSerie, Puntuacion


class FormularioCrearContenido(forms.ModelForm):
    class Meta:
        model= PeliculaSerie
        fields= [
            "nombre",
            "duracion",
            "anio_estreno",
            "director",
            "genero",
            "tipo",
            "portada_img",
            "trailer_url"
        ]
        
        
class FormularioPuntuarContenido(forms.ModelForm):
    class Meta:
        model= Puntuacion
        fields= [
            "usuario",
            "pelicula_serie",
            "puntaje",
            "comentario"
        ]
