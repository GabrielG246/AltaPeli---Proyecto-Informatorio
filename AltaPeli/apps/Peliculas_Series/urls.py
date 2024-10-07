from django.urls import path
from .views import PeliculasSeriesView


urlpatterns = [
    path('', PeliculasSeriesView),
]