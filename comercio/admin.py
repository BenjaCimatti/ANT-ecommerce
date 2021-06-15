from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Categoria)
admin.site.register(Proveedor)
admin.site.register(Marca)
admin.site.register(Producto)
admin.site.register(Stock)
admin.site.register(Carrito)
admin.site.register(ProductoAgregado)