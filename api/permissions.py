from rest_framework import permissions
from rest_framework.permissions import SAFE_METHODS, IsAuthenticated
from rest_action_permissions.permissions import ActionPermission
from CRM.models import Client, Lead


class AllowedToConvertLeads(permissions.BasePermission):
    
    def has_permission(self, request, view):
        print("Has permission called")
        user = request.user
        return user.role in ['Gestion', 'Vente']
    
    def has_object_permission(self, request, view, obj):
        print("Has object permission called")
        user = request.user
        if obj.sales_contact == user or user.role == "Gestion":
            return True

class LeadsPermissions(permissions.BasePermission):
    
    def has_permission(self, request, view):
        user = request.user
        if user.role == "Vente" and view.action in ['list', 'create', 'retrieve', 'update', 'destroy']:
            return True
        elif user.role == "Support" and view.action in ['list', 'retrieve']:
            return True
        elif user.role == "Gestion" and view.action in ['list', 'retrieve', 'update', 'destroy']:
            return True
        else:
            return False
    
    def has_object_permission(self, request, view, obj):
        user = request.user
        if obj.sales_contact == user or user.role == 'Gestion':
            return True
        if view.action in ['list', 'retrieve']:
            return True
        else:
            return False


class ClientsPermissions(permissions.BasePermission):
    
    def has_permission(self, request, view):
        user = request.user
        
        if user.role == "Vente" and view.action in ['list', 'create', 'retrieve', 'update', 'destroy']:
            return True
        elif user.role == "Support" and view.action in ['list', 'retrieve']:
            return True
        elif user.role == "Gestion" and view.action in ['list', 'create', 'retrieve', 'update', 'destroy']:
            return True
        else:
            return False
    
    def has_object_permission(self, request, view, obj):
        
        user = request.user
        
        if request.method in SAFE_METHODS:
            return True
        if  obj.sales_contact == user or user.role == 'Gestion':
            return True


class ContractPermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        
        if user.role == "Vente" and view.action in ['list', 'create', 'retrieve', 'update', 'destroy']:
            return True
        elif user.role == "Support" and view.action in ['list', 'retrieve']:
            return True
        elif user.role == "Gestion" and view.action in ['list', 'create', 'retrieve', 'update', 'destroy']:
            return True
        else:
            return False    
        
    def has_object_permission(self, request, view, obj):
        user = request.user
        if request.method in SAFE_METHODS:
            return True
        if  obj.sales_contact == user or user.role == 'Gestion':
            return True


class EventPermissions(permissions.BasePermission):
    
    def has_permission(self, request, view):
        user = request.user
        if user.role == "Vente" and view.action in ['list', 'create', 'retrieve', 'update', 'destroy']:
            return True
        elif user.role == "Support" and view.action in ['list', 'create', 'retrieve', 'update', 'destroy']:
            return True
        elif user.role == "Gestion" and view.action in ['list', 'create', 'retrieve', 'update', 'destroy']:
            return True
        else:
            return False
    
    def has_object_permission(self, request, view, obj):
        user = request.user
        if request.method in SAFE_METHODS:
            return True
        if obj.support_contact == user:
            return True
        client = Client.objects.get(id=obj.client.id)
        if user.id == client.sales_contact.id:
            return True
        if user.role == "Gestion":
            return True


class EventStatusPermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if user.role == "Vente" and view.action in ['list','retrieve']:
            return True
        elif user.role == "Support" and view.action in ['list','retrieve']:
            return True
        elif user.role == "Gestion" and view.action in ['list', 'create', 'retrieve', 'update', 'destroy']:
            return True
        else:
            return False
        
    def has_object_permission(self, request, view, obj):
        user = request.user
        if user.role == "Gestion":
            return True
            
#class LeadsActionPermissions(ActionPermission):
#    create_perms = IsAuthenticated & LeadsPermissions
#    retrieve_perms = IsAuthenticated & LeadsPermissions
#    list_perms = IsAuthenticated & LeadsPermissions
#    update_perms = IsAuthenticated & LeadsPermissions
#    delete_perms = IsAuthenticated & LeadsPermissions
#    write_perms = IsAuthenticated & LeadsPermissions
#    destroy_perms = IsAuthenticated & LeadsPermissions
#    None_perms = IsAuthenticated & LeadsPermissions
#    read_perms = IsAuthenticated & LeadsPermissions
#    convert_to_client = IsAuthenticated & AllowedToConvertLeads
    