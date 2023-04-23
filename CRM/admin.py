from django.contrib import admin
from .models import Client, Lead, Contract, Event
# Register your models here.


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Informations client", {"fields": ["first_name", "last_name", "email", "phone", "mobile", "company_name"]}),
        ("Date", {"fields": ['date_created','date_updated']}),
        ("Contact", {"fields": ["sales_contact"]}),
    ]
    readonly_fields = ["date_created","date_updated"]
    
@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Informations client", {"fields": ["first_name", "last_name", "email", "phone", "mobile","company_name", "converted_to_client"]}),
        ("Date", {"fields": ["date_created", "date_updated"]}),
        ("Contact", {"fields": ["sales_contact"]}),
    ]
    readonly_fields = ["date_created","date_updated"]

@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Contrat", {"fields": ["client", "date_created", "date_updated", "status"]}),
        ("Facturation", {"fields": ["amount", "payement_due"]}),
        ("Contact", {"fields": ["sales_contact"]}),
    ]
    readonly_fields = ["date_created","date_updated"]
    
@admin.register(Event)
class Eventadmin(admin.ModelAdmin):
    fieldsets = [
        ("Evenement", {"fields": ["client", "date_created", "date_updated", "attendees", "event_status", "event_date"]}),
        ("Note", {"fields": ["note"]}),
        ("Contact", {"fields": ["support_contact"]}),
    ]
    readonly_fields = ["date_created","date_updated"]