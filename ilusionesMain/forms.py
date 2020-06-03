from django import forms
from django.forms import ModelForm
from django.core import validators
from ilusionesAPI.models import Almacen

class FormAlmacen(ModelForm):
    subInventario = forms.CharField(
        max_length=10,
        validators=[validators.MinLengthValidator(10,'El campo Almacen debe tener exactamente 10 caracteres'),
                    validators.RegexValidator('^[a-zA-Z]{5}[0-9]{5}$', 'La clave esta mal formada')]
    )

    class Meta:
        model = Almacen
        fields = ['subInventario', 'pdv', 'nombre']
        labels = {
            "subInventario": "Almacen",
            "pdv": "PDV",
            "nombre": "Nombre",
        }
        error_messages = {
            'subInventario': {
                'required': "El campo Almacen es obligatorio",
            },
            'pdv': {
                'required': "El campo PDV es obligatorio",
            },
            'nombre': {
                'required': "El campo Nombre es obligatorio",
            },
        }

class EditFormAlmacen(ModelForm):

    class Meta:
        model = Almacen
        fields = ['pdv', 'nombre']
        labels = {
            "subInventario": "Almacen",
            "pdv": "PDV",
            "nombre": "Nombre",
        }
        error_messages = {
            'pdv': {
                'required': "El campo PDV es obligatorio",
            },
            'nombre': {
                'required': "El campo Nombre es obligatorio",
            },
        }

