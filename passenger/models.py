from django.db import models
from django.contrib.auth.hashers import make_password

# Create your models here.
class Passengers(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    password = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name