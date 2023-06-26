from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [ 
    path('',views.Index, name = 'Index'),
    path('Productos/',views.cargarInicio, name = 'Productos'),
    path('Registrate/',views.Registrate, name = 'Registrate'),
    path('InicioDeSesion/',views.InicioDeSesion, name = 'InicioDeSesion'),
    path('Carrito/',views.Carrito, name = 'Carrito'),
    path('Api/',views.Api, name = 'Api'),
    path('Ayuda/',views.Ayuda, name='Ayuda'),
    path('Admin/',views.cargarAgregarProducto, name = 'Admin'),
    path('agregarProductoForm',views.agregarProducto),
    path('agregarProducto',views.cargarAgregarProducto),
    path('editarProducto/<sku>',views.cargarEditarProducto),
    path('editarProductoForm',views.editarProducto),
    path('eliminarProducto/<sku>',views.eliminarProducto),

]