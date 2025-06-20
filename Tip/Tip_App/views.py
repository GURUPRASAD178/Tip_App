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
