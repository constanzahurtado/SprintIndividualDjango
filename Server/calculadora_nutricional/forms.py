from django import forms
from django.db.models import fields
from django.db.models.enums import Choices
from django.forms.widgets import PasswordInput
from .models import Contacto, Usuario


class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = ('nombre','apellido','email', 'mensaje')

class UsuariosForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ('username','email_address', 'password', 'nombre_grupo_usuario')

class LoginForm(forms.Form):
    nombre_login = forms.CharField(widget=forms.TextInput)
    password_login = forms.CharField(widget=forms.PasswordInput)



