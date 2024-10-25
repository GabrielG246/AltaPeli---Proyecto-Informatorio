from django.urls import path
from . import views


urlpatterns = [
    # URLS de Contenido Público
    path('<int:pk>/', views.VistaListarContenido, name="listar_contenido"),
    path('comunidad/', views.VistaComunidad, name='comunidad'),
    path('detalle_contenido/<int:pk>/', views.VistaDetalleContenido, name="detalle_contenido"),
    
    #URLS de Administrador/Contribuidor
    path('crear_contenido/', views.AdminVistaCrearContenido.as_view(), name="admin_crear_contenido"),
    path('eliminar_contenido/<int:pk>/', views.AdminVistaEliminarContenido.as_view(), name="admin_eliminar_contenido"),
    path('modificar_contenido/<int:pk>/', views.AdminVistaModificarContenido.as_view(), name="admin_modificar_contenido"),
    path('listado_contenido/', views.AdminVistaListarContenido, name="admin_listar_contenido"),
    
    #URLS de Reseñas (Usuarios y Administradores/Contribuidores)
    path('crear_resena/<int:pk>/', views.VistaPuntuarContenido, name="crear_resena"),
    path('eliminar_resena/<int:pk>/', views.VistaEliminarReseña.as_view(), name="eliminar_resena"),
    
    #URLS de Reseñas (Usuarios)
    path('editar_resena/<int:pk>/', views.VistaModificarReseña, name="editar_resena"),
]