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
    entregada = models.BooleanField(default=False)

    def __str__(self):
        return self.clave

class ordenCompra(models.Model):
    almacen = models.ForeignKey(Almacen, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    estatus = models.ForeignKey(Estatus, on_delete=models.CASCADE, default=1)
    orden = models.ForeignKey(Orden, on_delete=models.CASCADE, default='null')

class Recepcion(models.Model):
    folio = models.CharField(primary_key=True, unique=True, max_length=100)
    almacen = models.ForeignKey(Almacen, on_delete=models.CASCADE, related_name='almacenes')
    nombre = models.CharField(max_length=100)
    orden = models.ForeignKey(Orden, on_delete=models.CASCADE, default='null')

    def __str__(self):
        return self.folio

class Inventario(models.Model):
    imei = models.CharField(primary_key=True, unique=True, max_length=50)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    folio = models.ForeignKey(Recepcion, on_delete=models.CASCADE, related_name='productos')

    def __str__(self):
        return self.imei