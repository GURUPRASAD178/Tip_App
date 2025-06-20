from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'John Doe'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control', 'placeholder': 'name@example.com'
    }))
    message = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control', 'placeholder': 'How can we help?', 'rows': 5
    }))
