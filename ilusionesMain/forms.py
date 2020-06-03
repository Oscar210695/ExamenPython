from django import forms
from django.core import validators
from ilusionesAPI.models import Almacen

class FormAlmacen(forms.ModelForm):

    class Meta:
        model = Almacen
        fields = ('subInventario', 'pdv', 'nombre',)

