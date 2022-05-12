from django.db import models

# Create your models here.

class detalleMovimiento(models.Model):
    detalle = models.CharField(max_length=45)