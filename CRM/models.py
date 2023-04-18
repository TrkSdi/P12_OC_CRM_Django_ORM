from django.db import models
from Epic_Events.settings import AUTH_USER_MODEL

# Create your models here.

class Client(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=10)
    mobile = models.CharField(max_length=10)
    date_created = models.DateField()
    date_updated = models.DateField()
    sales_contact = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, default=None)
    
    def __str__(self):
        return self.first_name

class Prospect(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=10)
    mobile = models.CharField(max_length=10)
    date_created = models.DateField()
    date_updated = models.DateField()
    sales_contact = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)


class Contract(models.Model):
    sales_contact = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True, default=None)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    date_created = models.DateField()
    date_updated = models.DateField()
    status = models.BooleanField(default=False)
    amount = models.FloatField()
    payement_due = models.DateField()
    
    def __str__(self):
        return f'Contrat: {self.client}'
    

class Event(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, null=True, blank=True, default=None)
    date_created = models.DateField()
    date_updated = models.DateField()
    support_contact = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    event_status = models.ForeignKey(Contract, on_delete=models.CASCADE)
    attendees = models.IntegerField()
    event_date = models.DateTimeField()
    note = models.TextField(max_length=500)
    
    def __str__(self):
        return f'Evenement: {self.client}'
    