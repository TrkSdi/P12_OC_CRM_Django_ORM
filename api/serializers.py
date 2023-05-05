from rest_framework import serializers
from user.models import CustomUser
from CRM.models import Client, Lead, Contract, Event, EventStatus
from rest_framework.serializers import ValidationError


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id',
                    'username',
                  'first_name',
                  'last_name',
                  'password',
                  'email',
                  'role',]
        extra_kwargs = {'password': {'write_only': True}}
        
        def create(self, validated_data):
            password = validated_data.pop('password')
            user = CustomUser(**validated_data)
            user.set_password(password)
            user.save()
            return user


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
        read_only_fields = [
                  'sales_contact',]


class LeadSerializer(serializers.ModelSerializer):
    
    parent_lookup_kwargs = {
        'leads_pk': 'leads__pk',
    }
    
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
                'converted_to_client']
        read_only_fields = [
                  'sales_contact',]


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
                  'contract',
                  'client',
                  'date_created',
                  'date_updated',
                  'support_contact',
                  'event_status',
                  'attendees',
                  'event_date',
                  'note',
                  ]
        
    def validate(self, data):
        if data['contract'] is None:
            raise serializers.ValidationError("Le champ contrat ne peut pas être vide.")
        return data
        

class EventStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventStatus
        fields = ['id',
                  'name',
                  ]