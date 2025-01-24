from django.urls import path
from django.shortcuts import render
from . import views

urlpatterns = [
    path('passenger_page/', views.passenger_page, name='passengerPage'), 
]