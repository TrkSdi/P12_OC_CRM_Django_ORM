from rest_framework.response import Response
from rest_framework.decorators import api_view
from user.models import CustomUser
from CRM.models import Client, Prospect, Contract, Event
from api.serializers import UserSerializer, ClientSerializer, ProspectSerializer, ContractSerializer, EventSerializer
from rest_framework.viewsets import ModelViewSet
from api.permissions import IsAdmin
from rest_framework.permissions import IsAuthenticated



class UserViewSet(ModelViewSet):
    
    
    serializer_class = UserSerializer
    queryset = CustomUser.objects.all()
    permission_classes = [IsAdmin & IsAuthenticated]
    
   
    def list(self, request, *args, **kwargs):
        queryset = CustomUser.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)
        

class ClientViewSet(ModelViewSet):
    
    serializer_class = ClientSerializer
    queryset = Client.objects.all()
    permission_classes = [IsAdmin & IsAuthenticated]



class ProspectViewSet(ModelViewSet):
    serializer_class = ProspectSerializer
    queryset = Prospect.objects.all()
    permission_classes = []

class ContractViewSet(ModelViewSet):
    serializer_class = ContractSerializer
    queryset = Contract.objects.all()
    permission_classes = []

class EventViewSet(ModelViewSet):
    serializer_class =EventSerializer
    queryset = Event.objects.all()
    permission_classes = []
