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
