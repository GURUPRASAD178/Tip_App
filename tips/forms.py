from django import forms
from .models import Waiter

class WaiterForm(forms.ModelForm):
    class Meta:
        model = Waiter
        fields = ['name', 'photo', 'payment_link']
