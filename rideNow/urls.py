from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from django.shortcuts import render
from .views import *
from passenger.views import *
from driver.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='home'),
    path('contact/',contact,name="contact"),
    path('admin login/',AdminLogin,name="adminLogin"),
    path('passenger login/',passLogin,name="passengerLogin"),
    path('driver login/',driverLogin,name="driverLogin"),
    path('passenger Register/',passRegister,name="passReg"),
    path('driver register/',driverReg,name="driverReg"),
    path('driver/',driver,name="driver"),
    path('admindash/',admindash,name="admindash"),
    path('passenger_page/',passenger_page, name='passengerPage'),
    path('profile/',profile,name="profile"),
    path('driver_page/',driver_page, name='driverpage'),
]