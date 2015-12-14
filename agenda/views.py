from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
from rest_framework.views import APIView

from agenda.forms import CitasForms
from agenda.models import Agenda, Citas


class IndexView(View):

    def get(self, request, *args, **kwargs):
        usuarios = User.objects.all()
        return render(request, "index.html", context={"usuarios": usuarios})



class RegisterView(View):

    def get(self, request, *args, **kwargs):
        return render(request, "registro.html", context={"create_form": UserCreationForm()})

    def post(self, request, *args, **kwargs):
        formulario = UserCreationForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            #mensaje =  "El usuario {usuario} ha sido creado exitosamente".format(usuario=formulario.username)
            return render(request, "success.html", context={"mensaje": "que bueno funciono"})
        else:
            return render(request, "registro.html", context={"create_form": formulario})


class AgendaView(View):

    def get(self, request, *args, **kwargs):
        citas = request.user.agenda.citas_set.all()
        return render(request, "agenda.html", context={"citas": citas})



class AgendaCitasCreationView(APIView):

    def get(self, request, *args, **kwargs):
        """
        :type request: django.core.handlers.wsgi.WSGIRequest or rest_framework.request.Request
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        return render(request, "citas_creacion.html", context={"create_form": CitasForms()})

    def post(self, request, *args, **kwargs):
        """
        :type request: django.core.handlers.wsgi.WSGIRequest or rest_framework.request.Request
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        data = request.POST.copy()
        agenda, was_created = Agenda.objects.get_or_create(
                defaults={
                    'nombre': request.user.username,
                },
                usuario=request.user
        )
        data['agenda'] = str(agenda.id)
        formulario = CitasForms(data)
        if formulario.is_valid():
            formulario.save()
            return render(request, "success.html", context={"mensaje": "que bueno funciono"})
        else:
            return render(request, "citas_creacion.html", context={"create_form": formulario})

