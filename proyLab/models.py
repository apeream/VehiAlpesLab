# -*- coding: utf-8 -*-
# from __future__ import unicode_literals

from django.db import models

# Create your models here.

# Clase Vendedor: Define un Vendedor para la venta de vehiculo
from django.forms import ModelForm


class Vendedor(models.Model):
    nombre = models.CharField(max_length=250, null=True)

# Clase Perfil: Define un Perfil de compra de interés para VehiAlpes
class Perfil(models.Model):
    R_18_30 = 0
    R_30_40 = 1
    R_40_50 = 2
    R_50_60 = 3
    R_60_100 = 4
    RANGO_CHOICES = (
        (R_18_30, 'De 18 a 30 años'),
        (R_30_40, 'De 30 a 40 años'),
        (R_40_50, 'De 40 a 50 años'),
        (R_50_60, 'De 50 a 60 años'),
        (R_60_100, 'De 60 a 100 años')
    )
    rango = models.IntegerField(choices=RANGO_CHOICES, null=False)
    tieneCarro = models.BooleanField(null=False)
    sugerencia = models.CharField(max_length=250, null=True)
    vendedores = models.ManyToManyField(Vendedor, through='PerfilVendedor')

class PerfilVendedor(models.Model):
    vendedor = models.ForeignKey(Vendedor)
    perfil = models.ForeignKey(Perfil)

# Clase Prospecto: Define un Prospecto para la compra de vehiculo
class Prospecto(models.Model):
    R_18_30 = 0
    R_30_40 = 1
    R_40_50 = 2
    R_50_60 = 3
    R_60_100 = 4
    RANGO_CHOICES = (
        (R_18_30, 'De 18 a 30 años'),
        (R_30_40, 'De 30 a 40 años'),
        (R_40_50, 'De 40 a 50 años'),
        (R_50_60, 'De 50 a 60 años'),
        (R_60_100, 'De 60 a 100 años')
    )
    nombre = models.CharField(max_length=250, null=True)
    rango = models.IntegerField(choices=RANGO_CHOICES, null=False)
    tieneCarro = models.BooleanField(null=False)
    vendedor = models.ForeignKey(Vendedor, related_name='prospectos', null=True, on_delete=models.CASCADE)

class ProspectoForm(ModelForm):

    class Meta:
        model = Prospecto
        fields = ['nombre', 'rango', 'tieneCarro']