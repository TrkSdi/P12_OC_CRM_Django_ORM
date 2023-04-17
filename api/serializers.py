from rest_framework import serializers
from user.models import CustomUser
from CRM.models import Client, Prospect, Contract, Event



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
        fields = ['first_name',
                  'last_name',
                  'email',
                  'phone',
                  'mobile',
                  'date_created',
                  'date_updated',
                  'sales_contact'
                  ]
        
class ProspectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prospect
        fields = ['first_name',
                  'last_name',
                  'email',
                  'phone',
                  'mobile',
                  'date_created',
                  'date_updated',
                  'sales_contact'
                  ]

class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = ['sales_contact',
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
        fields = ['client',
                  'date_created',
                  'date_updated',
                  'support_contact',
                  'event_status',
                  'attendees',
                  'event_date',
                  'note',
                  ]
        