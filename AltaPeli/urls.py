"""
URL configuration for AltaPeli project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings

from .views import Inicio_View, About_Us


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Inicio_View, name="PaginaPrincipal"),
    path('sesiones/', include('apps.Sesiones.urls')),
    path('listas/', include('apps.Listas.urls')),
    path('peliculas_series/', include('apps.Peliculas_Series.urls')),
    path('actores_directores/', include('apps.Actores_Directores.urls')),
    path( 'about_us/', About_Us, name='about_us')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT, show_indexes=True)
