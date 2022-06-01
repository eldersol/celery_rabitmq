from django import forms
from .models import Registro


class Formulario(forms.ModelForm):
    class Meta:
        model = Registro
        fields = '__all__'
