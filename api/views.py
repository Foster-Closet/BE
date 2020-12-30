from core.models import User, Registry, Item
from api.serializers import UserSerializer, RegistrySerializer, ItemSerializer, ItemWithRegistrySerializer
from rest_framework import generics, permissions, viewsets
from rest_framework.exceptions import PermissionDenied
from rest_framework.authentication import  BasicAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view


try:
    user = User.objects.all().first()
except User.DoesNotExist:
    user = User(username='testuser', password='momentumlearn')
    user.save()

class UserCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]



#https://stackoverflow.com/questions/15770488/return-the-current-user-with-django-rest-framework





class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]
    queryset = User.objects.all()



class RegistryListView(generics.ListCreateAPIView):
    serializer_class = RegistrySerializer
    #permission_classes = [permissions.IsAuthenticated]
    permission_classes = [permissions.AllowAny]


    def perform_create(self, serializer):
    #     #if not self.request.user.is_foster:
    #         #raise PermissionDenied(detail="Only foster families can add registries")
        #serializer.save(user=self.request.user)
        #serializer.save(user=self.request.user)
        serializer.save(user=user)
        

    def get_queryset(self):
        return Registry.objects.filter(user=user)

class RegistryDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = RegistrySerializer

    def get_queryset(self):
        #return Registry.objects.filter(registry__user=self.request.user)
        return Registry.objects.all()


class ItemCreateView(generics.ListCreateAPIView): 
    queryset = Item.objects.all()
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    permission_classes = [permissions.AllowAny]
    serializer_class = ItemWithRegistrySerializer



    def perform_create(self, serializer):
        # registry = serializer.validated_data['registry']
        # if registry.user != self.request.user:
        #     raise PermissionDenied(detail="This registry does not belong to this user.")
        serializer.save()

class ItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    #permission_classes = [permissions.IsAuthenticated]
    permission_classes = [permissions.AllowAny]
    serializer_class = ItemSerializer


    def get_queryset(self):
        #return Item.objects.filter(registry__user=self.request.user)
        return Item.objects.all()

    
    