from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    zipcode = models.CharField(null=True, blank=True, max_length=5)
    is_donor = models.BooleanField(default=True, blank=True)
    is_foster = models.BooleanField(default=False, blank=True)
    phone_number = models.CharField(null=True, blank=True, max_length=10)



class Registry(models.Model):
    user = models.ForeignKey(to='User', on_delete=models.CASCADE, related_name='requests')
    time_made = models.DateTimeField(auto_now_add=True, null=True)


class Item(models.Model):
    registry = models.ForeignKey(to='Registry', on_delete=models.CASCADE, related_name='items')
    #subcategory = models.ForeignKey(to='Subcategory', related_name='items')
    description = models.CharField(null=True, blank=True, max_length=100)
    donor = models.ForeignKey(to='User', on_delete=models.SET_NULL, null=True, blank=True)
    fulfilled = models.BooleanField(default=False, blank=True)
    time_fulfilled = models.DateTimeField(null=True, auto_now=True)

# class Category(models.Model):
#     categories = [
#         'TI': 'Travel Items'

#         'CL': 'Clothes'


#     ]
#     category = models.CharField(choices=categories, max_length=50)
    

# class Subcategory(models.Model):
#     category = models.ForeignKey(to='Category', related_name='subcategories')    class 
#     choices = ['stroller, double-stroller, infant car-seat, convertible car-seat', 'rear-facing car seat']
#     category = models.ForeignKey(to=Category, default=1):
    



