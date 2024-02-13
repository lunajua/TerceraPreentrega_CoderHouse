from django.contrib import admin
from .models import Contacto
from .models import Producto
from .models import Reparacion


# Register your models here.
admin.site.register(Contacto)
admin.site.register(Producto)
admin.site.register(Reparacion)