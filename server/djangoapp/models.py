from django.db import models
from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

# Car Make model: a manufacturer such as Toyota or Audi
class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    # Any other fields you would like to include in car make model
    country = models.CharField(max_length=100, blank=True, default="")

    def __str__(self):
        return self.name  # Return the name as the string representation


# Car Model model: a model made by a car make, such as the Corolla by Toyota
class CarModel(models.Model):
    # Many-To-One relationship: one Car Make has many Car Models
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    # Dealer ID refers to a dealer stored in the Mongo database
    dealer_id = models.IntegerField(null=True, blank=True)
    name = models.CharField(max_length=100)

    CAR_TYPES = [
        ('Sedan', 'Sedan'),
        ('SUV', 'SUV'),
        ('Wagon', 'Wagon'),
    ]
    type = models.CharField(max_length=10, choices=CAR_TYPES, default='SUV')
    year = models.IntegerField(
        default=2023,
        validators=[
            MaxValueValidator(2023),
            MinValueValidator(2015),
        ],
    )
    # Any other fields you would like to include in car model
    created_at = models.DateTimeField(default=now)

    def __str__(self):
        return self.car_make.name + " " + self.name  # Make and model name
