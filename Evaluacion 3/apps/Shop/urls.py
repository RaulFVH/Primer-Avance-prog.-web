from django.urls import path
from . import views

urlpatterns = [ 
    path('',views.Index, name = 'Index'),
    path('Productos/',views.Productos, name = 'Productos'),
    path('Registrate/',views.Registrate, name = 'Registrate'),
    path('InicioDeSesion/',views.InicioDeSesion, name = 'InicioDeSesion'),
    path('Carrito/',views.Carrito, name = 'Carrito'),
    path('Api/',views.Api, name = 'Api'),
    path('Ayuda/',views.Ayuda, name='Ayuda'),
    path('Admin/',views.Admin, name = 'Admin'),
    path('agregarProducto',views.cargarAgregarProducto),
    path('agregarProductoForm',views.agregarProducto),
    path('editarProducto/<sku>',views.cargarEditarProducto),
    path('editarProductoForm',views.editarProducto),
    path('eliminarProducto/<sku>',views.eliminarProducto),

]

