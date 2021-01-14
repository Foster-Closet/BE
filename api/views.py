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


class RegistryListCreateView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = RegistrySerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        
    def get_queryset(self):
        return self.request.user.registries.all()


class RegistryListView(generics.ListAPIView):
    serializer_class = RegistrySerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        return Registry.objects.exclude(user=self.request.user).order_by('time_made')


class RegistryDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = RegistrySerializer

    def get_queryset(self):
        return Registry.objects.all()


class ItemCreateView(generics.ListCreateAPIView): 
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = ItemWithRegistrySerializer

    def perform_create(self, serializer):
        registry = serializer.validated_data['registry']
        if registry.user != self.request.user:
            raise PermissionDenied(detail="This registry does not belong to this user.")
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
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = ItemWithRegistrySerializer

    def get_queryset(self):
        return Item.objects.filter(registry__user=self.request.user)
        #return Item.objects.all()

    
    