from django.db import models

# Create your models here.
class Place(models.Model) :
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=300)
    street = models.CharField(max_length=30)
    number = models.CharField(max_length=10)
    postalcode = models.CharField(max_length=10)
    suburb = models.CharField(max_length=30)
    city = models.CharField(max_length=15)
    state = models.CharField(max_length=15)
    coordinates = models.CharField(max_length=30) # "latitude, longitude" format
    def __str__(self):
     return self.name
