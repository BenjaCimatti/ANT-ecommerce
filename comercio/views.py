from rest_framework import viewsets
from .models import *
from .serializers import *
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.

# ViewSets define the view behavior.
class ProductoViewSet(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
    serializer_class = ProductoSerializer
    
    def get_queryset(self):
        return Producto.objects.all()

# ViewSets define the view behavior.
class MarcaViewSet(viewsets.ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer

# ViewSets define the view behavior.
class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

# ViewSets define the view behavior.
class ProveedorViewSet(viewsets.ModelViewSet):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer

# ViewSets define the view behavior.
class StockViewSet(viewsets.ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer

# ViewSets define the view behavior.
class CarritoViewSet(viewsets.ModelViewSet):
    queryset = Carrito.objects.all()
    serializer_class = CarritoSerializer

# ViewSets define the view behavior.
class ProductoAgregadoViewSet(viewsets.ModelViewSet):
    queryset = ProductoAgregado.objects.all()
    serializer_class = ProductoAgregadoSerializer
