from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin


class CustomUserManager(BaseUserManager):
    def create_user(self, username, email=None, password=None, **extra_fields):
        if not username:
            raise ValueError("Nom d'utilisateur obligatoire")

        user = self.model(
            username=username,
            email=email
        )
        user.is_staff = True
        user.is_active = True
        user.is_superuser = True
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, username, email=None, password=None):

        user = self.create_user(
                            username=username,
                            email=email,
                            password=password
                            )
        user.is_admin = True
        user.role = 'Gestion'
        user.save()


class CustomUser(AbstractBaseUser, PermissionsMixin):

    ROLE = (
        ('Gestion', 'Gestion'),
        ('Vente', 'Vente'),
        ('Support', 'Support'),
    )

    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    username = models.CharField(max_length=50, unique=True, blank=False)
    password = models.CharField(max_length=500)
    email = models.EmailField(max_length=250, unique=True, blank=False)
    role = models.CharField(max_length=10, choices=ROLE, null=True, blank=True)
    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
    objects = CustomUserManager()

    def __str__(self):
        return f'{self.username} ({self.role})'

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    class Meta:
        verbose_name = "Collaborateur"
        verbose_name_plural = "Collaborateurs"
