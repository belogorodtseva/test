from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^chooseapp/', views.chooseapp, name='chooseapp'),
    url(r'^addapp/', views.addapp, name='addapp'),
    #url(r'^chooseapp_time/(?P<pk>[0-9]+)/', views.chooseapp_time, name='chooseapp_time'),
    ]
