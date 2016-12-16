from django.conf.urls import url
from django.contrib import admin
from perfis import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^perfis/(?P<perfil_id>\d+)$', views.exibir, name='exibir'),
    url(r'^perfis/(?P<perfil_id>\d+)/convidar$', views.convidar, name='convidar'),
    url(r'^convite/(?P<convite_id>\d+)/aceitar$', views.aceitar, name='aceitar'),

    #SEMPRE DAR NOMES PRAS URLS E CHAMALAS NOS LINKS USADOS NAS PAGINAS PELO NOME
    #PQ ASSIM A MANUTENÇÃO DO SISTEMA FICA BEM MAIS FACIL
]