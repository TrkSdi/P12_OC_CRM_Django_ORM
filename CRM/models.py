from django.db import models
from django.forms import ValidationError
from django.shortcuts import get_object_or_404
from Epic_Events.settings import AUTH_USER_MODEL
from django.db.models import Q


class Client(models.Model):
    first_name = models.CharField("Prénom", max_length=25)
    last_name = models.CharField("Nom", max_length=25)
    email = models.EmailField("Email", max_length=100)
    phone = models.CharField("Tél. fixe", max_length=10)
    mobile = models.CharField("Tél. mobile", max_length=10)
    company_name = models.CharField("Compagnie", max_length=250, null=True, blank=True, default=None)
    date_created = models.DateTimeField("Date de création", auto_now_add=True)
    date_updated = models.DateTimeField("Mis à jour le", auto_now=True)
    sales_contact = models.ForeignKey(AUTH_USER_MODEL, limit_choices_to=Q(role='Vente')|Q(role='Gestion'), on_delete=models.PROTECT, default=None, verbose_name="Contact")
    
    def __str__(self):
        return self.first_name
    
    class Meta:
        verbose_name = "Client"


class Lead(models.Model):
    first_name = models.CharField("Prénom", max_length=25)
    last_name = models.CharField("Nom", max_length=25)
    email = models.EmailField("Email", max_length=100)
    phone = models.CharField("Tél. fixe", max_length=10)
    mobile = models.CharField("Tél. mobile", max_length=10)
    company_name = models.CharField("Compagnie", max_length=250, null=True, blank=True, default=None)
    date_created = models.DateTimeField("Date de création", auto_now_add=True)
    date_updated = models.DateTimeField("Mis à jour le", auto_now=True)
    sales_contact = models.ForeignKey(AUTH_USER_MODEL,limit_choices_to=Q(role='Vente')|Q(role='Gestion'), on_delete=models.PROTECT, verbose_name="Contact")
    converted_to_client = models.BooleanField("Converti en client",default=False)
    
    def __str__(self):
        return self.first_name
    
    class Meta:
        verbose_name = "Prospect"


class Contract(models.Model):
    
    sales_contact = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.PROTECT, null=True, blank=True, default=None, verbose_name="Contact")
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name="Client")
    date_created = models.DateTimeField("Date de création", auto_now_add=True)
    date_updated = models.DateTimeField("Mis à jour le", auto_now=True)
    status = models.BooleanField("Contrat signé", default=False)
    amount = models.FloatField("Montant")
    payement_due = models.DateField("Date d'échéance")
    
    
    def __str__(self):
        return f'Contrat de: {self.client}'
    
    class Meta:
        verbose_name = "Contrat"


class EventStatus(models.Model):
    
    name = models.CharField("Intitulé", max_length=50)

    def __str__(self):
        return f'{self.name}'
    
    class Meta:
        verbose_name = "Status"
        verbose_name_plural = "Status"


class Event(models.Model):
    contract = models.ForeignKey(Contract, limit_choices_to={'status': True}, on_delete=models.CASCADE, null=True, verbose_name="Contrat")
    client = models.ForeignKey(Client, on_delete=models.CASCADE, null=True, blank=True, default=None, verbose_name="Client")
    date_created = models.DateTimeField("Date de création", auto_now_add=True)
    date_updated = models.DateTimeField("Mis à jour le", auto_now=True)
    support_contact = models.ForeignKey(AUTH_USER_MODEL, limit_choices_to=Q(role='Support')|Q(role='Gestion'), on_delete=models.PROTECT, verbose_name="Contact")
    event_status = models.ForeignKey(EventStatus, on_delete=models.CASCADE, verbose_name='Status')
    attendees = models.IntegerField("Nombre de participants")
    event_date = models.DateTimeField("Date de l'évènement")
    note = models.TextField("Note", max_length=500)
    
    def __str__(self):
        return f'Évenement de: {self.client}'
    
    class Meta:
        verbose_name = "Évènement"
    

    