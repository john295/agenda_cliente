"""agenda_cliente URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.decorators import login_required

from agenda import views as agendaViews


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^/?$', agendaViews.IndexView.as_view(), name='index'),
    url(r'^my_admin/jsi18n', 'django.views.i18n.javascript_catalog'),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', name="my_login"),
    url(r'^login/$', 'django.contrib.auth.views.login', name="my_login"),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name="my_logout", kwargs={'next_page': '/'}),
    url(r'^registrar/?', agendaViews.RegisterView.as_view(), name="register"),
    url(r'^citas/crear/?', login_required(agendaViews.AgendaCitasCreationView.as_view()), name="citas_creation"),
    url(r'^agenda/?', login_required(agendaViews.AgendaView.as_view()), name="agenda")
]
