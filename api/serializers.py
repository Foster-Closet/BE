from rest_framework import serializers
from core.models import User, Registry, TravelItem


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'zipcode', 'email', 'phone_number', 'first_name', 'last_name', 'is_donor', 'is_foster']
    
class TravelItemSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = TravelItem
        fields = ['id', 'registry', 'donor', 'description', 'fulfilled']


class RegistrySerializer(serializers.ModelSerializer):
    travelitems = TravelItemSerializer(many=True, read_only=True)

    class Meta:
        model = Registry
        fields = ['id', 'time_made', 'travelitems']