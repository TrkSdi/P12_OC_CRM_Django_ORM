from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class CustomUser(AbstractUser):
    
    ROLE = (
        ('Gestion', 'Gestion'),
        ('Vente', 'Vente'),
        ('Support', 'Support'),
    )
    
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=10, choices=ROLE, null=True, blank=True)
    #username = models.CharField(max_length=25, unique=True)

    def __str__(self):
        return f'{self.username} ({self.role})'