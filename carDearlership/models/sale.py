from django.db import models
from django.forms import ModelForm
from .car import Car


class Sale(models.Model):
    buyerName = models.CharField(max_length=30,verbose_name="Buyer's Name")
    buyerInfo = models.CharField(max_length=30,verbose_name="Buyer`s Contact Number")
    car= models.ForeignKey(Car, on_delete=models.DO_NOTHING)


class SaleForm(ModelForm):
    class Meta:
        model = Sale
        fields = ['buyerName','buyerInfo']
