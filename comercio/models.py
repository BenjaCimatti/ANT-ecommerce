from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

class Marca(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Marca'
        verbose_name_plural = 'Marcas'

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

class Proveedor(models.Model):
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    telefono = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    precio = models.FloatField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    proveedor = models.OneToOneField(Proveedor, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

class Stock(models.Model):
    producto = models.OneToOneField(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()

    def __str__(self):
        return f'Stock de {self.producto.nombre} {self.producto.marca.nombre}: {self.cantidad}'

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Stock'
        verbose_name_plural = 'Stocks'

class Carrito(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    vendido = models.BooleanField(default = False)
    precioFinal = models.FloatField(null = True, blank = True)
    precioVendido = models.FloatField(null = True, blank = True)

    def __str__(self):
        if self.vendido:
            return f'Carrito {self.id} de {self.usuario.username} esta vendido'
        else:
            return f'Carrito {self.id} de {self.usuario.username} no esta vendido'
        

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Carrito'
        verbose_name_plural = 'Carritos'


class ProductoAgregado(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    unidades = models.IntegerField()
    precioVendido = models.FloatField(null = True, blank = True)
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.unidades} de {self.producto.nombre}'

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'ProductoAgregado'
        verbose_name_plural = 'ProductosAgregados'

        
@receiver(post_save, sender=Carrito)
def finish_purchase(sender, instance, created, **kwargs):
    if not getattr(instance, 'processed', False):
        if not created:
            if instance.vendido:
                productos_agredados = ProductoAgregado.objects.filter(carrito = instance) # traemos todos los productos del carrito
                if(productos_agredados.count() > 0):
                    for a in productos_agredados:
                        producto = Producto.objects.get(id = a.producto.id) # traemos el producto
                        if instance.precioFinal == None:
                            instance.precioFinal = 0
                        producto_precioFinal = a.unidades * producto.precio # producto de las unidades con el precio
                        a.precioVendido = producto_precioFinal
                        a.save() # guardamos el producto
                        instance.precioVendido = instance.precioFinal # nos aseguramos que el precio no cambie con respecto al precio del producto
                        productos_stock = Stock.objects.filter(producto = producto) # traemos los stock
                        for b in productos_stock:
                            b.cantidad -= a.unidades # reducir stock
                            b.save()
                    instance.processed = True
                    instance.save()
            else:
                productos_agredados = ProductoAgregado.objects.filter(carrito = instance) # traemos todos los productos del carrito
                if(productos_agredados.count() > 0):
                    for a in productos_agredados:
                        producto = Producto.objects.get(id = a.producto.id) # traemos el producto
                        if instance.precioFinal == None:
                            instance.precioFinal = 0
                        producto_precioFinal = a.unidades * producto.precio # producto de las unidades con el precio
                        instance.precioFinal += producto_precioFinal
                    instance.processed = True
                    instance.save()

@receiver(post_save, sender=Producto)
def create_stock(sender, instance, created, **kwargs):
    if created:
        Stock.objects.create(producto=instance, cantidad = 0) # creamos un stock del producto