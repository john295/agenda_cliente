# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Citas',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('nombre', models.CharField(max_length=30)),
                ('descripcion', models.CharField(max_length=300, null=True, blank=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_limite', models.DateTimeField()),
                ('agenda', models.ForeignKey(to='agenda.Agenda')),
            ],
        ),
    ]
