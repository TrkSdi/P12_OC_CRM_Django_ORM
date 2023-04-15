from django.db import models

# Create your models here.

class Client(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=10)
    mobile = models.CharField(max_length=10)
    date_created = models.DateField()
    date_updated = models.DateField()
    #sales_contact
    