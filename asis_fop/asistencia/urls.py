from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^colegio/(?P<colegio_id>[0-9]+)/$', views.cursos, name='cursos'),
    url(r'^curso/(?P<curso_id>[0-9]+)/(?P<periodo>[0-9]+)/$', views.lista, name='lista'),
    url(r'^pasarlista/(?P<curso_id>[0-9]+)/(?P<periodo>[0-9]+)/$', views.pasarlista, name='pasarlista'),
]