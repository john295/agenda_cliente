from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Agenda(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30, null=True)
    usuario = models.OneToOneField(User)

    def __str__(self):
        return str(self.id)


class Citas(models.Model):
    id = models.AutoField(primary_key=True)
    agenda = models.ForeignKey(Agenda)
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=300, null=True, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_limite = models.DateTimeField()

    def __str__(self):
        return self.nombre