from django import forms
from .models import Tema, Comentario

class TemaForm(forms.ModelForm):
    class Meta:
        model = Tema
        fields = ['titulo', 'descripcion']

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['texto']