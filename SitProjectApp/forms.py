from django import forms
from .models import Servicio, Cliente, Vehiculo

class ServicioForm(forms.ModelForm):
    class Meta:
        model = Servicio
        fields = ['tipo_servicio', 'descripcion' ,'precio']
        widgets = {
            'tipo_servicio': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tipo de Servicio'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descripción', 'rows': 3}),
            'precio': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '    Precio'}),
        }

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'apellido', 'email', 'telefono']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apellido'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Teléfono'}),
        }

class VehiculoForm(forms.ModelForm):
    class Meta:
        model = Vehiculo
        fields = ['marca', 'modelo', 'anio', 'chasis_nro']
        widgets = {
            'marca': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Marca'}),
            'modelo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Modelo'}),
            'anio': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Año'}),
            'chasis_nro': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Número de Chasis'}),
        }
