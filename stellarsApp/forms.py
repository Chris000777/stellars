from django import forms
from django.forms import ValidationError
from .models import Post
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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


class PostForm(forms.ModelForm):

    # nombre = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese nombre'}),error_messages={'required':'Por favor no te olvide de mi!'})
    class Meta:
        model=Post
        fields= fields=['author', 'movie','title','content', 'rating', 'alta']
        # fields=['title','content']
        #exclude=('baja',)
        # widgets = {
        #     'nombre': forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese nombre'})
        # }
        # error_messages={
        #     'nombre': {
        #         'required':'No te olvides del nombre!'
        #     }
        # }

# class PostFormValidado(PostForm):
    
#     def clean_titulo(self):
#         for post in posts:
#             if (title.upper() != peliculas.upper()):
#                 titulo = self.cleaned_data['title']
#             if nombre.upper() == 'ORIGAMI':
#                 raise ValidationError('Codo a codo no dicta esta categoria de cursos')
#             return title

class RegistrarUsuarioForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email' , 'password1', 'password2']
