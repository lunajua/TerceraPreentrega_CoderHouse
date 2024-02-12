from django.urls import path 
from AppMantenimientoHogar import views
from django.contrib import admin


urlpatterns = [
    
    path('', views.index, name="Index"),        
    path('contacto/', views.contacto, name="Contacto"),
    path('venta/', views.venta, name="Venta"),
    path('busqueda/', views.busqueda, name="Busqueda")      
]
    