from django.shortcuts import render, get_object_or_404
from django.contrib.auth.views import LoginView
from .models import Waiter


# List all waiters
def index(request):
    waiters = Waiter.objects.all()
    return render(request, 'index.html')

def tip(request):
    waiters = Waiter.objects.all()
    return render(request, 'home.html', {'waiters': waiters})

def services(request):
    waiters = Waiter.objects.all()
    return render(request, 'service.html')

def about(request):
    waiters = Waiter.objects.all()
    return render(request, 'about.html')

def contact(request):
    waiters = Waiter.objects.all()
    return render(request, 'contact.html')

class CustomLoginView(LoginView):
    template_name = 'login.html'


# Waiter detail view
def waiter_detail(request, waiter_id):
    waiter = get_object_or_404(Waiter, id=waiter_id)
    return render(request, 'admin.html', {'waiter': waiter})

##############################################################################
# views.py
from django.conf import settings
import razorpay
from django.shortcuts import render, get_object_or_404
from .models import Waiter

def waiter_detail(request, waiter_id):
    waiter = get_object_or_404(Waiter, id=waiter_id)
    
    amount_param = request.GET.get('amount', 0)
    
    try:
        amount = int(amount_param) * 100  # Razorpay accepts amount in paise
        if amount <= 0:
            raise ValueError("Invalid tip amount")
    except:
        return render(request, 'tip_waiter.html', {
            'waiter': waiter,
            'error': "Invalid tip amount.",
            'amount_display': amount_param,
            'razorpay_key': settings.RAZORPAY_KEY_ID
        })

    # Create Razorpay order
    client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))
    order_data = {
        'amount': amount,
        'currency': 'INR',
        'payment_capture': 1
    }
    order = client.order.create(data=order_data)

    return render(request, 'tip_waiter.html', {
        'waiter': waiter,
        'razorpay_key': settings.RAZORPAY_KEY_ID,
        'order_id': order['id'],
        'amount': amount,
        'amount_display': amount_param
    })





