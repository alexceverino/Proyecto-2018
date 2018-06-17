from django.db import models
from .validator import *
# Create your models here.
import datetime
import time
# modelos de la base de datos
from django.contrib.auth.models import User

class perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rut = models.CharField(max_length=50,validators=[validar_rut])
    tipo = models.CharField(max_length=50,null=False)


class tribunal(models.Model):
    id_tribunal = models.CharField(primary_key=True,max_length = 100)
    nombre_tribunal = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_tribunal

class sentencia(models.Model):
    id_sentencia = models.AutoField(primary_key=True)
    juez_sentencia = models.CharField(max_length=100)
    nombre_tribunal = models.ForeignKey('tribunal',on_delete=models.CASCADE)
    norma_aplicada = models.CharField(max_length=150)
    fecha_sentencia = models.DateField(auto_now=False)
    materias_sentencia = models.CharField(max_length=100)
    fecha_agregacion = models.DateField(auto_now=True)
    sentencia = models.CharField(max_length = 500)

    def __str__(self):
        return self.juez_sentencia


# Create your models here.
