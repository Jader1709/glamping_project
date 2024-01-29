from django import forms
from . models import Cabaña

class CabañaForm(forms.ModelForm):
    class Meta:
        model = Cabaña
        fields = "__all__"
        exclude = ['status']
        labels = {
            'name': 'Nombre',
            'image': 'Imagen',
            'capacity': 'Capacidad',
            'price': 'Precio',
            'description': 'Descripcion',
            'type_cabin': 'tipo cabaña',
        }
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Ingresa el nombre'}),
            'image': forms.FileInput(attrs={'placeholder': 'Ingresa el documento'}),
            'capacity': forms.NumberInput(attrs={'placeholder': 'Ingresa la capacidad'}),
            'price': forms.TextInput(attrs={'placeholder': 'Ingresa el precio'}),
            'description': forms.TextInput(attrs={'placeholder': 'Ingresa la descripcion'}),
            'type_cabin': forms.TextInput(attrs={'placeholder': 'Ingresa el tipo de cabaña'}),
        }