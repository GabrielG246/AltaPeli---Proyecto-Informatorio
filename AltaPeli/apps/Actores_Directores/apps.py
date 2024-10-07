from django.apps import AppConfig


class ActoresDirectoresConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.Actores_Directores'

    def ready(self):
        # Este método se ejecuta cuando la aplicación ya está completamente cargada
        from django.apps import apps
        PeliculaSerie = apps.get_model('Peliculas_Series', 'PeliculaSerie')
        Premio = apps.get_model('AltaPeli', 'Premio')
        # Ahora puedes usar PeliculaSerie de forma segura