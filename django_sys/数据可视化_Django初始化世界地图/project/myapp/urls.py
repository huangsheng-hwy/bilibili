from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^django_demo', views.django_demo),
    url(r'^data_demo', views.data_demo),
]
