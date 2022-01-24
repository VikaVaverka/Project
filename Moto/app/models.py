from django.db import models
import datetime

class Motorcycle(models.Model):
    brand = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    image = models.ImageField(upload_to='image/', blank=True)
    price = models.CharField(max_length=10)
    
    def __str__(self):
        return f'{self.brand} {self.name} {self.color}'


class Order(models.Model):

    product = models.ForeignKey(Motorcycle,on_delete=models.CASCADE)
    customer = models.CharField(max_length=100, default='', blank=True)
    price = models.CharField(max_length=4)
    email = models.EmailField()
    address = models.CharField (max_length=100, default='', blank=True)
    phone = models.CharField (max_length=50, default='', blank=True)
    date = models.DateField (default=datetime.datetime.today)
    status = models.BooleanField (default=False)

    def __str__(self):
        return f'{self.product} {self.customer}'