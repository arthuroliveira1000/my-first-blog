from django.conf.urls import url
from usuarios import views


urlpatterns = [
   url(r'^registrar/$', views.RegistrarUsuarioView.as_view(), name='registrar')
]