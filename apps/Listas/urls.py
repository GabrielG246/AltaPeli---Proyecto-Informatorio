from django.urls import path
from .views import ListasView


urlpatterns = [
    path('', ListasView),
]