from django.db import models
from modulo.medicamentos.models import Medicamentos

# Create your models here.


class Prescripcion(models.Model):
    descripcion = models.CharField(max_length=256,null=False)
    medicamento = models.ForeignKey(Medicamentos, on_delete = models.CASCADE)