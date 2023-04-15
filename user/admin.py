from django.contrib import admin
from .models import CustomUser

# Register your models here.

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    fieldsets = [
        ("ID", {"fields": ["first_name", "last_name", "email"]}),
        ("Authentication", {"fields": ["username", "password"]}),
        ("Permission", {"fields": ["role"]})
    ]

