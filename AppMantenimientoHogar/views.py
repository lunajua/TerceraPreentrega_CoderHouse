from django.shortcuts import render
from .forms import ContactoFormulario
from .forms import Venta
from .forms import ReparaFormulario

# Create your views here.
def index(request):
    return render(request, 'AppMantenimientoHogar/index.html') 

def contacto(request):
    data = { #form es la variable que viaje y se crea una instancia y debo pasarlo en el retorno y renderizar por eso va como un tercer parámetro.
        'form': ContactoFormulario()
    }
    
    if request.method == 'POST':
        formulario = ContactoFormulario(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Mensaje Enviado"
        else:
            data["form"] = formulario
    
    return render(request, 'AppMantenimientoHogar/contacto.html', data)

def venta(request):
    
    data = { 
        
        'form': Venta()
    }
    
    if request.method == 'POST':
        formulario = Venta(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Pedido Registrado"
        else:
            data["form"] = formulario
            
    return render(request, 'AppMantenimientoHogar/venta.html', data)

def busqueda(request):
    return render(request, 'AppMantenimientoHogar/busqueda.html')

def reparacion(request):
    
    data = { 
        
        'form': ReparaFormulario()
    }
    
    if request.method == 'POST':
        repaform = ReparaFormulario(data=request.POST)
        if repaform.is_valid():
            repaform.save()
            data["mensaje"] = " Registrado"
        else:
            data["form"] = repaform
            
    return render(request, 'AppMantenimientoHogar/reparacion.html', data)
      
    
    