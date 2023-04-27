from django.urls import path
from . import views

urlpatterns = [
    path('guias/', views.lista_guias, name='lista_guias'),
]
