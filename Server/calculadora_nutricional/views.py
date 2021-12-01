from django.shortcuts import redirect, render
from .forms import LoginForm, ContactoForm, UsuariosForm
from .backend import MyBackend
from django.contrib.auth import login as auth_login, logout
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group


# Create your views here.

myBackend = MyBackend()

def index(request):
    return render(request,'calculadora_nutricional/index.html')

def recursos_externos(request):
    return render(request,'calculadora_nutricional/recursos_externos.html')

def contacto(request):
    return render(request,'calculadora_nutricional/contacto.html')

def preguntas_frecuentes(request):
    return render(request,'calculadora_nutricional/preguntas_frecuentes.html')

def sobre_mi(request):
    return render(request,'calculadora_nutricional/sobre_mi.html')

def calculadora(request):
    return render(request,'calculadora_nutricional/calculadora.html')

def guia_usuario(request):
    return render(request,'calculadora_nutricional/guia_usuario.html')

def registro(request):
    if request.method == "POST":
        form=UsuariosForm(data=request.POST)
        if form.is_valid():
            user_name = form.cleaned_data["user_name"]
            email_address = form.cleaned_data["email_address"]
            password=form.cleaned_data["password"]
            user_group = User.objects.create_user(user_name, email_address,password)
            user_group.save()
            grupo = Group.objects.get(name=request.POST.get("nombre_grupo_usuario"))
            user_group.groups.add(grupo)
            return render(request,'calculadora_nutricional/usuario_creado.html')
    else:
        form = UsuariosForm()
        return render(request,'calculadora_nutricional/crear_usuario.html',{'form': form})


def login(request, backend ='calculadora_nutricional.backend.MyBackend'):
    if request.method == "POST":
        form = LoginForm(data = request.POST)
        if form.is_valid():
            usuario = form.cleaned_data['nombre_login']
            clave = form.cleaned_data['password_login']
            print(type(usuario))
            print(type(clave))
            user1 = myBackend.authenticate(request, username = usuario, password = clave)
            if user1 is not None:
                auth_login(request, user1, backend)
                return render(request,'calculadora_nutricional/principal.html', {"user":user1})
            else:
                print('sigue aca')
                return render(request,'calculadora_nutricional/sobre_mi.html', {"form":form})
    else:
        form = LoginForm()
        return render(request,'calculadora_nutricional/ingreso.html', {"form":form})

def cerrar_sesion(request):
    logout(request)
    return redirect("/login")

@login_required(login_url="/login")
def principal(request):
    return render(request,'calculadora_nutricional/principal.html')

def envio_mensaje(request):
    if request.method == "POST":
        form = ContactoForm(data = request.POST)
        if form.is_valid():
            contacto = form.save(commit = False)
            contacto.save()
        return redirect('/contacto')
    else:
        form = ContactoForm()
        return render(request,'calculadora_nutricional/contacto.html', {"form": form})



