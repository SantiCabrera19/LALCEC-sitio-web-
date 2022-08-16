from django.db import models
# Create your models here.

class prueba(models.model):
    title = models.CharField(max_lenght=50)
    description = models.TextField(blank=True)