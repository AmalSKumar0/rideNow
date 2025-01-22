from django.shortcuts import *
from django.http import HttpResponse
# from .forms import DriverRegistrationForm
from django.contrib import messages
from django.contrib.auth.hashers import check_password, make_password
from driver.models import *
from passenger.models import *

# from passenger.models import passenger
# from driver.models import driver

def home(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')

def AdminLogin(request):
    return HttpResponse('Admin Login')

def driverLogin(request):
    if request.method == 'POST':
            email = request.POST.get('email')
            password = request.POST.get('password')
            try:
                driver = Drivers.objects.get(email=email)
                if check_password(password, driver.password):
                    # request.session['driver_id'] = driver.driver_id  # Save driver ID in session
                    return redirect('driver')  # Redirect to the driver dashboard
                else:
                    err = "Incorrect password"
            except Passengers.DoesNotExist:
                 err = "User not found"
    return render(request,'Registration/driverLogin.html')

def passLogin(request):
    if request.method == 'POST':
            email = request.POST.get('email')
            password = request.POST.get('password')
            try:
                passenger = Passengers.objects.get(email=email)
                if check_password(password, passenger.password):
                    # request.session['driver_id'] = driver.driver_id  # Save driver ID in session
                    return redirect('driver')  # Redirect to the driver dashboard
                else:
                    err = "Incorrect password"
            except Passengers.DoesNotExist:
                 err = "User not found"
    return render(request,'Registration/passengerLogin.html')

def passRegister(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # Validate passwords
        if password != confirm_password:
            messages.error(request, "Passwords do not match!")
            return render(request, 'Registration/passengerRegister.html')

        # Save data to the database
        Passengers.objects.create(
            name=name,
            email=email,
            phone=phone,
            address=address,
            password=make_password(password)  # Hash the password
        )

        messages.success(request, "Account created successfully!")
        return redirect('driver')
    return render(request,'Registration/passengerRegister.html')

def driverReg(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        vehicle_type = request.POST.get('vehicle_type')
        manufacture_date = request.POST.get('manufacture_date')
        license_number = request.POST.get('license_number')
        vehicle_number = request.POST.get('vehicle_number')
        vehicle_image = request.FILES.get('vehicle_image')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # Validate passwords
        if password != confirm_password:
            messages.error(request, "Passwords do not match!")
            return render(request, 'Registration/driverRegister.html')

        # Save data to the database
        NewDrivers.objects.create(
            name=name,
            email=email,
            phone=phone,
            address=address,
            vehicle_type=vehicle_type,
            manufacture_date=manufacture_date,
            license_number=license_number,
            vehicle_number=vehicle_number,
            vehicle_image=vehicle_image,
            password=make_password(password)  # Hash the password
        )

        messages.success(request, "Account created successfully!")
        return redirect('driver')  # Replace with your success page or URL

    return render(request, 'Registration/driverRegister.html')


def AdminLogin(request):
    return render(request,'Registration/adminLogin.html') 

def driver(request):
    return HttpResponse('hello world')
