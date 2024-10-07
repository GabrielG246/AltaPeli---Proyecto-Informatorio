from django.urls import path
from .views import ActoresDirectoresView


urlpatterns = [
    path('', ActoresDirectoresView),
]