from django import forms
from django.forms import ValidationError

def solo_caracteres(valor):
    if any(char.isdigit() for char in valor):
        raise ValidationError('El campo no puede contener números.')

class ContactoForm(forms.Form):
    nombre = forms.CharField(
        label='Nombre',
        max_length=50,
        validators=(solo_caracteres,),
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':''}))

    apellido = forms.CharField(
        label='Apellido',
        max_length=50,
        validators=(solo_caracteres,),
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':''}))

    direccion= forms.CharField(
        label='Dirección',
        max_length=50,
        error_messages={
            'required':'Por favor ingrese una dirección válida'
        },
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':''}))

    email = forms.EmailField(
        label='Email',
        max_length=50,
        error_messages={
            'required':'Por favor ingrese una dirección válida'
        },
        widget=forms.TextInput(attrs={'class':'form-control','type':'email'}))

    telefono= forms.CharField(
        label='Teléfono',
        max_length=20,
        widget=forms.TextInput(attrs={'class':'form-control','type':'number'}))

    