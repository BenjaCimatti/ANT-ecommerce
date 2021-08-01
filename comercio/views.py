from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializers import *
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
# Create your views here.

# ViewSets define the view behavior.
class ProductoViewSet(viewsets.ModelViewSet):    
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

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

    permission_classes = (IsAuthenticated,) 

    serializer_class = CarritoSerializer

    def get_queryset(self):
        return Carrito.objects.filter(usuario=self.request.user, vendido=False)

# ViewSets define the view behavior.
class ProductoAgregadoViewSet(viewsets.ModelViewSet):
    queryset = ProductoAgregado.objects.all()
    serializer_class = ProductoAgregadoSerializer

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user(request):

    content = {
        'user':str(request.user),
    }

    return Response(content)