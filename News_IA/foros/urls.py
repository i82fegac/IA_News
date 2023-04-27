from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_temas, name='lista_temas'),
    path('crear/', views.crear_tema, name='crear_tema'),
    path('<int:tema_id>/', views.detalle_tema, name='detalle_tema'),
    path('<int:tema_id>/comentar/', views.crear_comentario, name='crear_comentario'),
]