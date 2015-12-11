from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Agenda(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30, null=True)
    usuario = models.ForeignKey(User)