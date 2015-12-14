from django.contrib import admin
from .models import Agenda, Citas

@admin.register(Agenda)
class AgendaAdmin(admin.ModelAdmin):
    pass

@admin.register(Citas)
class CitasAdmin(admin.ModelAdmin):
    pass