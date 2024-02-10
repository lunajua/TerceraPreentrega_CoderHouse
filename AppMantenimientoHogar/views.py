from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'AppMantenimientoHogar/index.html') 

def about(request):
    return render(request, 'AppMantenimientoHogar/about.html')

def contact(request):
    return render(request, 'AppMantenimientoHogar/contact.html')

def service(request):
    return render(request, 'AppMantenimientoHogar/service.html')