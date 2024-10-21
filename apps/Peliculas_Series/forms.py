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
        
    def __init__(self, *args, **kwargs):
        # Obtener Id
        usuario= kwargs.pop("usuario", None)
        pelicula_serie= kwargs.pop("pelicula_serie", None)
        
        super().__init__(*args, **kwargs)
        
        if usuario is not None:
            self.fields['usuario'].initial= usuario
            
        if pelicula_serie is not None:
            self.fields['pelicula_serie'].initial= pelicula_serie