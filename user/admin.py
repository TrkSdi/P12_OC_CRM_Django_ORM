from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import Group
from .admin_permissions import GroupAdminPermissions, CustomUserPermissions


class GroupAdmin(GroupAdminPermissions, admin.ModelAdmin):
    list_display = ["name", "pk"]

admin.site.unregister(Group)
admin.site.register(Group, GroupAdmin)

@admin.register(CustomUser)
class CustomUserAdmin(CustomUserPermissions, admin.ModelAdmin):
    
    fieldsets = [
        ("ID", {"fields": ["first_name", "last_name", "email"]}),
        ("Authentication", {"fields": ["username", "password"]}),
        ("Permission", {"fields": ["role"]})
    ]

    def save_model(self, request, obj, form, change):
        if change:
            original_obj = self.model.objects.get(pk=obj.pk)
            if obj.password != original_obj.password:
                obj.password = make_password(obj.password)
        else:
            obj.password = make_password(obj.password)
        
        super().save_model(request, obj, form, change)
        

        