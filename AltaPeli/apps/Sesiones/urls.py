from django.urls import path
from .views import SesionesView


urlpatterns = [
    path('', SesionesView),
]