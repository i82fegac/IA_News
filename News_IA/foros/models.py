from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Tema(models.Model):
    titulo = models.CharField(max_length=255)
    descripcion = models.TextField()
    creador = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

class Comentario(models.Model):
    texto = models.TextField()
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    tema = models.ForeignKey(Tema, related_name='comentarios', on_delete=models.CASCADE)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.texto[:50] + "..."