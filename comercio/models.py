from django.db import models
from django.contrib.auth.models import User

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

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

class Stock(models.Model):
    proveedor = models.OneToOneField(Proveedor, on_delete=models.CASCADE)
    producto = models.OneToOneField(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()

    def __str__(self):
        return f'Stock de {self.producto.nombre}: {self.cantidad}'

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Stock'
        verbose_name_plural = 'Stocks'

class Carrito(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    vendido = models.BooleanField()
    precioFinal = models.FloatField()
    precioVendido = models.FloatField()

    def __str__(self):
        return f'Carrito {self.id} de {self.usuario.nombre}: vendido {self.vendido}'

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Carrito'
        verbose_name_plural = 'Carritos'


class ProductoAgregado(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    unidades = models.IntegerField()
    precioUnidad = models.FloatField()
    precioVendido = models.FloatField()
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.unidades} de {self.producto.nombre}'

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'ProductoAgregado'
        verbose_name_plural = 'ProductosAgregados'