from __future__ import unicode_literals

from django.db import models


class Pais(models.Model):
    nombre = models.CharField(max_length=120, null=True, blank=True)


class Ciudad(models.Model):
    nombre = models.CharField(max_length=120, null=True, blank=True)
    pais = models.ForeignKey(Pais, on_delete=models.PROTECT)


class TipoPersona(models.Model):
    '''
    Fisica, Jurica, etc
    '''
    nombres = models.CharField(max_length=120, null=True, blank=True)


class UniqueId(models.Model):
    '''
    Tipo de identifdicador, cuit para empresas, DNI para personas
    '''
    nombres = models.CharField(max_length=120, null=True, blank=True)


class Persona(models.Model):
    nombres = models.CharField(max_length=120, null=True, blank=True)
    tipo = models.ForeignKey(TipoPersona, on_delete=models.PROTECT)
    tipo_uid = models.ForeignKey(UniqueId, on_delete=models.PROTECT)
    uid = models.CharField(max_length=90, null=True, blank=True)


class TipoRelacion(models.Model):
    # familiar, aportante, socio, amigo, etc
    nombre = models.CharField(max_length=120)


class Relacion(models.Model):
    '''
    Relacion entre dos personas
    '''
    persona1 = models.ForeignKey(Persona, on_delete=models.PROTECT, related_name='Relacion.Persona1+')
    persona2 = models.ForeignKey(Persona, on_delete=models.PROTECT, related_name='Relacion.Persona2+')
    relacion = models.ForeignKey(TipoRelacion, on_delete=models.PROTECT)
    #TODO fecha de inicio y fecha de fin


