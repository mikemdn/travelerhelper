
from django.conf.urls import url, include
from django.contrib import admin
from . import views

app_name = 'findways'

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^signin/$', views.signin, name = 'signin'),
    url(r'^signup/$', views.signup, name = 'signup')
]