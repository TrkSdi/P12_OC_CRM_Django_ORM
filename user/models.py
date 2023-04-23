from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class CustomUser(AbstractUser):
    MANAGER = 1
    SALES = 2
    SUPPORT = 3
    
    ROLE = (
        (MANAGER, 'Gestion'),
        (SALES, 'Vente'),
        (SUPPORT, 'Support'),
    )
    
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=10, choices=ROLE, null=True, blank=True)
    username = models.CharField(max_length=25, unique=True)
    is_staff = models.BooleanField(('staff status'), default=True)
    is_active = models.BooleanField(('active'), default=True)

    def __str__(self):
        return f'{self.username} ({self.role})'