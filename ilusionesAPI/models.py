from django.db import models
from django.core.validators import FileExtensionValidator

# Create your models here.
class Almacen(models.Model):
    default_error_messages = {
        'unique': 'Ya existe actualmente esta clave',
    }

    subInventario = models.CharField(primary_key=True, unique=True, max_length=10, error_messages=default_error_messages)
    pdv = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    sku = models.CharField(primary_key=True, unique=True, max_length=50)

    def __str__(self):
        return self.sku

class Estatus(models.Model):
    descripción = models.CharField(max_length=50)

    def __str__(self):
        return self.descripción

class Orden(models.Model):
    default_error_messages = {
        'unique': 'Ya existe actualmente esta clave',
    }

    clave = models.CharField(primary_key=True, unique=True, max_length=20, error_messages=default_error_messages)
    total = models.IntegerField(default=0)

    def __str__(self):
        return self.clave

class ordenCompra(models.Model):
    almacen = models.ForeignKey(Almacen, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    estatus = models.ForeignKey(Estatus, on_delete=models.CASCADE, default=1)
    orden = models.ForeignKey(Orden, on_delete=models.CASCADE, default="null")