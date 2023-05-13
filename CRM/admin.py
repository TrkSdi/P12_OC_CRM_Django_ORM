from typing import Optional
from django.contrib import admin
from django.http.request import HttpRequest
from django.contrib.admin.views.decorators import staff_member_required
from .models import Client, Lead, Contract, Event, EventStatus
from django.contrib import messages


### CLIENT ###
@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Informations client", {"fields": ["first_name", "last_name", "email", "phone", "mobile", "company_name"]}),
        ("Date", {"fields": ['date_created','date_updated']}),
        ("Contact", {"fields": ["sales_contact"]}),
    ]
    readonly_fields = ["date_created","date_updated"]
    
    ### REQUEST.USER SAVE & ASSIGNEMENT
    def save_model(self, request, obj, form, change):
        if not change:
            obj.sales_contact = request.user
        super().save_model(request, obj, form, change)
        
    def get_changeform_initial_data(self, request):
        initial = super().get_changeform_initial_data(request)
        initial['sales_contact'] = request.user.id
        return initial
    
    
    ### PERMISSIONS ### 
    def has_view_permission(self, request, obj=None):
        if request.user.role in ["Vente", "Support", "Gestion"]:
            return True
           
    def has_add_permission(self, request):
        if request.user.role == "Vente":
            return True

    def has_change_permission(self, request, obj=None):
        if (obj and obj.sales_contact == request.user) or request.user.role in ["Gestion"]:
            return True
    
    def has_delete_permission(self, request, obj=None):
        if obj and obj.sales_contact == request.user:
            return True


### LEAD ###
@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
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
    
    ### REQUEST.USER SAVE & ASSIGNEMENT
    def save_model(self, request, obj, form, change):
        if not change:
            obj.sales_contact = request.user
        super().save_model(request, obj, form, change)
    
    def get_changeform_initial_data(self, request):
        initial = super().get_changeform_initial_data(request)
        initial['sales_contact'] = request.user.id
        return initial
    
    ### ACTION ###
    actions = ['convert_to_client']
    
    @admin.action(permissions=["change"])
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

    ### PERMISSIONS ### 
    def has_view_permission(self, request, obj=None):
        if request.user.role == "Vente" or "Support" or "Gestion":
            return True
           
    def has_add_permission(self, request):
        if request.user.role == "Vente":
            return True

    def has_change_permission(self, request, obj=None):
        if (obj and obj.sales_contact == request.user) or request.user.role in ["Gestion"]:
            return True
    
    def has_delete_permission(self, request, obj=None):
        if obj and obj.sales_contact == request.user:
            return True


### CONTRACT ###
@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    list_display = ("client",
                    "status")
    
    fieldsets = [
        ("Contrat", {"fields": ["client",
                                "date_created",
                                "date_updated",
                                "status"]}),
        ("Facturation", {"fields": ["amount", "payement_due"]}),
        ("Contact", {"fields": ["sales_contact"]}),
    ]
    readonly_fields = ["date_created","date_updated"]
    
    ### REQUEST.USER SAVE & ASSIGNEMENT
    def save_model(self, request, obj, form, change):
        if not change:
            obj.sales_contact = request.user
        super().save_model(request, obj, form, change)
        
    def get_changeform_initial_data(self, request):
        initial = super().get_changeform_initial_data(request)
        initial['sales_contact'] = request.user.id
        return initial

    ### ACTION ###
    actions = ['validate_a_contract']
    
    @admin.action(permissions=["change"])
    def validate_a_contract(self, request, queryset):
        contract = queryset.get()
        if contract.status is False:
            contract.status = True
            contract.save()
        else:
            messages.error(request, 'Contrat déjà validé')
    
    ### PERMISSIONS ###        
    def has_view_permission(self, request, obj=None):
        if request.user.role == "Vente" or "Support" or "Gestion":
            return True
           
    def has_add_permission(self, request):
        if request.user.role == "Vente":
            return True

    def has_change_permission(self, request, obj=None):
        if (obj and obj.sales_contact == request.user) or request.user.role in ["Gestion"]:
            return True
    
    def has_delete_permission(self, request, obj=None):
        if obj and obj.sales_contact == request.user:
            return True


### EVENT ###
@admin.register(Event)
class Eventadmin(admin.ModelAdmin):
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


    ### PERMISSIONS ###        
    def has_view_permission(self, request, obj=None):
        if request.user.role in ["Vente", "Support", "Gestion"]:
            return True
           
    def has_add_permission(self, request):
        if request.user.role in ["Vente"]:
            return True
        
    def has_change_permission(self, request, obj=None):
        if obj and obj.client and obj.client.sales_contact == request.user:
            return True
        if request.user.role in ["Gestion"]:
            return True
        if obj and obj.support_contact == request.user:
            return True
    
    def has_delete_permission(self, request, obj=None):
        if obj and obj.client and obj.client.sales_contact == request.user:
            return True
        if obj and obj.support_contact == request.user:
            return True
        

### EVENT STATUS ###
@admin.register(EventStatus)
class EventStatusadmin(admin.ModelAdmin):
    fieldsets = [("Status", {"fields" : ["name", "creator"]})]
    
    ### REQUEST.USER SAVE & ASSIGNEMENT
    def save_model(self, request, obj, form, change):
        if not change:
            obj.creator = request.user
        super().save_model(request, obj, form, change)
        
    def get_changeform_initial_data(self, request):
        initial = super().get_changeform_initial_data(request)
        initial['creator'] = request.user.id
        return initial
    
    ### PERMISSIONS ### 
    def has_view_permission(self, request, obj=None):
        if request.user.role in ["Vente", "Support", "Gestion"]:
            return True
        
    def has_add_permission(self, request):
        if request.user.role in ["Vente",]:
            return True
    
    def has_change_permission(self, request, obj=None):
        if obj and obj.creator == request.user:
            return True
        if request.user.role in ["Gestion"]:
            return True
    
    def has_delete_permission(self, request, obj=None):
        if obj and obj.creator == request.user:
            return True