from rest_framework import serializers
from core.models import User, Registry, Item, Message

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email', 'phone_number', 'first_name', 'last_name']
        
class MessageSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Message
        fields = ['sender', 'receiver', 'message', 'url' ]
   
class ItemSerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model = Item
        fields = ['id', 'donor', 'description', 'status']

class ItemWithRegistrySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Item
        fields = ['id', 'registry', 'donor', 'description', 'status']

class ItemStatusSerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True)


#https://www.django-rest-framework.org/api-guide/relations/
class RegistrySerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True)
    user = serializers.SlugRelatedField(read_only=True, slug_field='username')
    class Meta:
        model = Registry
        fields = ['id', 'user', 'items']

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        registry = Registry.objects.create(**validated_data)
        for item_data in items_data:
            Item.objects.create(registry=registry, **item_data)
        return registry

    def update(self, instance, validated_data):
        items_data = validated_data.pop('items')
        # Unless the application properly enforces that this field is
        # always set, the following could raise a `DoesNotExist`, which
        # would need to be handled.
        #original_items = instance.items
        for item_data in items_data:
            Item.objects.create(registry=instance, **item_data)
        return instance
