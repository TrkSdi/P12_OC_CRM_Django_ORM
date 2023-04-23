from rest_framework import serializers
from user.models import CustomUser
from CRM.models import Client, Lead, Contract, Event, EventStatus


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username',
                  'first_name',
                  'last_name',
                  'email',
                  'role',]


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id',
                  'first_name',
                  'last_name',
                  'email',
                  'phone',
                  'mobile',
                  'company_name',
                  'date_created',
                  'date_updated',
                  'sales_contact'
                  ]


class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = ['id',
                  'first_name',
                  'last_name',
                  'email',
                  'phone',
                  'mobile',
                  'company_name',
                  'date_created',
                  'date_updated',
                  'sales_contact',
                  'converted_to_client'
                  ]


class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = ['id',
                  'sales_contact',
                  'client',
                  'date_created',
                  'date_updated',
                  'status',
                  'amount',
                  'payement_due',
                  ]

 
class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['id',
                  'client',
                  'date_created',
                  'date_updated',
                  'support_contact',
                  'event_status',
                  'attendees',
                  'event_date',
                  'note',
                  ]

class EventStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventStatus
        fields = ['id',
                  'name',
                  'status'
                  ]