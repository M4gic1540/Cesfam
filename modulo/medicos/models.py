from django.db import models
from modulo.persona.models import Persona

# Create your models here.

class Medico(models.Model):
    idPersona = models.ForeignKey(Persona,on_delete= models.CASCADE)
    especialidad = models.CharField(max_length=45)
    