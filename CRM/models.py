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
    sales_contact = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    date_created = models.DateField()
    date_updated = models.DateField()
    status = models.BooleanField(default=False)
    amount = models.FloatField(max_length=4)
    payement_due = models.DateField()
    

class Event(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    date_created = models.DateField()
    date_updated = models.DateField()
    support_contact = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    event_status = models.ForeignKey(Contract, on_delete=models.CASCADE)
    attendees = models.IntegerField()
    event_date = models.DateTimeField()
    note = models.TextField(max_length=500)