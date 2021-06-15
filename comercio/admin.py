from django.contrib import admin
from .models import *


class ListaProductoInline(admin.TabularInline):

    model = ListaProducto
    extra = 1

@admin.register(Carrito)
class CarritoAdmin(admin.ModelAdmin):

    list_display = ('user',)
    inlines = [ListaProductoInline,]

# Register your models here.
admin.site.register(Categoria)
admin.site.register(Proveedor)
admin.site.register(Marca)
admin.site.register(Producto)
admin.site.register(ListaProducto)
admin.site.register(Venta)