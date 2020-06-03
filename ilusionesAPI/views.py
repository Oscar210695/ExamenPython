from django.shortcuts import render
from rest_framework import viewsets          
from .serializers import serializerClass      
from .models import Almacen   

# Create your views here.
class getAlmacenes(viewsets.ModelViewSet):       
  serializer_class = serializerClass          
  queryset = Almacen.objects.all()              
