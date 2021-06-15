from django.db import models
from django.contrib.auth.models import User

class Marca(models.Model):
    models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Marca'
        verbose_name_plural = 'Marcas'

class Categoria(models.Model):
    models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'