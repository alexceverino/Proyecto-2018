from django import forms
from itertools import cycle
from .models import *
from datetime import datetime, date, timedelta
import time

#from .validator import *
from django.core.exceptions import ValidationError

class AgregarSentencia(forms.Form):
    juez = forms.CharField(max_length=100)
    norma_aplicada = forms.CharField(max_length=150)
    #combobox que consulta a la base de datos
    tribunales = forms.ModelChoiceField(queryset=tribunal.objects.all())
    fecha_sentencia = forms.DateField()
    materias_sentencia = forms.CharField(max_length=100)
    sentencia = forms.CharField(max_length=500,widget=forms.Textarea)

from django.contrib.auth import (
authenticate,
get_user_model,
login,
logout,
)

User = get_user_model()


class login_usuarios(forms.Form):
    usuario = forms.CharField(max_length = 50)
    contrasena = forms.CharField(widget=forms.PasswordInput,max_length = 50)

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get("usuario")
        password = self.cleaned_data.get("contrasena")
        user = authenticate( username = username, password = password )
        if not user:
            raise forms.ValidationError("Usuario no existe.")
        if not user.check_password(password):
            raise forms.ValidationError.get("Usuario incorrecto.")
        if not user.is_active:
            raise forms.ValidationError("Usser no existe")
        return super(login_usuarios,self).clean(*args,**kwargs)
