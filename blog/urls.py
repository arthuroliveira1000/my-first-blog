from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.post_list), 
    #Essa expressão regular corresponderá a ^ (um começo) seguido por $ (fim) - então somente uma seqüência vazia irá corresponder.
]