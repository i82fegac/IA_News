from django.db import models

# Create your models here.
class Etiqueta(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
    
class Articulo(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    etiquetas = models.CharField(max_length=100, default='Sin etiquetas')

    def __str__(self) -> str:
        return self.titulo
    
    