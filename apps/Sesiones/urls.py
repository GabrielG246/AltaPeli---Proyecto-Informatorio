from django.urls import path
from . import views
from .views import CustomLoginView, editar_perfil



urlpatterns = [
    path('registro/', views.registroUsuarios, name = 'registro'),
    path('login/', CustomLoginView.as_view(), name = 'login')    ,
    path('editar_perfil/', editar_perfil, name='editar_perfil')
]