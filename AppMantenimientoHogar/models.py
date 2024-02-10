from django.db import models

# Create your models here.
class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    celular = models.IntegerField(max_length=50)
    email = models.EmailField(null=True, blank=True)
    mensaje = models.TextField() 
    
class Persona(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.IntegerField()
    fecha_nacimiento = models.DateField()  
    
