from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Persona(models.Model):
    rut = models.CharField(max_length=30, unique=True, verbose_name='ingrese su rut' )
    nombre = models.TextField(max_length=45, verbose_name= 'ingrese su nombre')
    apellido = models.TextField(max_length=45, verbose_name= 'ingrese su apellido')
    direccion = models.CharField(max_length=45, verbose_name='ingrese su direccion')
    idUser = models.OneToOneField(User,models.CASCADE,primary_key=True)