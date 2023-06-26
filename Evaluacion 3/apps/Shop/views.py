from django.shortcuts import render, redirect
from .models import *
import os
from django.conf import settings
from django.http import HttpResponse
import json

# Create your views here.

from django.shortcuts import render

def Index(request):
    return render(request, 'index.html')

def cargarInicio(request):
    productos = Producto.objects.all()
    producto_plantas = Producto.objects.filter(categoria_id=1)
    producto_semillas = Producto.objects.filter(categoria_id=2)
    producto_tierra = Producto.objects.filter(categoria_id=3)
    producto_fertilizantes = Producto.objects.filter(categoria_id=4)
    producto_herramientas = Producto.objects.filter(categoria_id=5)
    producto_macetas = Producto.objects.filter(categoria_id=6)
    producto_riego = Producto.objects.filter(categoria_id=7)
    producto_decoraciones = Producto.objects.filter(categoria_id=8)
    return render(request, "Productos.html", {"prod": productos, "prod_plants": producto_plantas, "prod_seeds": producto_semillas, "prod_land": producto_tierra, "prod_fertilizer": producto_fertilizantes, "prod_tools": producto_herramientas, "prod_pots": producto_macetas, "prod_irrigation": producto_riego, "prod_decorations": producto_decoraciones})

def cargarAgregarProducto(request):
    categorias = Categoria.objects.all()
    productos = Producto.objects.all()

    return render(request, "Admin.html",{"cate":categorias,"prod":productos})

def agregarProducto(request):
    #print("AGREGANDO PRODUCTOS A LA BBDD",request.POST)
    v_sku = request.POST['txtSku']
    v_precio = request.POST['txtPrecio']
    v_nombre = request.POST['txtNombre']
    v_imagen = request.FILES['txtImagen']
    v_descripcion = request.POST['txtDescripcion']
    v_stock = request.POST['txtStock']

    v_categoria = Categoria.objects.get(id_categoria=request.POST['cmbCategoria'])

    Producto.objects.create(sku = v_sku, precio = v_precio, nombre = v_nombre,imagen = v_imagen,descripcion = v_descripcion,stock = v_stock, categoria_id = v_categoria)


    return redirect('/agregarProducto')


def cargarEditarProducto(request,sku):
    producto = Producto.objects.get(sku = sku)
    categorias = Categoria.objects.all()
    return render(request,"editarProducto.html",{"prod":producto,"cate":categorias})
def editarProducto(request):
    v_sku = request.POST['txtSku']
    productoBD = Producto.objects.get(sku = v_sku)
    v_precio = request.POST['txtPrecio']
    v_nombre = request.POST['txtNombre']
    v_descripcion = request.POST['txtDescripcion']
    v_stock = request.POST['txtStock']
    v_categoria = Categoria.objects.get(id_categoria = request.POST['cmbCategoria'])

    try:
        v_imagen = request.FILES['txtImagen']   
        ruta_img = os.path.join(settings.MEDIA_ROOT,str(productoBD.imagen))
        os.remove(ruta_img)

    except:
        v_imagen = productoBD.imagen

    productoBD.nombre = v_nombre
    productoBD.precio = v_precio
    productoBD.imagen = v_imagen
    productoBD.descripcion = v_descripcion
    productoBD.stock = v_stock
    productoBD.categoria_id = v_categoria
    

    productoBD.save()

    return redirect('/agregarProducto')


def eliminarProducto(request,sku):
    producto = Producto.objects.get(sku = sku)
    ruta_img = os.path.join(settings.MEDIA_ROOT,str(producto.imagen))
    os.remove(ruta_img)
    producto.delete()

    return redirect('/agregarProducto')

def carrito(request):
    productos = json.loads(request.body)
    for p in productos:
        sku = p.get('sku')
        cantidad = p.get('cantidad')
        if sku is not None and cantidad is not None:
            print("SKU:", sku)
            print("CANTIDAD:", cantidad)
        else:
            print("No se encontró SKU o CANTIDAD en el elemento del producto")
    return HttpResponse("OK!")


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

def Admin(request):
    return render(request, 'Admin.html')