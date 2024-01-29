from django import forms
from . models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = "__all__"
        exclude = ['status']
        labels = {
            'id': 'ID',
            'name': 'Nombre',
            'document': 'Documento',
            'email': 'Correo',
            'phone': 'Telefono',                      
        }
        widgets = {
            'id': forms.NumberInput(attrs={'placeholder': 'Ingresa el ID'}),
            'name': forms.TextInput(attrs={'placeholder': 'Ingresa el nombre'}),
            'document': forms.TextInput(attrs={'placeholder': 'Ingresa el documento'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Ingresa el Email'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Ingresa la Telefono'}),            
        }