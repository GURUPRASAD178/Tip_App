from django.db import models

# Create your models here.

class Waiter(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='waiter_photos/')
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    joined_date = models.DateField(auto_now_add=True)
    contact_number = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    total_tips_received = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return self.name