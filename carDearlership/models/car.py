from django.db import models
from django.forms import ModelForm


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
    sellerName = models.CharField(max_length=30)
    sellerNumber = models.IntegerField()
    carMaker = models.CharField(max_length=30)
    carModel = models.CharField(max_length=30)
    carYear = models.CharField(max_length=4)
    carCondition = models.CharField(max_length=10,choices=CONDITION_CHOICES)
    carPrice = models.IntegerField()

class CarForm(ModelForm):
    class Meta:
        model = Car
        fields = ['sellerName', 'sellerNumber', 'carMaker', 'carModel','carYear','carCondition','carPrice']
