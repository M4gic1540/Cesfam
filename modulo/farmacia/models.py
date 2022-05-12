from django.db import models
from modulo.farmaceuticos.models import Quimico
from modulo.persona.models import Persona
from modulo.paciente.models import Paciente
from modulo.prescripciones.models import Prescripcion
# Create your models here.

class Personal(models.Model):
    idPersona = models.ForeignKey(Persona,on_delete= models.CASCADE)
    idQuimico = models.ForeignKey(Quimico,on_delete= models.CASCADE)

class fichasPacientes(models.Model):
    pacienteid = models.OneToOneField(Paciente,models.CASCADE)
    nombrePaciente = models.ForeignKey(Persona,models.CASCADE)
    descripcionMedicamento = models.ForeignKey(Prescripcion,models.CASCADE)
