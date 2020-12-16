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
    registry = models.ForeignKey(to='Registry', on_delete=models.CASCADE, related_name='requests')
    description = models.CharField(null=True, blank=True, max_length=100)
    donor = models.ForeignKey(to='User', on_delete=models.SET_NULL, null=True, blank=True)
    fulfilled = models.BooleanField(default=False, blank=True)
    time_fulfilled = models.DateTimeField(null=True, auto_now=True)
