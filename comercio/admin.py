from django.contrib import admin
from .models import *


@admin.register(Carrito)
class CarritoAdmin(admin.ModelAdmin):

    list_display = ('id','usuario','vendido')
    list_display_links = ('id','usuario','vendido')

    readonly_fields = ('precioFinal','precioVendido')

@admin.register(ProductoAgregado)
class ProductoAgregadoAdmin(admin.ModelAdmin):

    readonly_fields = ('precioVendido',)


# Register your models here.
admin.site.register(Categoria)
admin.site.register(Proveedor)
admin.site.register(Marca)
admin.site.register(Producto)
admin.site.register(Stock)