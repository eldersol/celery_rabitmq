from django import forms
from .models import Registro


class Formulario(forms.ModelForm):
    contrasena = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Registro
        fields = '__all__'
