from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.hashers import make_password


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    fieldsets = [
        ("ID", {"fields": ["first_name", "last_name", "email"]}),
        ("Authentication", {"fields": ["username", "password"]}),
        ("Permission", {"fields": ["role", "is_staff", "is_active", "is_superuser"]})
    ]
    def save_model(self, request, obj, form, change):
        # Hash the password before saving the user
        obj.password = make_password(obj.password)
        super().save_model(request, obj, form, change)
        

        