from rest_framework import serializers
from core.models import User, Registry, TestModel


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'password']

 
class RegistrySerializer(serializers.ModelSerializer):

    class Meta:
        model = Registry
        

class UserSerializer2(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'password', 'zipcode', 'email', 'phone_number', 'first_name', 'last_name']

class TestSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = TestModel
        fields = ['number']
