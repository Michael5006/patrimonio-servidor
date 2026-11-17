from rest_framework import serializers

from .models import Categoria, Lugar


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['id', 'nombre', 'descripcion']


class LugarSerializer(serializers.ModelSerializer):
    # Campo de solo lectura para mostrar el nombre de la categoría en el cliente
    categoria_nombre = serializers.ReadOnlyField(source='categoria.nombre')

    class Meta:
        model = Lugar
        fields = ['id', 'nombre', 'direccion', 'descripcion', 'categoria', 'categoria_nombre']
