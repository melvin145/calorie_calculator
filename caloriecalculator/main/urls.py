from django.conf.urls import url
from django.urls import path
from django.contrib import admin

from . import views
from django.urls import path

urlpatterns=[
    path("",views.home,name='homes'),
    path('result',views.calculations,name='calculation')
]