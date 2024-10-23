from django.urls import path
from . import views


urlpatterns = [
    path('<int:pk>/', views.VistaListarContenido, name="listar_contenido"),
    path('crear_contenido/', views.AdminVistaCrearContenido.as_view(), name="admin_crear_contenido"),
    path('eliminar_contenido/<int:pk>/', views.AdminVistaEliminarContenido.as_view(), name="admin_eliminar_contenido"),
    path('modificar_contenido/<int:pk>/', views.AdminVistaModificarContenido.as_view(), name="admin_modificar_contenido"),
    path('listado_contenido/', views.AdminVistaListarContenido, name="admin_listar_contenido"),
    path('detalle_contenido/<int:pk>/', views.VistaDetalleContenido, name="detalle_contenido"),
    path('crear_reseña/<int:pk>/', views.VistaPuntuarContenido, name="crear_reseña"),
    path('editar_reseña/<int:pk>/', views.VistaPuntuarContenido, name="editar_reseña"),
    path('comunidad/', views.VistaComunidad, name='comunidad')
]