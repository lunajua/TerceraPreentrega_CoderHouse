from django.db import models
# Create your models here.

opciones_consulta = [
    [0, "Consulta"],
    [1, "Reclamo"],
    [2, "Sugerencia"],
    [3, "Venta"],
    [4, "Felicitaciones"]
]
class Contacto(models.Model):
    nombre = models.CharField(max_length=50)    
    correo = models.EmailField()
    tipo_consulta = models.IntegerField(choices=opciones_consulta)
    mensaje = models.TextField() 
    
    def __str__(self):
        return self.nombre


opciones_venta = [
    [0, "Tablet"],
    [1, "Smartphone"],
    [2, "SmartTv"],
    [3, "SmartWatch"]    
]

minorista_mayorista = [
    [0, "Minorista"],
    [1, "Mayorista"]
]

marcas = [
    [0, "Samsung"],
    [1, "Apple"],
    [2, "Huawei"],
    [3, "Xiaomi"]   
]

class Producto(models.Model):    
    marca = models.IntegerField(choices=marcas)
    op_venta = models.IntegerField(choices=opciones_venta)
    op_minorista_mayorista = models.IntegerField(choices=minorista_mayorista)
    descripcion = models.TextField()
        
    def __str__(self):
        return self.descripcion

class Reparacion(models.Model):
    fecha = models.DateField()
    producto = models.CharField(max_length=20)
    contacto = models.ForeignKey(Contacto, on_delete=models.CASCADE)
    problema = models.TextField()        
    estado = models.BooleanField(default=False)
     
    
    def __str__(self):
        return self.problema