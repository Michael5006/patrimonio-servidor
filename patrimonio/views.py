from rest_framework import viewsets

from .models import Categoria, Lugar
from .serializers import CategoriaSerializer, LugarSerializer


class CategoriaViewSet(viewsets.ModelViewSet):
    # ModelViewSet da el CRUD completo: listar, crear, ver, actualizar y eliminar
    queryset = Categoria.objects.all().order_by('id')
    serializer_class = CategoriaSerializer


class LugarViewSet(viewsets.ModelViewSet):
    queryset = Lugar.objects.select_related('categoria').order_by('id')
    serializer_class = LugarSerializer
