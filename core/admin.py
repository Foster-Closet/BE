from django.contrib import admin
from .models import User, Registry, TestModel

# Register your models here.
admin.register(Registry)
admin.register(User)
admin.register(TestModel)