from django import forms
from . models import Servicio

class ServicioForm(forms.ModelForm):
    class Meta:
        model = Servicio
        fields = "__all__"
        exclude = ['status']
        labels = {
            'id': 'ID',
            'name': 'Nombre',
            'price': 'Precio',                      
        }
        widgets = {
            'id': forms.NumberInput(attrs={'placeholder': 'Ingresa el ID'}),
            'name': forms.TextInput(attrs={'placeholder': 'Ingresa el Nombre'}),
            'price': forms.NumberInput(attrs={'placeholder': 'Ingresa la Precio'}),            
        }