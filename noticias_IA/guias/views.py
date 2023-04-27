from django.shortcuts import render
from .models import Guia

def lista_guias(request):
    guias = Guia.objects.all()
    return render(request, 'lista_guias.html', {'guias': guias})
