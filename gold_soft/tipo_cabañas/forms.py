from django import forms
from . models import Tipo_cabaña

class Tipo_cabañaForm(forms.ModelForm):
    class Meta:
        model = Tipo_cabaña
        fields = "__all__"
        exclude = ['status']
        labels = {
            'id': 'ID',
            'name': 'Nombre',
        }
        widgets = {
            'id': forms.NumberInput(attrs={'placeholder': 'Ingresa el ID'}),
            'name': forms.TextInput(attrs={'placeholder': 'Ingresa el nombre'}),
        }