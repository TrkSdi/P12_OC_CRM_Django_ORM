from django.contrib import admin
from .models import Client, Prospect, Contract, Event
# Register your models here.


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Informations client", {"fields": ["first_name", "last_name", "email", "phone", "mobile"]}),
        ("Date", {"fields": ["date_created", "date_updated"]}),
        ("Contact", {"fields": ["sales_contact"]}),
    ]
    
@admin.register(Prospect)
class ProspectAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Informations client", {"fields": ["first_name", "last_name", "email", "phone", "mobile"]}),
        ("Date", {"fields": ["date_created", "date_updated"]}),
        ("Contact", {"fields": ["sales_contact"]}),
    ]

@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Contrat", {"fields": ["client", "date_created", "date_updated", "status"]}),
        ("Facturation", {"fields": ["amount", "payement_due"]})
    ]
    
@admin.register(Event)
class Eventadmin(admin.ModelAdmin):
    fieldsets = [
        ("Evenement", {"fields": ["client", "date_created", "date_updated", "attendees", "event_status"]}),
        ("Note", {"fields": ["note"]}),
        ("Contact", {"fields": ["support_contact"]}),
        
    ]