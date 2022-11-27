from django.db import models

# Create your models here.
class Equipo(models.Model):
    n_equipo = models.CharField(max_length=20)
    n_entrenador = models.CharField(max_length=20)
    n_estadio = models.CharField(max_length=20)
    titulos = models.CharField(max_length=20)
    n_ciudad = models.CharField(max_length=20)
    p_origen = models.CharField(max_length=20)   
    