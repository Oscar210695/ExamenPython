from rest_framework import serializers
from .models import Almacen, Producto, ordenCompra, Orden, Inventario, Recepcion
      
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
    fields = ('almacen', 'producto', 'cantidad', 'estatus', 'orden')

class serializerClassOrdenIn(serializers.ModelSerializer):
  class Meta:
    model = Orden
    fields = ('clave', 'total', 'entregada')

class serializerClassInventario(serializers.ModelSerializer):
  class Meta:
    model = Inventario
    fields = ('imei', 'producto', 'folio')

class serializerClassInven(serializers.ModelSerializer):
  class Meta:
    model = Inventario
    fields = ('imei', 'producto','folio')

class serializerClassRecep(serializers.ModelSerializer):
  class Meta:
    model = Recepcion
    fields = ('almacen', 'nombre', 'folio', 'orden')

class serializerClassRecepAlm(serializers.ModelSerializer):
  productos = serializerClassInven(many=True)

  class Meta:
    model = Recepcion
    fields = ('almacen','productos')
