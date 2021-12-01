from django.contrib.auth.backends import BaseBackend
from django.conf import settings
from .models import Usuario

class MyBackend(BaseBackend):
    def authenticate(self, request, username = None , password = None):
        try:
            usuario = Usuario.objects.filter(username = username, password = password).get()
            return usuario
        except:
            return None

    def get_user(self, user_id):
        try:
            return Usuario.objects.get(pk=user_id)
        except Usuario.DoesNotExist:
            print("chao")
            return None