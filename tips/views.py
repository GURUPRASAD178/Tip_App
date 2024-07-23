from django.shortcuts import render,redirect,get_object_or_404

from .models import Waiter

def waiter_list(request):
    waiters = Waiter.objects.all()
    return render(request, 'tips/waiter_list.html', {'waiters': waiters})

def payment(request):
    waiters = Waiter.objects.all()
    return render(request, 'tips/payment.html', {'waiters': waiters})

def adminlogin(request):
    waiters = Waiter.objects.all()
    return render(request, 'tips/admin.html',{'waiters': waiters})




from .forms import WaiterForm
def add_waiter(request):
    if request.method == 'POST':
        form = WaiterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('waiter_list')
    else:
        form = WaiterForm()
    return render(request, 'tips/add_waiter.html', {'form': form})

