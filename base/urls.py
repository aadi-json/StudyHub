from django.contrib import admin
from django.urls import path
from base.views import *

urlpatterns = [
    path('register/', registerUser, name="register"),
    path('login/', loginPage, name="login"),
    path('logout/', logoutUser, name="logout"),
    path('', home, name="home"),
    path('room/<str:pk>/', rooms, name="rooms"),
    path('create-room/', createRoom, name="create-room"),
    path('update-room/<str:pk>/', updateRoom, name="update-room"),
    path('delete-room/<str:pk>/', deleteRoom, name="delete-room")
]
