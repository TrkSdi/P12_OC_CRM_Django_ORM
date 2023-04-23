from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view, action
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from django.contrib import messages

from user.models import CustomUser
from CRM.models import Client, Lead, Contract, Event, EventStatus
from api.permissions import IsAdmin
from api.serializers import (UserSerializer, ClientSerializer,
                             LeadSerializer, ContractSerializer,
                             EventSerializer, EventStatusSerializer)



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
    queryset = Lead.objects.filter(converted_to_client=False)
    permission_classes = []
    
    @action(detail=True, methods=['get'])
    def convert_to_client(self,request, pk):
        lead = Lead.objects.get(pk=pk)
        lead.converted_to_client = True
        lead.save()
        client = Client.objects.create(
                first_name = lead.first_name,
                last_name = lead.last_name,
                email = lead.email, 
                phone = lead.phone,
                mobile = lead.mobile,
                company_name = lead.company_name,
                date_created = lead.date_created,
                date_updated = lead.date_updated,
                sales_contact = lead.sales_contact
        )
        client.save()
        return Response()

class ContractViewSet(ModelViewSet):
    serializer_class = ContractSerializer
    queryset = Contract.objects.all()
    permission_classes = []


class EventViewSet(ModelViewSet):
    serializer_class = EventSerializer
    queryset = Event.objects.all()
    permission_classes = []


class EventStatusViewSet(ModelViewSet):
    serializer_class = EventStatusSerializer
    queryset = EventStatus.objects.all()
    permission_classes = []
    



