from django import forms
from .models import PeliculaSerie

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