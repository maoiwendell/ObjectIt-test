from django.test import TestCase
from carDearlership.models import Car

class CarTestCase(TestCase):
    def setUp(self):
        Car.objects.create(
            sellerName="Jane Doe",
            sellerNumber="645215253",
            carMaker="Mitsubishi",
            carModel="rev",
            carYear="1975",
            carCondition="fair",
            carPrice=10)

    def test_cars_created(self):
        """Cars has been created."""
        car = Car.objects.get(sellerName="Jane Doe")
        self.assertTrue(car)
