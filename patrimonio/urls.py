from rest_framework.routers import DefaultRouter

from .views import CategoriaViewSet

# El router crea automáticamente las rutas del CRUD para cada ViewSet
router = DefaultRouter()
router.register('categorias', CategoriaViewSet)

urlpatterns = router.urls
