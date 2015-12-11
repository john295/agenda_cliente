from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Create your views here.



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
            return render(request, "registro.html", context={"create_form": UserCreationForm})




class AgendaCreationView(View):

    def get(self, request, *args, **kwargs):
        return render(request, "agenda.html", context={"create_form": UserCreationForm()})

    def post(self, request, *args, **kwargs):
        pass

