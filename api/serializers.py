from rest_framework import serializers
from core.models import User, Registry, Item

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'zipcode', 'email', 'phone_number', 'first_name', 'last_name', 'is_donor', 'is_foster']
        
    
class ItemSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Item
        fields = ['id', 'donor', 'description', 'status']

class ItemWithRegistrySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Item
        fields = ['id', 'registry', 'donor', 'description', 'status']

#https://www.django-rest-framework.org/api-guide/relations/
class RegistrySerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True)

    class Meta:
        model = Registry
        fields = ['id', 'time_made', 'items']

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        registry = Registry.objects.create(**validated_data)
        for item_data in items_data:
            Item.objects.create(registry=registry, **item_data)
        return registry

