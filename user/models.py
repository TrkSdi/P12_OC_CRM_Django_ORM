from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin, AbstractUser


#class MyUserManager(BaseUserManager):
#    def create_user(self, username, password):
#        if not username:
#            raise ValueError("Nom d'utilisateur obligatoire")
#        user = self.model(username=username, password=password)
#        user.set_password(password)
#        user.is_staff = True
#        user.is_active = True
#        user.save(using=self.db)
#        
#        return user
#    
#    def create_superuser(self, username, password, **kwargs):
#        user = self.create_user(username=username, password=password)
#        user.is_admin = True
#        user.is_staff = True
#        user.is_active = True
#        user.is_superuser = True
#        user.set_password(password)
#        user.save(using=self.db)
#        
#        return user
#
#class CustomUser(AbstractBaseUser, PermissionsMixin):
#    ROLE = (
#        ('Gestion', 'Gestion'),
#        ('Vente', 'Vente'),
#        ('Support', 'Support'),
#    )
#    
#    first_name = models.CharField(max_length=50, null=True, blank=True)
#    last_name = models.CharField(max_length=50, null=True, blank=True)
#    username = models.CharField(max_length=50, unique=True)
#    password = models.CharField(max_length=500)
#    email = models.EmailField(unique=True)
#    role = models.CharField(max_length=10, choices=ROLE, null=True, blank=True)
#    is_staff = models.BooleanField(('staff'), default=True)
#    is_active = models.BooleanField(('active'), default=True)
#    is_superuser = models.BooleanField(('manager'), default=False)
#
#    USERNAME_FIELD = 'username'
#    objects = MyUserManager()
#    
#    def __str__(self):
#        return f'{self.username} ({self.role})'
#    
#    def has_perm(self, perm, obj=None): 
#        return True
#
#    def has_module_perms(self, app_label): 
#        return True
    

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