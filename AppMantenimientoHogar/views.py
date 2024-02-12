from django.shortcuts import render
from .forms import Contacto

# Create your views here.
def index(request):
    return render(request, 'AppMantenimientoHogar/index.html') 

def contacto(request):
    data = { #form es la variable que viaje y se crea una instancia y debo pasarlo en el retorno y renderizar por eso va como un tercer parámetro.
        'form': Contacto()
    }
    return render(request, 'AppMantenimientoHogar/contacto.html', data)

def venta(request):
    return render(request, 'AppMantenimientoHogar/venta.html')

def busqueda(request):
    return render(request, 'AppMantenimientoHogar/busqueda.html')

