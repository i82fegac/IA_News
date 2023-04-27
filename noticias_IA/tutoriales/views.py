from django.shortcuts import render
from .models import Tutorial

def lista_tutoriales(request):
    tutoriales = Tutorial.objects.all()
    return render(request, 'lista_tutoriales.html', {'tutoriales': tutoriales})
