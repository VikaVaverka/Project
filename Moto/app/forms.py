from django import forms
from django.core.exceptions import ValidationError
import datetime
from .models import Order, Motorcycle

class Client(forms.Form):
    # fist_name = forms.CharField(max_length=50, label='First Name')
    # last_name = forms.CharField(max_length=50, label='Last Name')
    # email = forms.EmailField(max_length=100, label='E-mail')
    # number_phone = forms.CharField(max_length=13, label='Number Phone')
    # password = forms.CharField(max_length=100, label='Password')
    model = Order

    def __str__(self):
        return f'{self.fist_name} {self.last_name}'

class MakeOrder(forms.Form):

    product = forms.CharField(max_length=50, label='Product')
    price = forms.CharField(max_length=4, label='Price')
    customer = forms.CharField(max_length=50, label='Customer')
    address = forms.CharField (max_length=50, label='Adress')
    email = forms.EmailField()
    phone = forms.CharField (max_length=50, label='Phone')

    def __str__(self):
        return f'{self.product} {self.customer}'