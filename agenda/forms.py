from django import forms

from agenda.models import Citas
from django.contrib.admin import widgets


class CitasForms(forms.ModelForm):


    def __init__(self, *args, **kwargs):
        super(CitasForms, self).__init__(*args, **kwargs)
        self.fields['fecha_limite'].widget = widgets.AdminSplitDateTime()
        self.fields['agenda'].widget = forms.HiddenInput()

    class Meta:
         model = Citas
         fields = ['agenda', 'nombre', 'descripcion', 'fecha_limite']