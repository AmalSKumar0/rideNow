from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from django.shortcuts import render
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='home'),
    path('contact/',contact,name="contact"),
    path('admin login/',AdminLogin,name="adminLogin"),
    path('passenger/',passLogin,name="passengerLogin"),
    path('driver login/',driverLogin,name="driverLogin"),
    path('passenger Register/',passRegister,name="passReg"),
    path('driver register/',driverReg,name="driverReg"),
    path('driver/',driver,name="driver"),
]
