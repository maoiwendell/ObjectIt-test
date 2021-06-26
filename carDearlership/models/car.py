from django.db import models
from django.db.models import Model
from django.forms import ModelForm
from django.core.validators import MaxValueValidator, MinValueValidator


class Car(models.Model):
    POOR = 'poor'
    FAIR = 'fair'
    GOOD = 'good'
    EXCELLENT = 'excellent'
    CONDITION_CHOICES = [
        (POOR, 'Poor'),
        (FAIR, 'Fair'),
        (GOOD, 'Good'),
        (EXCELLENT, 'Excellent'),
    ]
    sellerName = models.CharField(max_length=30,verbose_name="Seller name")
    sellerNumber = models.CharField(max_length=30,verbose_name="Seller mobile")
    carMake = models.CharField(max_length=30,verbose_name="Make")
    carModel = models.CharField(max_length=30,verbose_name="Model")
    carYear = models.CharField(max_length=4,verbose_name="Year")
    carCondition = models.CharField(max_length=10,
        choices=CONDITION_CHOICES,verbose_name="Condition")
    carPrice = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(100000),
            MinValueValidator(1000)
        ],verbose_name="Asking Price")

class CarForm(ModelForm):
    class Meta:
        model = Car
        fields = ['sellerName', 'sellerNumber', 'carMake', 'carModel','carYear','carCondition','carPrice']
