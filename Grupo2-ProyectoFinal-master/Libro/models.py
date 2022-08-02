from importlib.util import module_for_loader
from statistics import mode
from django.db import models

# Create your models here.

class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=50)
    editorial = models.CharField(max_length=50)
    fecha_de_publicacion = models.DateField()
    disponible = models.BooleanField()
    