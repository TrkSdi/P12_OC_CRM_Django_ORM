from django.db import models
from django.shortcuts import get_object_or_404
from Epic_Events.settings import AUTH_USER_MODEL


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
    sales_contact = models.ForeignKey(AUTH_USER_MODEL,limit_choices_to={'role': 'Vente'}, on_delete=models.PROTECT, default=None)
    converted_to_client = models.BooleanField(default=False)
    
    def __str__(self):
        return self.first_name


class Contract(models.Model):
    
    sales_contact = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.PROTECT, null=True, blank=True, default=None)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    date_created = models.DateTimeField("Date de création", auto_now_add=True)
    date_updated = models.DateTimeField("Mis à jour le", auto_now=True)
    status = models.BooleanField("Contrat signé", default=False)
    amount = models.FloatField()
    payement_due = models.DateField()
    assigned = models.BooleanField("Assigné", default=False)
    
    def __str__(self):
        return f'Contrat de: {self.client}'


class EventStatus(models.Model):
    
    name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name}'


class Event(models.Model):
    contract = models.ForeignKey(Contract, limit_choices_to={'status': True, 'assigned': False}, on_delete=models.CASCADE, null=True, blank=True, default=None )
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
    
    def assign_contract(self, pk):
        contract = Contract.objects.get(pk=pk)
        print("CONTRACT", contract)
        contract.assigned = True
        contract.save()
        client = contract.client
        client.save()


    