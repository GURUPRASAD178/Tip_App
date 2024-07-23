from django.db import models

class Waiter(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='waiters/')
    payment_link = models.URLField(max_length=200)

    def __str__(self):
        return self.name

class Waiter1(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='waiters/')
    payment_link = models.URLField(max_length=200)

    def __str__(self):
        return self.name
    
    from django.db import models

