from django.contrib import admin
from .models import Client, Lead, Contract, Event
from django.contrib import messages



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
    
    actions = ['convert_to_client']
    def convert_to_client(self,request, queryset):
        lead = queryset.get()
        print("LEAD", lead)
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
