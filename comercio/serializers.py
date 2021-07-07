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

class CarritoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Carrito
        fields = '__all__'
        
class ProductoAgregadoSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductoAgregado
        fields = '__all__'