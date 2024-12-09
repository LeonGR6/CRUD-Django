from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Producto
from .forms import ProductoForm
# Create your views here.

def inicio(request):
    return render(request,'paginas/inicio.html')

def nosotros(request):
    return render(request, 'paginas/nosotros.html')


def productos(request):
    Productos_l = Producto.objects.all()
    return render(request, 'productos/index.html', {'productos': Productos_l})

def crear(request):
    formmulario = ProductoForm(request.POST or None, request.FILES or None)
    if formmulario.is_valid():
        formmulario.save()
        return redirect('productos')
    return render(request,'productos/crear.html', {'formulario': formmulario})

def editar(request, id):
    producto = Producto.objects.get(id=id)
    formmulario = ProductoForm(request.POST or None, request.FILES or None, instance=producto)
    if formmulario.is_valid() and request.POST:
        formmulario.save()
        return redirect('productos')
    return render(request,'productos/editar.html', {'formulario': formmulario})

def eliminar(request, id):
    producto = Producto.objects.get(id=id)  
    producto.delete()  
    return redirect('productos')