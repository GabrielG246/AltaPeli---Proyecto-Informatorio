from django.urls import path
from django.conf import settings
from django.contrib.auth.views import LogoutView
from django.conf.urls.static import static
from . import views



urlpatterns = [
    path('registro/', views.registro, name = 'registro'),
    path('login/', views.login_usuario, name='login'),
    path('perfil/', views.perfil_usuario, name='perfil'),
    path('editar_perfil/', views.editar_perfil, name='editar_perfil'),
    path('logout/', LogoutView.as_view(next_page='login') , name='logout')]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)