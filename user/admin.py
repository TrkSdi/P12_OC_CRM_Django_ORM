from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import Group


class GroupAdmin(admin.ModelAdmin):
    list_display = ["name", "pk"]
    
    ### Permissions ###        
    def has_view_permission(self, request, obj=None):
        if request.user.role == "Gestion":
            return True
        
    def has_add_permission(self, request):
        if request.user.role == "Gestion":
            return True

    def has_change_permission(self, request, obj=None):
        if request.user.role == "Gestion":
            return True
    
    def has_delete_permission(self, request, obj=None):
        if request.user.role == "Gestion":
            return True

admin.site.unregister(Group)
admin.site.register(Group, GroupAdmin)

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    
    fieldsets = [
        ("ID", {"fields": ["first_name", "last_name", "email"]}),
        ("Authentication", {"fields": ["username", "password"]}),
        ("Permission", {"fields": ["role", "is_staff", "is_active", "is_superuser"]})
    ]
    readonly_fields = ["is_staff", "is_active", "is_superuser"]
    
    def save_model(self, request, obj, form, change):
        if change:
            original_obj = self.model.objects.get(pk=obj.pk)
            if obj.password != original_obj.password:
                obj.password = make_password(obj.password)
        else:  # New model being created
            obj.password = make_password(obj.password)
        
        super().save_model(request, obj, form, change)
        
    ### Permissions ###        
    def has_view_permission(self, request, obj=None):
        if request.user.role == "Vente" or "Support" or "Gestion":
            return True
        
    def has_add_permission(self, request):
        if request.user.role == "Gestion":
            return True

    def has_change_permission(self, request, obj=None):
        if request.user.role == "Gestion":
            return True
    
    def has_delete_permission(self, request, obj=None):
        if request.user.role == "Gestion":
            return True
        

        