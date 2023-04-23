from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from django.contrib import messages

from user.models import CustomUser
from CRM.models import Client, Lead, Contract, Event
from api.serializers import UserSerializer, ClientSerializer, LeadSerializer, ContractSerializer, EventSerializer
from api.permissions import IsAdmin



from django.contrib import messages
from rest_framework.decorators import action

class UserViewSet(ModelViewSet):
    
    serializer_class = UserSerializer
    queryset = CustomUser.objects.all()
    permission_classes = []
    
    def list(self, request, *args, **kwargs):
        queryset = CustomUser.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)


class ClientViewSet(ModelViewSet):
    
    serializer_class = ClientSerializer
    queryset = Client.objects.all()
    permission_classes = []
    
    
class LeadViewSet(ModelViewSet):
    serializer_class = LeadSerializer
    queryset = Lead.objects.all()
    permission_classes = []
    
    #@action(detail=True, methods=['put'])
    #def convert_to_client(self,request):
    #    self.get_object.convert_to_client()
    #    return Response()


class ContractViewSet(ModelViewSet):
    serializer_class = ContractSerializer
    queryset = Contract.objects.all()
    permission_classes = []


class EventViewSet(ModelViewSet):
    serializer_class =EventSerializer
    queryset = Event.objects.all()
    permission_classes = []
    



