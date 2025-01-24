from django.db import models


class Passenger(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    password = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name

