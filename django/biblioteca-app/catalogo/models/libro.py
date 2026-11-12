from django.db import models
from .categoria import Categoria
from catalogo.models.autor import Autor

class Libro(models.Model):
    titulo= models.CharField(max_length=200)
    autores= models.ManyToManyField(
        Autor,
        related_name='libros',
        blank=True
    )
    fecha_publicacion = models.DateField()
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    isbn = models.CharField(max_length=100)

    def __str__(self):
        return self.titulo

    class Meta: 
        verbose_name_plural = "libros"
        verbose_name = "libro"
        ordering =['titulo']