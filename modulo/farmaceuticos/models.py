from django.db import models
from modulo.persona.models import Persona

# Create your models here.

class Quimico(models.Model):
    idPersona = models.ForeignKey(Persona,on_delete= models.CASCADE)
    