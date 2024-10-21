from django.urls import path
from . import views


urlpatterns = [
    path('<int:pk>/', views.VistaListarContenido, name="listar_contenido"),
    path('crear_contenido/', views.AdminVistaCrearContenido.as_view(), name="admin_crear_contenido"),
    path('eliminar_contenido/<int:pk>/', views.AdminVistaEliminarContenido.as_view(), name="admin_eliminar_contenido"),
    path('listado_contenido/', views.AdminVistaListarContenido, name="admin_listar_contenido"),
    path('detalle_contenido/<int:pk>/', views.VistaDetalleContenido, name="detalle_contenido"),
    path('puntuar_contenido/<int:pk>/', views.VistaPuntuarContenido, name="puntuar_contenido"),
    path('comunidad/', views.VistaComunidad, name='comunidad')
]