from django import forms
from .models import Cuenta, Info

class CuentaForm(forms.ModelForm):
    class Meta:
        model = Cuenta
        fields = ['alias', 'edad', 'descripcion']

        labels = {
            'alias': 'alias',
            'edad': 'edad',
            'descripcion': 'descripcion',

        }
        widgets = {
            'alias': forms.TextInput(attrs={'class': 'form-control'}),
            'edad': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
        }

