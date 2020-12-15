from core.models import User, Registry, Item
from api.serializers import UserSerializer, RegistrySerializer, ItemSerializer
from rest_framework import generics, permissions
from rest_framework.exceptions import PermissionDenied



class UserCreateView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]
    queryset = User.objects.all()



class RegistryListView(generics.ListCreateAPIView):
    serializer_class = RegistrySerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        if not serializer.cleaned_data['is_foster']:
            raise PermissionDenied(detail="Only foster families can add registries")

        serializer.save(user=self.request.user)

    def get_queryset(self):
        return Registry.objects.filter(user=self.request.user)

class ItemCreateView(generics.CreateAPIView): 
    queryset = Item.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        registry = serializer.cleaned_data['registry']
        if registry.user != self.request.user:
            raise PermissionDenied(detail="This registry does not belong to this user.")
        serializer.save()


# class ItemListView(generics.ListView):
#     serializer_class = ItemSerializer
#     queryset = Item.objects.all()
    
   
class ItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ItemSerializer


    def get_queryset(self):
        return Item.objects.filter(registry__user=self.request.user)
    
    