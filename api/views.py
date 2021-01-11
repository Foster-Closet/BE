from core.models import User, Registry, Item, Message
from api.serializers import UserSerializer, RegistrySerializer, ItemSerializer, ItemWithRegistrySerializer, MessageSerializer
from rest_framework import generics, permissions, viewsets, status
from rest_framework.exceptions import PermissionDenied
from rest_framework.authentication import  BasicAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from twilio.rest import Client
from django.conf import settings

client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)

def sendMessage(body, from_, to):
    message = client.messages.create(
                     body=body,
                     from_=from_,
                     to=to
    )



try:
    user = User.objects.all().first()
except User.DoesNotExist:
    user = User(username='testuser', password='momentumlearn')

    user.save()



class UserCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]
    queryset = User.objects.all()


@api_view(['GET', 'POST'])
def message_list(request):
    """
    Return a user's messages, or post a message from one user to another
    """
    if request.method == 'GET':
        messages = request.user.messages_received
        serializer = MessageSerializer(messages, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(sender=request.user)
            message = serializer.data['message']
            receiver_id = serializer.data['receiver']
            reciever = User.objects.filter(id=receiver_id).first()
            sendMessage(message, request.user.phone_number, reciever.phone_number)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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


class RegistryListCreateView(generics.ListCreateAPIView):
    serializer_class = RegistrySerializer
    #permission_classes = [permissions.IsAuthenticatedOrReadONly]
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
    #     #if not self.request.user.is_foster:
    #         #raise PermissionDenied(detail="Only foster families can add registries")
        serializer.save(user=self.request.user)
        #serializer.save(user=user)
        
    def get_queryset(self):
        return self.request.user.registries.all()


class RegistryListView(generics.ListAPIView):
    serializer_class = RegistrySerializer
    #permission_classes = [permissions.IsAuthenticatedOrReadONly]
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        return Registry.objects.exclude(user=self.request.user)


class RegistryDetailView(generics.RetrieveUpdateDestroyAPIView):
    #permission_classes = [permissions.IsAuthenticated]
    permission_classes = [permissions.AllowAny]
    serializer_class = RegistrySerializer

    def get_queryset(self):
        #return Registry.objects.filter(registry__user=self.request.user)
        return self.request.user.registries.all()
        #return user.registries.all()


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
        return Item.objects.filter(registry__user=self.request.user)
        #return Item.objects.filter(registry__user=user)


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
        return Item.objects.filter(registry__user=self.request.user)
        #return Item.objects.all()

    
    