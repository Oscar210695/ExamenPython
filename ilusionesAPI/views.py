from django.shortcuts import render
from rest_framework import viewsets          
from .serializers import serializerClass, serializerClassProd, serializerClassOrden, serializerClassOrdenIn, serializerClassInventario, serializerClassRecep, serializerClassRecepAlm
from .models import Almacen, Producto, ordenCompra, Orden, Inventario, Recepcion

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

class getInven(viewsets.ModelViewSet):       
  serializer_class = serializerClassInventario          
  queryset = Inventario.objects.all()  

class getRecep(viewsets.ModelViewSet):       
  serializer_class = serializerClassRecep      
  queryset = Recepcion.objects.all() 

class getInvAlm(viewsets.ModelViewSet): 
  queryset = Recepcion.objects.all()      
  serializer_class = serializerClassRecepAlm 
  model = Recepcion
  filter_fields = ('almacen', ) 