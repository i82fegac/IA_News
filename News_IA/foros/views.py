from django.shortcuts import render, get_object_or_404, redirect
from .models import Tema, Comentario
from .forms import TemaForm, ComentarioForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def lista_temas(request):
    temas = Tema.objects.all().order_by('-fecha_creacion')
    return render(request, 'lista_temas.html', {'temas': temas})

@login_required
def crear_tema(request):
    if request.method == 'POST':
        form = TemaForm(request.POST)
        if form.is_valid():
            tema = form.save(commit=False)
            tema.creador = request.user
            tema.save()
            return redirect('lista_temas')
    else:
        form = TemaForm()
    return render(request, 'crear_tema.html', {'form': form})

def detalle_tema(request, tema_id):
    tema = get_object_or_404(Tema, id=tema_id)
    comentarios = tema.comentarios.order_by('fecha_publicacion')
    return render(request, 'detalle_tema.html', {'tema': tema, 'comentarios': comentarios})

@login_required
def crear_comentario(request, tema_id):
    tema = get_object_or_404(Tema, id=tema_id)
    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.autor = request.user
            comentario.tema = tema
            comentario.save()
            return redirect('detalle_tema', tema_id=tema_id)
    else:
        form = ComentarioForm()
    return render(request, 'crear_comentario.html', {'form': form, 'tema': tema})