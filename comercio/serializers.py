from rest_framework import serializers
from .models import *

class ProductoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Producto
        fields = '__all__'

class MarcaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Marca
        fields = '__all__'

class CategoriaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Categoria
        fields = '__all__'

class ProveedorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Proveedor
        fields = '__all__'

class StockSerializer(serializers.ModelSerializer):

    class Meta:
        model = Stock
        fields = '__all__'

class DeleteProductoAgregadoSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductoAgregado
        fields = ['id']

class AddProductoAgregadoSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductoAgregado
        fields = ['producto','unidades']

class ProductoAgregadoSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductoAgregado
        exclude = ['carrito']
        depth = 1

class CarritoSerializer(serializers.ModelSerializer):

    productos = ProductoAgregadoSerializer(many=True)

    class Meta:
        model = Carrito
        fields = ['usuario','vendido','precioFinal','precioVendido','productos']

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'password',)