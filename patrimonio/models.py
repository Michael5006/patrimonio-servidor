from django.db import models


class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre


class Lugar(models.Model):
    # ForeignKey: cada lugar pertenece a una categoría
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE,
        related_name='lugares',
    )
    nombre = models.CharField(max_length=150)
    direccion = models.CharField(max_length=200, blank=True)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre
