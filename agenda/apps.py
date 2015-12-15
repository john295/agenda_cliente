from django.apps import AppConfig
import threading
import time
import datetime

from agenda.models import Citas


class CitaCheckThread(threading.Thread):

    def run(self):
        while True:
            today = datetime.datetime.today()
            citas = Citas.objects.filter(fecha_limite__lte=today)
            citas.delete()
            time.sleep(10)

class AgendaConfig(AppConfig):
    name = 'agenda'

    def ready(self):
        cita_check_thread = CitaCheckThread()
        cita_check_thread.start()
