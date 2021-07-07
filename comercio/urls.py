from django.urls import path, include
from .views import *

urlpatterns = [
    path('producto/', ProductoViewSet.as_view({'get': 'list'})),
    path('marca/', MarcaViewSet.as_view({'get': 'list'})),
    path('categoria/', CategoriaViewSet.as_view({'get': 'list'})),
    path('proveedor/', ProveedorViewSet.as_view({'get': 'list'})),
    path('stock/', StockViewSet.as_view({'get': 'list'})),
    path('carrito/', CarritoViewSet.as_view({'get': 'list'})),
    path('productoagregado/', ProductoAgregadoViewSet.as_view({'get': 'list'}))
]
