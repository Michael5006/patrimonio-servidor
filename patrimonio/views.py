from rest_framework import viewsets

from .models import Categoria
from .serializers import CategoriaSerializer


class CategoriaViewSet(viewsets.ModelViewSet):
    # ModelViewSet da el CRUD completo: listar, crear, ver, actualizar y eliminar
    queryset = Categoria.objects.all().order_by('id')
    serializer_class = CategoriaSerializer
