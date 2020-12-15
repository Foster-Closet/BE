from django.contrib import admin
from .models import User, Registry, Item

# Register your models here.
admin.register(Registry)
admin.register(User)
admin.register(Item)
