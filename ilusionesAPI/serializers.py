from rest_framework import serializers
from .models import Almacen, Producto, ordenCompra
      
class serializerClass(serializers.ModelSerializer):
  class Meta:
    model = Almacen
    fields = ('subInventario', 'pdv', 'nombre')

class serializerClassProd(serializers.ModelSerializer):
  class Meta:
    model = Producto
    fields = ('sku',)

class serializerClassOrden(serializers.ModelSerializer):
  class Meta:
    model = ordenCompra
    fields = ('almacen', 'producto', 'cantidad', 'estatus')