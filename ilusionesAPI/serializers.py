from rest_framework import serializers
from .models import Almacen
      
class serializerClass(serializers.ModelSerializer):
  class Meta:
    model = Almacen
    fields = ('subInventario', 'pdv', 'nombre')