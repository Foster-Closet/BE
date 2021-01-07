from django.contrib import admin
from .models import User, Registry, Item

# Register your models here.
admin.site.register(Registry)
admin.site.register(User)
admin.site.register(Item)
