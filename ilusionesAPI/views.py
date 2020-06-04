from django.shortcuts import render
from rest_framework import viewsets          
from .serializers import serializerClass, serializerClassProd, serializerClassOrden , serializerClassOrdenIn    
from .models import Almacen, Producto, ordenCompra, Orden

# Create your views here.
class getAlmacenes(viewsets.ModelViewSet):       
  serializer_class = serializerClass          
  queryset = Almacen.objects.all()   

class getProductos(viewsets.ModelViewSet):       
  serializer_class = serializerClassProd          
  queryset = Producto.objects.all()  

class getOrden(viewsets.ModelViewSet):       
  serializer_class = serializerClassOrden          
  queryset = ordenCompra.objects.all()      

class getOrdenInd(viewsets.ModelViewSet):       
  serializer_class = serializerClassOrdenIn          
  queryset = Orden.objects.all()        
