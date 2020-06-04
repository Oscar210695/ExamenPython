from django import forms
from django.forms import ModelForm
from django.core import validators
from django.core.validators import FileExtensionValidator
from ilusionesAPI.models import Almacen, Orden

class FormAlmacen(ModelForm):
    subInventario = forms.CharField(
        max_length=10,
        validators=[validators.MinLengthValidator(10,'El campo Almacen debe tener exactamente 10 caracteres'),
                    validators.RegexValidator('^[a-zA-Z]{5}[0-9]{5}$', 'La clave esta mal formada debe tener la estructura de 5 letras seguida de 5 números')]
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

class FormOrden(ModelForm):
    clave = forms.CharField(
        max_length=20,
        validators=[validators.RegexValidator('^[a-zA-Z0-9]*$', 'La clave solo debe tener número y/o letras')]
    )
    Archivo = forms.FileField(validators=[FileExtensionValidator(allowed_extensions=['xls', 'xlsx'], message='Deben ser archivos de tipo excel')])

    class Meta:
        model = Orden
        fields = ['clave']
        labels = {
            "clave": "Clave"
        }

