from django.urls import path 
from AppMantenimientoHogar import views


urlpatterns = [
    path('', views.index, name="Index"),
    path('about/', views.about, name="About"),
    path('contact/', views.contact, name="Contact"),
    path('service/', views.service, name="Service"),      
]
    