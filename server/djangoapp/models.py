from django.db import models
from django.utils.timezone import now


# Create your models here.

# <HINT> Create a Car Make model `class CarMake(models.Model)`:

from django.db import models

class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    # Add any other fields you would like to include for a car make here

    def __str__(self):
        return self.name



# <HINT> Create a Car Model model `class CarModel(models.Model):`:


from django.db import models

class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    # Add any other fields you would like to include for a car make here

    def __str__(self):
        return self.name

class CarModel(models.Model):
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE, related_name='car_models')
    dealer_id = models.IntegerField()
    name = models.CharField(max_length=100)
    TYPE_CHOICES = [
        ('Sedan', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'WAGON'),
    ]
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    year = models.DateField()

    # Add any other fields you would like to include for a car model here

    def __str__(self):
        return f"{self.car_make.name} {self.name}"


# <HINT> Create a plain Python class `CarDealer` to hold dealer data


# <HINT> Create a plain Python class `DealerReview` to hold review data
