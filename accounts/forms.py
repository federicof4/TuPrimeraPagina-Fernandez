from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = (
            "username",
            "email",
        )
        whidgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),            
        }
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "fecha_nacimiento",
            "direccion",
            "telefono",
            "compania",
            "user_image",
            "nro_documento",
        )
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'fecha_nacimiento': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Fecha de Nacimiento', 'type': 'date'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Dirección'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Teléfono'}),
            'compania': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Compañía'}),
            'user_image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'nro_documento': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Número de Documento'}),
        }   