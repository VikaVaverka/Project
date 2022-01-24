from django.shortcuts import redirect, render
from app.forms import MakeOrder
from app.models import Order

import datetime

def home(request):
    return render(request, 'home.html')

def order(request):

    if request.method == 'POST':
        form = MakeOrder(request.POST)

        if form.is_valid():
            order_ent = Order()
            product = form.cleaned_data['product']
            customer = form.cleaned_data['customer']
            price = form.cleaned_data['price']
            address = form.cleaned_data['address']
            phone = form.cleaned_data['phone']
            date = datetime.datetime.now()

            return redirect('thanks')
    else:
        form = MakeOrder()
    
    return render(request, 'order.html', {'form': form})


def thanks(request):
    thanks = 'thanks'
    return render(request, 'thanks.html', {'thanks': thanks})