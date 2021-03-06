"""ilusionesProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from ilusionesAPI import views

router = routers.DefaultRouter() 
router.register(r'almacen', views.getAlmacenes, 'ilusionesAPIAlmacen')  
router.register(r'prod', views.getProductos, 'ilusionesAPIProd')  
router.register(r'orden', views.getOrden, 'ilusionesAPIOrden')  
router.register(r'ordenIn', views.getOrdenInd, 'ilusionesAPIOrdenInd')  
router.register(r'recep', views.getRecep, 'ilusionesAPIRecep')  
router.register(r'inven', views.getInven, 'ilusionesAPIInven')  
router.register(r'invAlm', views.getInvAlm, 'ilusionesAPIInvenAlm')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('', include('ilusionesMain.urls')),
]
