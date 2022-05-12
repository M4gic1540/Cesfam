from django.db import models

from modulo.tipoMovimiento.models import detalleMovimiento
# Create your models here.

class stockMedicamento(models.Model):
    fecha_creacion = models.DateField()
    movimiento = models.TextField(max_length=40)
    detalleMovimiento = models.ForeignKey(detalleMovimiento,models.CASCADE,null=True)