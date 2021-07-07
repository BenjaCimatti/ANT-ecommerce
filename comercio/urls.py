from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

# urlpatterns = [
#     path('producto/', ProductoViewSet.as_view({'get': 'list'})),
#     path('marca/', MarcaViewSet.as_view({'get': 'list'})),
#     path('categoria/', CategoriaViewSet.as_view({'get': 'list'})),
#     path('proveedor/', ProveedorViewSet.as_view({'get': 'list'})),
#     path('stock/', StockViewSet.as_view({'get': 'list'})),
#     path('carrito/', CarritoViewSet.as_view({'get': 'list'})),
#     path('producto-agregado/', ProductoAgregadoViewSet.as_view({'get': 'list'}))
# ]

router = DefaultRouter()
router.register("producto", ProductoViewSet, basename="producto")
router.register("marca", MarcaViewSet, basename="marca")
router.register("categoria", CategoriaViewSet, basename="categoria")
router.register("proveedor", ProveedorViewSet, basename="proveedor")
router.register("stock", StockViewSet, basename="stock")
router.register("carrito", CarritoViewSet, basename="carrito")
router.register("producto-agregado", ProductoAgregadoViewSet, basename="producto-agregado")

urlpatterns = router.urls