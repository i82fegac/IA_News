from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Articulo, Etiqueta
from .forms import ArticuloForm

def lista_articulos(request):
    articulos = Articulo.objects.all().order_by('-fecha_publicacion')
    return render(request, 'lista_articulos.html', {'articulos': articulos})

def detalle_articulo(request, pk):
    articulo = get_object_or_404(Articulo, pk=pk)
    return render(request, 'detalle_articulo.html', {'articulo': articulo})

@login_required
def crear_articulo(request):
    if request.method == 'POST':
        form = ArticuloForm(request.POST)
        if form.is_valid():
            articulo = form.save(commit=False)
            articulo.autor = request.user
            articulo.save()
            form.save_m2m()
            return redirect('detalle_articulo', pk=articulo.pk)
    else:
        form = ArticuloForm()
    return render(request, 'crear_articulo.html', {'form': form})

@login_required
def editar_articulo(request, pk):
    articulo = get_object_or_404(Articulo, pk=pk)

    if request.user != articulo.autor:
        return redirect('detalle_articulo', pk=articulo.pk)

    if request.method == 'POST':
        form = ArticuloForm(request.POST, instance=articulo)
        if form.is_valid():
            articulo = form.save(commit=False)
            articulo.save()
            form.save_m2m()
            return redirect('detalle_articulo', pk=articulo.pk)
    else:
        form = ArticuloForm(instance=articulo)
    return render(request, 'editar_articulo.html', {'form': form, 'articulo': articulo})

@login_required
def eliminar_articulo(request, pk):
    articulo = get_object_or_404(Articulo, pk=pk)

    if request.user != articulo.autor:
        return redirect('detalle_articulo', pk=articulo.pk)

    if request.method == 'POST':
        articulo.delete()
        return redirect('lista_articulos')
    return render(request, 'eliminar_articulo.html', {'articulo': articulo})
