from django.shortcuts import render,redirect
from .forms import searchAuto
from .models import Passenger
from driver.models import Drivers,Bookings,CompletedBookings,Reviews
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.urls import reverse
from.utils import get_distance_between_places,generate_otp,calculate_trip_price


def passenger_page(request):

    request.session['whoami']=1

    if 'passengerFlag' in request.session:
        flag = request.session['passengerFlag']
    elif Bookings.objects.filter(pass_id=request.session['passenger_id']):
        flag = 3
    else:
        flag = 1

    paymentwindow = request.session.get('paymentwindow', False)
    reviewFlag = request.session.get('reviewFlag', False)
    
    # Retrieve session data for error handling
    err = request.session.get('err', '')
    error = request.session.get('error', '')
    distance = request.session.get('distance', 0)
    price = request.session.get('price', 0)

    # Button actions
    # If passenger clicks "another location" button
    if request.GET.get('another_location') == 'true':
        request.session['passengerFlag'] = 1
        return HttpResponseRedirect(reverse('passengerPage'))
    
    # If passenger tries to pay for the auto
    if 'payment' in request.GET:
        request.session['lookedupdriver'] = request.GET['payment']
        request.session['paymentwindow'] = True
        return HttpResponseRedirect(reverse('passengerPage'))
    
    # If passenger clicks "Back" to view other autos
    if 'Back' in request.GET:
        request.session['paymentwindow'] = False
        return HttpResponseRedirect(reverse('passengerPage'))
    
    # If passenger pays and books the auto
    if 'BookDriver' in request.GET:
        bookings = Bookings(
            pass_id=request.session['passenger_id'],
            driver_id=request.GET['BookDriver'],
            from_location=request.session['from'],
            to_location=request.session['to'],
            landmark=request.session['landmark'],
            status='requested',
            distance=request.session['distance'],
            price=request.session['price'],
            OTP=generate_otp()
        )
        bookings.save()
        request.session['bookingID'] = bookings.book_id
        request.session['paymentwindow'] = False
        request.session['passengerFlag'] = 3
        return redirect('passengerPage')
    
    # Review actions
    # Submit a review
    if 'submitReview' in request.GET:
        feedback = request.GET['feedback']
        text = request.GET['review_text']
        passenger_instance = Passenger.objects.get(pass_id=request.session['passenger_id'])
        driver_instance = Drivers.objects.get(driver_id=request.session['lookedupdriver'])
        review = Reviews(
            pass_id=passenger_instance,
            driver_id=driver_instance,
            stars=feedback,
            review_text=text
        )
        review.save()
        request.session['reviewFlag'] = False
        return redirect('passengerPage')
    
    # Initiate review process
    if 'review' in request.GET:
        request.session['reviewFlag'] = True
        return redirect('passengerPage')
    
    # Cancel review process
    if 'gobacktoreview' in request.GET:
        request.session['reviewFlag'] = False
        return redirect('passengerPage')
    
    # Confirm trip
    if 'confirmTrip' in request.GET:
        id = request.GET['confirmTrip']
        booking = Bookings.objects.get(id=id)
        booking.delete()
        request.session['passengerFlag'] = 2
        temp = request.session['passenger_id']
        request.session.flush()
        request.session['passenger_id'] = temp 
        return redirect('passengerPage')
    # Fetching data from models and session

    # Booking data
    if 'bookingID' in request.session:
        booking = Bookings.objects.get(book_id=request.session['bookingID'])
    else:
        booking = Bookings.objects.none()
    
    # Driver data of the viewed and booked driver
    if 'lookedupdriver' in request.session:
        lookedupdriver = Drivers.objects.get(driver_id=request.session['lookedupdriver'])
    else:
        lookedupdriver = Drivers.objects.none()
    
    # Passenger details
    passenger = Passenger.objects.get(id=request.session['passenger_id'])
    available_drivers = Drivers.objects.none()
    
    # Search functionality and form handling
    if request.method == 'POST':
        searchForm = searchAuto(request.POST)
        
        if searchForm.is_valid():
            fromLoc = searchForm.cleaned_data['from_loc']
            toLoc = searchForm.cleaned_data['to_loc']
            landmark = searchForm.cleaned_data['landmark']
            request.session['distance'] = get_distance_between_places(fromLoc, toLoc)
            request.session['price'] = calculate_trip_price(request.session['distance'])

            # Store search data in session
            request.session['from'] = fromLoc
            request.session['to'] = toLoc
            request.session['landmark'] = landmark
            
            try:
                # Attempt to find drivers in the specified location
                available_drivers = Drivers.objects.filter(
                    current_location=fromLoc
                ).exclude(
                    Q(bookings__status__isnull=False) & ~Q(bookings__status="requested")
                )
                request.session['error'] = str(available_drivers)
                
                # If drivers are found, store their IDs in session
                if available_drivers.exists():
                    request.session['available_driver_ids'] = list(available_drivers.values_list('driver_id', flat=True))
                    request.session['passengerFlag'] = 2
                else:
                    # No drivers found; update flag accordingly
                    request.session['passengerFlag'] = 2

                return redirect('passengerPage')

            except Drivers.DoesNotExist:
                # No driver found in the given location, handle gracefully
                request.session['err'] = "No drivers available at the selected location."
                request.session['passengerFlag'] = 2  # Set flag for "no drivers"
                return redirect('passengerPage')

            except Exception as e:
                # Log the actual exception and set error flag
                request.session['err'] = str(e)  # Save the exception as a string
                request.session['passengerFlag'] = 4  # Set flag for error
                print(f"Error during driver search: {e}")  # Debugging: Print the error
                return redirect('passengerPage')
    else:
        searchForm = searchAuto()
    
    # Load available drivers from session if any
    if 'available_driver_ids' in request.session:
        driver_ids = request.session['available_driver_ids']
        available_drivers = Drivers.objects.filter(driver_id__in=driver_ids)

     # Process location if set in session
     # Safely get the first word or set to an empty string if 'from' or 'to' is empty or doesn't contain spaces
    from_location = request.session.get('from', '').split()[0] if request.session.get('from', '').split() else ''
    to_location = request.session.get('to', '').split()[0] if request.session.get('to', '').split() else ''

    # If you still need to strip commas
    from_location = from_location.strip(',')
    to_location = to_location.strip(',')


    return render(request, 'passenger/passenger.html', {
        'passenger_details': passenger,
        'flag': flag,
        'searchForm': searchForm,
        'driverInLocation': available_drivers,
        'from': from_location,
        'to': to_location,
        'err': err,
        'error': error,
        'paymentwindow': paymentwindow,
        'distance': distance,
        'price': price,
        'lookedupdriver': lookedupdriver,
        'booking': booking,
        'reviewFlag': reviewFlag,
    })

# def passenger_login(request):
#     err = ''
#     if request.method == 'POST':
#         login_form = PassengerLoginForm(request.POST)
#         register_form = PassengerRegistrationForm(request.POST)

#         if login_form.is_valid():  # Check login form validity
#             email = login_form.cleaned_data['email_id']
#             password = login_form.cleaned_data['password']
#             try:
#                 passenger = Passenger.objects.get(email=email)
#                 if passenger.password == password:
#                     request.session['passenger_id'] = passenger.pass_id
#                     if 'passengerFlag' in request.session:
#                         del request.session['passengerFlag']
#                     return redirect('passengerPage')
#                 else:
#                     err = "Incorrect password"
#             except Passenger.DoesNotExist:
#                 err = "User not found"
        
#         # Check registration form validity
#         elif register_form.is_valid():
#             name = register_form.cleaned_data['name']
#             email = register_form.cleaned_data['email']
#             gender = register_form.cleaned_data['gender']
#             address = register_form.cleaned_data['address']
#             phone_no = register_form.cleaned_data['phone']
#             password = register_form.cleaned_data['password']
#             try:
#                 new_passenger = Passenger(
#                     name=name,
#                     email=email,
#                     gender=gender,
#                     address=address,
#                     phone_no=phone_no,
#                     password=password
#                 )
#                 new_passenger.save()
#                 passenger = Passenger.objects.get(email=email)
#                 request.session['passenger_id']=passenger.pass_id
#                 if 'passengerFlag' in request.session:
#                     del request.session['passengerFlag']
#                 return redirect('passengerPage')  # Redirect to a success page
#             except Exception as e:
#                 err = str(e)
#     else:
#         login_form = PassengerLoginForm()
#         register_form = PassengerRegistrationForm()

#     return render(request, 'passenger/PassReg.html', {'RegisterForm': register_form, 'LoginForm': login_form, 'err': err})
