from django.contrib import admin
from django.urls import path
from base.views import *

urlpatterns = [
    path('', home, name="home"),
    path('room/' , rooms, name="rooms")
]
