from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    zipcode = models.CharField(null=True, blank=True, max_length=5)
    is_donor = models.BooleanField(default=True)
    is_foster = models.BooleanField(default=False)
    phone_number = models.CharField(null=True, blank=True, max_length=10)


class Registry(models.Model):
    author = models.ForeignKey(to='User', on_delete=models.CASCADE, related_name='requests')
    time_made = models.DateTimeField(auto_now=True)

class TestModel(models.Model):
    number = models.IntegerField()

# class GenericItem(models.Model):
#     ITEM_CHOICES = [ 
#         ('Feeding Supplies', (
#             ('bottles', 'Bottles'),
#             ('formula', 'Formula'),
#             )
#         ),
#         ('Bedding', (
#             ('cribs', 'Cribs'),
#             )
#         ),
#     ]

#     STATUS_CHOICES = [
#     ('fulfilled', 'Fulfilled'),
#     ('open', 'Open' ),  
# ]  
#     donor = models.ForeignKey(to='User', on_delete=models.SET_NULL, null=True, blank=True)
#     number_of_items = models.IntegerField(default=1, blank=True)
#     fulfilled = models.CharField(choices=STATUS_CHOICES, default='open')
#     item = models.CharField(choices=ITEM_CHOICES, max_length='50')
#     time_fulfilled = models.DateTimeField(null=True, blank=True)