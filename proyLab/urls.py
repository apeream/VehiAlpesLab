from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^agregar/$', views.agregar_prospecto, name='agregarProspecto'),
]