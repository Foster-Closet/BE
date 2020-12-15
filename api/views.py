from core.models import User, Registry, TravelItem
from api.serializers import UserSerializer, RegistrySerializer, TravelItemSerializer
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

class TravelItemCreateView(generics.CreateAPIView): 
    queryset = TravelItem.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        registry = serializer.cleaned_data['registry']
        if registry.user != self.request.user:
            raise PermissionDenied(detail="This registry does not belong to this user.")
        serializer.save()


# class TravelItemListView(generics.ListView):
#     serializer_class = TravelItemSerializer
#     queryset = TravelItem.objects.all()
    
   
class TravelItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = TravelItemSerializer


    def get_queryset(self):
        return TravelItem.objects.filter(registry__user=self.request.user)
    
    