from typing import Optional
from django.contrib import admin
from django.http.request import HttpRequest
from django.contrib.admin.views.decorators import staff_member_required
from .models import Client, Lead, Contract, Event, EventStatus
from django.contrib import messages
from .admin_permissions import (ClientPermissions, EventStatusPermissions,
                                LeadPermissions, ContractPermissions,
                                EventPermissions)


### CLIENT ###
@admin.register(Client)
class ClientAdmin(ClientPermissions, admin.ModelAdmin):
    list_display = ("first_name", "last_name", "company_name", "sales_contact")
    
    fieldsets = [
        ("Informations client", {"fields": ["first_name", "last_name", "email", "phone", "mobile", "company_name"]}),
        ("Date", {"fields": ['date_created','date_updated']}),
        ("Contact", {"fields": ["sales_contact"]}),
    ]
    readonly_fields = ["date_created","date_updated"]
    
    list_filter = ['last_name', 'email']
    
    ### REQUEST.USER SAVE & ASSIGNEMENT
    def save_model(self, request, obj, form, change):
        if not change:
            obj.sales_contact = request.user
        super().save_model(request, obj, form, change)
        
    def get_changeform_initial_data(self, request):
        """
        assign request.user as default sales_contact
        """
        initial = super().get_changeform_initial_data(request)
        initial['sales_contact'] = request.user.id
        return initial
    

### LEAD ###
@admin.register(Lead)
class LeadAdmin(LeadPermissions, admin.ModelAdmin):
    list_display = ('first_name',
                    'last_name',
                    'converted_to_client',
                    'sales_contact')
    fieldsets = [
        ("Informations client",{"fields": ["first_name",
                                           "last_name",
                                           "email",
                                           "phone",
                                           "mobile",
                                           "company_name",
                                           "converted_to_client"]}),
        ("Date", {"fields": ["date_created", "date_updated"]}),
        ("Contact", {"fields": ["sales_contact"]}),
    ]
    readonly_fields = ["date_created","date_updated"]
    
    list_filter = ['last_name', 'email']
    
    ### REQUEST.USER SAVE & ASSIGNEMENT
    def save_model(self, request, obj, form, change):
        if not change:
            obj.sales_contact = request.user
        client = Client.objects.filter(email=obj.email).count()
        if obj.converted_to_client == True and client == 0: 
            lead = Lead.objects.get(pk=obj.pk)
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
            
        super().save_model(request, obj, form, change)
    
    def get_changeform_initial_data(self, request):
        """
        assign request.user as default sales_contact
        """
        initial = super().get_changeform_initial_data(request)
        initial['sales_contact'] = request.user.id
        return initial
    
    ### ACTION ###
    actions = ['convert_to_client']
    
    @admin.action(description="Convertir en client",permissions=["change"])
    def convert_to_client(self,request, queryset):
        lead = queryset.get()
        if lead.converted_to_client is False:
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
        else:
            messages.error(request, 'Déjà client')


### CONTRACT ###
@admin.register(Contract)
class ContractAdmin(ContractPermissions, admin.ModelAdmin):
    list_display = ("client",
                    "status",
                    "sales_contact")
    
    fieldsets = [
        ("Contrat", {"fields": ["client",
                                "date_created",
                                "date_updated",
                                "status"]}),
        ("Facturation", {"fields": ["amount", "payement_due"]}),
        ("Contact", {"fields": ["sales_contact"]}),
    ]
    readonly_fields = ["date_created","date_updated"]
    
    list_filter = ['client__last_name', 'client__email', 'date_created', 'amount']
    
    ### REQUEST.USER SAVE & ASSIGNEMENT
    def save_model(self, request, obj, form, change):
        if not change:
            obj.sales_contact = request.user
        super().save_model(request, obj, form, change)
        
    def get_changeform_initial_data(self, request):
        """
        assign request.user as default sales_contact
        """
        initial = super().get_changeform_initial_data(request)
        initial['sales_contact'] = request.user.id
        return initial

    ### ACTION ###
    actions = ['validate_a_contract']
    
    @admin.action(description = "Valider le contrat", permissions=["change"])
    def validate_a_contract(self, request, queryset):
        contract = queryset.get()
        if contract.status is False:
            contract.status = True
            contract.save()
        else:
            messages.error(request, 'Contrat déjà validé')


### EVENT ###
@admin.register(Event)
class Eventadmin(EventPermissions, admin.ModelAdmin):
    list_display = ('client',
                    'contract',
                    'event_status',
                    'support_contact')
    
    fieldsets = [
        ("Evenement", {"fields": ["contract",
                                  "client",
                                  "date_created",
                                  "date_updated",
                                  "attendees",
                                  "event_status",
                                  "event_date"]}),
        ("Note", {"fields": ["note"]}),
        ("Contact", {"fields": ["support_contact"]}),
    ]
    readonly_fields = ["date_created","date_updated"]

    list_filter = ['client__last_name', 'client__email', 'event_date']
    

### EVENT STATUS ###
@admin.register(EventStatus)
class EventStatusadmin(EventStatusPermissions, admin.ModelAdmin):
    list_display = ("name",)
    fieldsets = [("Status", {"fields" : ["name"]})]
