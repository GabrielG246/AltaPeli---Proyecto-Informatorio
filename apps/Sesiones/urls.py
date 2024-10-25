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
    path('logout/', LogoutView.as_view(next_page='login') , name='logout'),
    path('admin_lista_usuarios', views.admin_listar_usuarios, name='admin_usuarios'),
    path('admin_agregar_contribuidor/<int:pk>/', views.agregar_a_contribuidores, name="agregar_contribuidor"),
    path('admin_eliminar_contribuidor/<int:pk>/', views.eliminar_de_contribuidores, name="eliminar_contribuidor"),
    path('admin_activar_usuario/<int:pk>/', views.activar_usuario, name="activar_usuario"),
    path('admin_desactivar_usuario/<int:pk>/', views.desactivar_usuario, name="desactivar_usuario"),
    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)