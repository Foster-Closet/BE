from core.models import User
from api.serializers import UserSerializer, RegistrySerializer, TestSerializer
from rest_framework import generics, permissions



class UserCreate(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        return User.objects.all()

class Registry(generics.ListCreateAPIView):

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return Request.objects.filter(user=self.request.user)



class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]


    def get_queryset(self):
        return User.objects.all()

class TestCreate(generics.CreateAPIView):
    serializer_class=TestSerializer

    

