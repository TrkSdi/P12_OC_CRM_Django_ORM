from django.db import models
from django.shortcuts import get_object_or_404
from Epic_Events.settings import AUTH_USER_MODEL

# Create your models here.

class Client(models.Model):
    first_name = models.CharField("Prénom", max_length=25)
    last_name = models.CharField("Nom", max_length=25)
    email = models.EmailField(max_length=100)
    phone = models.CharField("Tél. fixe", max_length=10)
    mobile = models.CharField("Tél. mobile", max_length=10)
    company_name = models.CharField("Compagnie", max_length=250, null=True, blank=True, default=None)
    date_created = models.DateTimeField("Date de création", auto_now_add=True)
    date_updated = models.DateTimeField("Mis à jour le", auto_now=True)
    sales_contact = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.PROTECT, default=None)
    
    def __str__(self):
        return self.first_name

class Lead(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=10)
    mobile = models.CharField(max_length=10)
    company_name = models.CharField("Compagnie", max_length=250, null=True, blank=True, default=None)
    date_created = models.DateTimeField("Date de création", auto_now_add=True)
    date_updated = models.DateTimeField("Mis à jour le", auto_now=True)
    sales_contact = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.PROTECT, default=None)
    converted_to_client = models.BooleanField(default=False)
    
    def __str__(self):
        return self.first_name
    
    #def convert_to_client(self, pk):
    #    if self.converted_to_client is False:
    #        return
    #    self.converted_to_client = True
    #    self.save()
    #    prospect = get_object_or_404(Leads, pk=pk)
    #    client = Client.objects.create(
    #            first_name = prospect.first_name,
    #            last_name = prospect.last_name,
    #            email = prospect.email, 
    #            phone = prospect.phone,
    #            mobile = prospect.mobile,
    #            date_created = prospect.date_created,
    #            date_updated = prospect.date_updated,
    #            sales_contact = prospect.sales_contact
    #        )
    #    client.save()
        

class Contract(models.Model):
    
    sales_contact = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.PROTECT, null=True, blank=True, default=None)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    date_created = models.DateTimeField("Date de création", auto_now_add=True)
    date_updated = models.DateTimeField("Mis à jour le", auto_now=True)
    status = models.BooleanField("Contrat signé", default=False)
    amount = models.FloatField()
    payement_due = models.DateField()
    
    def __str__(self):
        return f'Contrat de: {self.client}'
    
class EventStatus(models.Model):
    name = models.CharField(max_length=50)
    status = models.BooleanField("Commencé", default=False)

    
class Event(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, null=True, blank=True, default=None)
    date_created = models.DateTimeField("Date de création", auto_now_add=True)
    date_updated = models.DateTimeField("Mis à jour le", auto_now=True)
    support_contact = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.PROTECT)
    event_status = models.ForeignKey(EventStatus, on_delete=models.CASCADE)
    attendees = models.IntegerField()
    event_date = models.DateTimeField()
    note = models.TextField(max_length=500)
    
    def __str__(self):
        return f'Evenement: {self.client}'


    