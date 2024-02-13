from django import forms
from .models import Contacto
from .models import Producto
from .models import Reparacion


class ContactoFormulario(forms.ModelForm):
    
    class Meta:
        model = Contacto
        fields = "__all__"

class Venta(forms.ModelForm):
    
    class Meta:
        model = Producto
        fields = "__all__"

class ReparaFormulario(forms.ModelForm):
    class Meta:
        model = Reparacion
        fields = "__all__"