from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('inicio/', views.index, name='inicio'),
    path('almacenes/', views.getAlmacenes, name='almacenes'),
    path('borrarAlmacen/<str:subInventario>', views.deleteAlmacen, name='borrarAlmacen'),
    path('actualizarAlmacen/<str:subInventario>', views.getAlmacen, name='actualizarAlmacen'),
]