from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('inicio/', views.index, name='inicio'),
    path('almacenes/', views.getAlmacenes, name='almacenes'),
    path('borrarAlmacen/<str:subInventario>', views.deleteAlmacen, name='borrarAlmacen'),
    path('actualizarAlmacen/<str:subInventario>', views.getAlmacen, name='actualizarAlmacen'),
    path('crearAlmacen/', views.saveAlmacen, name='crearAlmacen'),
    path('subirOrden/', views.loadCompras, name='subirOrden'),
    path('ordenes/', views.getOrdenes, name='ordenes'),
    path('subirRec/<str:orden>', views.loadRec, name='subirRec'),
    path('inventario/', views.getInventario, name='inventario'),
]