from django.db import models
from modulo.persona.models import Persona
from modulo.prescripciones.models import Prescripcion
# Create your models here.

class Paciente(models.Model):
    idPersona = models.ForeignKey(Persona, models.DO_NOTHING)
    receta = models.ForeignKey(Prescripcion,models.CASCADE)
    diagnostico = models.TextField()
