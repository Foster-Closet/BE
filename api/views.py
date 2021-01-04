from core.models import User, Registry, Item
from api.serializers import UserSerializer, RegistrySerializer, ItemSerializer, ItemWithRegistrySerializer
from rest_framework import generics, permissions, viewsets, status
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



class RegistryListv2(APIView):

    def get(self, request, format=None):
        if self.request.user.is_donor:
            registries = Registry.objects.all()
        else:
            registries = request.user.registries.all()
        serializer = RegistrySerializer(registries, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = RegistrySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RegistryListView(generics.ListCreateAPIView):
    serializer_class = RegistrySerializer
    #permission_classes = [permissions.IsAuthenticatedOrReadONly]
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
    #     #if not self.request.user.is_foster:
    #         #raise PermissionDenied(detail="Only foster families can add registries")
        #serializer.save(user=self.request.user)
        serializer.save(user=user)
        

    def get_queryset(self):
        return user.registries.all()

class RegistryDetailView(generics.RetrieveUpdateDestroyAPIView):
    #permission_classes = [permissions.IsAuthenticated]
    permission_classes = [permissions.AllowAny]
    serializer_class = RegistrySerializer

    def get_queryset(self):
        #return Registry.objects.filter(registry__user=self.request.user)
        #return self.request.user.registries.all()
        return user.registries.all()
        
class ItemCreateView(generics.ListCreateAPIView): 
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    permission_classes = [permissions.AllowAny]
    serializer_class = ItemWithRegistrySerializer

    def perform_create(self, serializer):
        # registry = serializer.validated_data['registry']
        # if registry.user != self.request.user:
        #     raise PermissionDenied(detail="This registry does not belong to this user.")
        serializer.save()
    
    def get_queryset(self):
        #return Item.objects.filter(registry_user=self.request.user)
        return Item.objects.filter(registry_user=user)



@api_view(['GET'])
def item_list(request): 
    items = Item.objects.filter(registry__user=request.user)
    return Response({
        'requestedItems': items.filter(status='requestedItems').values(),
        'inProgress': items.filter(status='inProgress').values(),
        'fulfilled': items.filter(status='fulfilled').values()
    })


class ItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    #permission_classes = [permissions.IsAuthenticated]
    permission_classes = [permissions.AllowAny]
    serializer_class = ItemWithRegistrySerializer

    def get_queryset(self):
        #return Item.objects.filter(registry_user=self.request.user)
        return Item.objects.filter(registry_user=user)

    
    