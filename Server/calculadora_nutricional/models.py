from django.db import models
from django.forms.widgets import RadioSelect

# Create your models here.

CHOICES=[('Usuario','Usuario'),
         ('Administrador','Administrador')]

class Usuario(models.Model):
    username = models.CharField(max_length= 50)
    email_address = models.CharField(max_length= 30)
    password = models.CharField(max_length= 12)
    nombre_grupo_usuario = models.CharField(max_length=20, choices=CHOICES)
    last_login = models.CharField(max_length= 30)

class Contacto(models.Model):
    nombre = models.CharField(max_length= 50)
    apellido = models.CharField(max_length= 50)
    email = models.CharField(max_length= 30)
    mensaje = models.TextField(max_length= 600)
