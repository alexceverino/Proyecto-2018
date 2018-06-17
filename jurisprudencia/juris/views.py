
from django.shortcuts import render
import datetime
from .forms import *
from .models import *
from django.shortcuts import render, redirect
from .validator import *


from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as logout_auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.
#este es el registro de sentencia

@login_required
def registro(request):
    form = AgregarSentencia(request.POST or None)

    if form.is_valid():
        form_data = form.cleaned_data
        juez = form_data.get("juez")
        norma = form_data.get("norma_aplicada")
        tribunal = form_data.get("tribunales")
        fecha_sent = form_data.get("fecha_sentencia")
        materia = form_data.get("materias_sentencia")
        fecha_agre =  datetime.date.today()
        obj = sentencia.objects.create(juez_sentencia=juez,nombre_tribunal=tribunal,norma_aplicada=norma,
                                        fecha_sentencia = fecha_sent,materias_sentencia = materia)

    context = {
        "e1_form":form,
    }
    return render(request,"registro.html",context)

@login_required
def index(request):
    """
    Pagina inicial.
    """
    return render(
        request,
        'index.html',
        {
        }
    )



def login(request):
    form = login_usuarios(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("usuario")
        password = form.cleaned_data.get("contrasena")
        user = authenticate(username=username,password=password)
        if user.is_active:
            auth_login(request,user)
            return redirect(index)
        else:
            raise forms.ValidationError("Usser no se encuentra activo")

    return render(request,"login.html",{"form_login":form})

@login_required
def logout( request ):
    logout_auth(request)
    messages.info(request, 'Sesión finalizada.')
    return redirect(index)

"""
def login(request):
    #form = login_usuarios()
    if request.method == "POST":
        form = login_usuarios(request.POST )
        if form.is_valid():
            user = authenticate( username = form.cleaned_data['usuario'], password = form.cleaned_data['contrasena'] )
            if user is not None:
                if user.is_active:
                    # Clave correcta, y el usuario está marcado "activo"
                    auth_login(request, user)
                    return redirect(index)
                else:
                #errors = form._errors.setdefault("__all__", ErrorList())
                #errors.append(u"Nombre de usuario y / ó contraseña incorrectos")
                    raise forms.ValueError("Nombre de usuario y / ó contraseña incorrectos")
        else:
            #errors = form._errors.setdefault("__all__", ErrorList())
            #errors.append(u"Nombre de usuario y / ó contraseña incorrectos")
            raise forms.ValueError("Nombre de usuario y / ó contraseña incorrectos")

            user = form.cleaned_data.get("usuario")
            if user == "alex":
                return redirect(index)
            else:
                raise ValidationError('Usuario y/o contraseña inválido')

    else:
        form = login_usuarios()

    context = {
        "login_form":form,
    }
    return render(request,"login.html",context)

def logout(request):
    logout_auth(request)
    messages.info(request, 'Sesión finalizada.')
    return redirect(index)

"""
