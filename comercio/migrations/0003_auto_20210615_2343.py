# Generated by Django 3.1.7 on 2021-06-15 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comercio', '0002_carrito_comprar'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carrito',
            name='comprar',
        ),
        migrations.AlterField(
            model_name='carrito',
            name='vendido',
            field=models.BooleanField(default=False),
        ),
    ]