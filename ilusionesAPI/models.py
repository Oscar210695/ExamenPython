from django.db import models

# Create your models here.
class Almacen(models.Model):
    subInventario = models.CharField(primary_key=True, unique=True, max_length=10)
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

class ordenCompra(models.Model):
    almacen = models.ForeignKey(Almacen, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    estatus = models.ForeignKey(Estatus, on_delete=models.CASCADE, default=1)