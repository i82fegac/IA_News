from django.urls import path
from . import views

urlpatterns = [
    path('tutoriales/', views.lista_tutoriales, name='lista_tutoriales'),
]
