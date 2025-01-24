from django.db import models
from django.contrib.auth.hashers import make_password
from passenger.models import Passenger


class NewDrivers(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    vehicle_type = models.CharField(
        max_length=20,
        choices=[
            ('Auto Rickshaw', 'Auto Rickshaw'),
            ('Economy Car', 'Economy Car'),
            ('Sedan', 'Sedan'),
            ('Luxury Car', 'Luxury Car')
        ]
    )
    manufacture_date = models.DateField()
    license_number = models.CharField(max_length=50, unique=True)
    vehicle_number = models.CharField(max_length=20, unique=True)
    vehicle_image = models.ImageField(upload_to='uploads/vehicles/')
    password = models.CharField(max_length=255)  # Increase length for hashed password

    def save(self, *args, **kwargs):
        # Hash the password before saving
        if self.password:
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    

class Drivers(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    vehicle_type = models.CharField(
        max_length=20,
        choices=[
            ('Auto Rickshaw', 'Auto Rickshaw'),
            ('Economy Car', 'Economy Car'),
            ('Sedan', 'Sedan'),
            ('Luxury Car', 'Luxury Car')
        ]
    )
    manufacture_date = models.DateField()
    license_number = models.CharField(max_length=50, unique=True)
    vehicle_number = models.CharField(max_length=20, unique=True)
    vehicle_image = models.ImageField(upload_to='uploads/vehicles/')
    password = models.CharField(max_length=50)
    current_location = models.CharField(max_length=255, default="")  # Stores place name as a string
    is_active = models.BooleanField(default=False)  # True if the driver is available for a ride

    def __str__(self):
        return self.name

# Create your models here.




class CompletedBookings(models.Model):
    booking_id = models.IntegerField(primary_key=True)
    pass_id = models.IntegerField(null=True, blank=True)
    driver_id = models.IntegerField(null=True, blank=True)
    status = models.CharField(max_length=20, null=True, blank=True)
    completion_time = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Completed Booking {self.booking_id} with status {self.status}"


class Bookings(models.Model):
    book_id = models.AutoField(primary_key=True)
    pass_id = models.IntegerField(null=True, blank=True)
    driver = models.ForeignKey(Drivers, on_delete=models.CASCADE, related_name="bookings")
    from_location = models.CharField(max_length=255, null=True, blank=True)
    to_location = models.CharField(max_length=255, null=True, blank=True)
    landmark = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=50, null=True, blank=True)
    OTP = models.IntegerField(null=True, blank=True)
    distance = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"Booking {self.book_id} from {self.from_location} to {self.to_location}"



class Reviews(models.Model):
    review_id = models.AutoField(primary_key=True)
    pass_id = models.ForeignKey(Passenger, on_delete=models.CASCADE, null=True, blank=True)
    driver_id = models.ForeignKey(Drivers, on_delete=models.CASCADE, null=True, blank=True)
    review_text = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    stars = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"Review {self.review_id} for Driver {self.driver_id}"


