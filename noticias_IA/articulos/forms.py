from django import forms
from .models import Articulo, Etiqueta

class ArticuloForm(forms.ModelForm):
    class Meta:
        model = Articulo
        fields = ['titulo', 'contenido', 'etiquetas']
