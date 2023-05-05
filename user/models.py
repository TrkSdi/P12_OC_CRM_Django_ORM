from django.db import models
from django.contrib.auth.models import AbstractUser

    

class CustomUser(AbstractUser):
    
    ROLE = (
        ('Gestion', 'Gestion'),
        ('Vente', 'Vente'),
        ('Support', 'Support'),
    )
    
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=500)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=10, choices=ROLE, null=True, blank=True)
    is_staff = models.BooleanField(('staff'), default=True)
    is_active = models.BooleanField(('active'), default=True)
    is_superuser = models.BooleanField(('manager'), default=False)
    
    
    def __str__(self):
       return f'{self.username} ({self.role})'
   
    def save(self, *args, **kwargs):
        self.set_password(self.password)
        super().save(*args, **kwargs)