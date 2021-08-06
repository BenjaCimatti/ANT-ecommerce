from rest_framework import status, viewsets
from rest_framework.exceptions import bad_request
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
# Create your views here.

def bad_request(msg):
    content = {'bad request': msg}
    return Response(content, status=status.HTTP_400_BAD_REQUEST)

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

@api_view(['POST'])
def register_user(request):
    body = request.data
    username = body["username"]
    password = body["password"]
    print(body)
    print(username)
    print(password)
    serializer = UserSerializer(data=body)
    
    if serializer.is_valid():
        User.objects.create_user(username=username,password=password)
        return Response(serializer.data)
    else:
        return bad_request('Registro Fallido')


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_product(request):

    body = request.data

    producto_id = body["producto"]
    producto = Producto.objects.get(id=producto_id)
    unidades = body["unidades"]
    carrito = Carrito.objects.get(usuario=request.user, vendido=False)

    serializer = AddProductoAgregadoSerializer(data=body)
    
    if serializer.is_valid():

        ProductoAgregado.objects.create(
            producto = producto,
            unidades = unidades,
            carrito = carrito,
        )
        return Response(serializer.data)

    else:
        return bad_request('Body Fallido')