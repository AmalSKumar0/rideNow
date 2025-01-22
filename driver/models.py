from django.db import models
from django.contrib.auth.hashers import make_password

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
    live_location = models.CharField(max_length=255, default="")  # Stores place name as a string
    is_active = models.BooleanField(default=False)  # True if the driver is available for a ride

    def __str__(self):
        return self.name

