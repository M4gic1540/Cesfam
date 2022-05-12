from django.db import models
from modulo.stock.models import stockMedicamento
# Create your models here.

class Medicamentos(models.Model):
    nombre = models.CharField(max_length=45, unique = True)
    fecha_vencimiento = models.DateField()
    lote = models.CharField(max_length=45, unique=True)
    miligramos = models.CharField(max_length=256)
    cuidadosEsp = models.CharField(max_length=5)
    stock= models.ForeignKey(stockMedicamento,models.CASCADE)
    