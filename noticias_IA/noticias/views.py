from django.shortcuts import render
from .models import Noticia
from .api import obtener_noticias_ia




def lista_noticias(request):
    noticias = obtener_noticias_ia()
    
    context = {
        'noticias': noticias
    }
    
    return render(request, 'lista_noticias.html', context)

