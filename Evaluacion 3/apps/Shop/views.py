from django.shortcuts import render
from .models import *
import os
from django.conf import settings

# Create your views here.

from django.shortcuts import render

def Index(request):
    return render(request, 'index.html')

def Productos(request):
    productos = Producto.objects.all()
    producto_plantas = Producto.objects.filter(categoria_id=1)
    producto_semillas = Producto.objects.filter(categoria_id=2)
    producto_tierra = Producto.objects.filter(categoria_id=3)
    producto_fertilizantes = Producto.objects.filter(categoria_id=4)
    producto_herramientas= Producto.objects.filter(categoria_id=5)
    producto_macetas = Producto.objects.filter(categoria_id=6)
    producto_riego = Producto.objects.filter(categoria_id=7)
    producto_decoraciones = Producto.objects.filter(categoria_id=8)
    return render(request,"productos.html",{"prod" : productos, "prod_plants":producto_plantas, "prod_seeds":producto_semillas, "prod_land":producto_tierra, "prod_fertilizer":producto_fertilizantes, "prod_tools":producto_herramientas, "prod_pots":producto_macetas, "prod_irrigation":producto_riego, "prod_decorations":producto_decoraciones})

def Registrate(request):
    return render(request, 'registrate.html')

def InicioDeSesion(request):
    return render(request, 'inicioDeSesion.html')

def Carrito(request):
    return render(request, 'carrito.html')

def Api(request):
    return render(request, 'api.html')

def Ayuda(request):
    return render(request, 'Ayuda.html')