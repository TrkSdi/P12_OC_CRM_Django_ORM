from rest_framework import permissions
from rest_framework.permissions import SAFE_METHODS
from CRM.models import Client, Lead


class AllowedToConvertLeads(permissions.BasePermission):
    
    def has_permission(self, request, view):
        user = request.user
        if user.role == "Vente":
             return True
    
    def has_object_permission(self, request, view, obj):
        user = request.user
        if user == obj.sales_contact:
            return True


class LeadsPermissions(permissions.BasePermission):
    
    def has_permission(self, request, view):
        user = request.user
        if user.role == "Vente" and view.action in ['list', 'create', 'retrieve', 'update', 'destroy']:
            return True
        elif user.role == "Support" and view.action in ['list', 'retrieve']:
            return True
        elif user.role == "Gestion" and view.action in ['list', 'retrieve']:
            return True
        else:
            return False
    
    def has_object_permission(self, request, view, obj):
        user = request.user
        
        if view.action == 'convert_to_client':
            if obj.sales_contact == user:

                return True
            else:
                return False
        elif obj.sales_contact == user:
            
            return True
        elif view.action in ['list', 'retrieve']:
            
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
        elif user.role == "Gestion" and view.action in ['list', 'retrieve']:
            return True
        else:
            return False
    
    def has_object_permission(self, request, view, obj):
        
        user = request.user
        
        if request.method in SAFE_METHODS:
            return True
        return obj.sales_contact == user


class ContractPermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        
        if user.role == "Vente" and view.action in ['list', 'create', 'retrieve', 'update', 'destroy']:
            return True
        elif user.role == "Support" and view.action in ['list', 'retrieve']:
            return True
        elif user.role == "Gestion" and view.action in ['list', 'retrieve']:
            return True
        else:
            return False    
        
    def has_object_permission(self, request, view, obj):
        user = request.user
        if request.method in SAFE_METHODS:
            return True
        return obj.sales_contact == user
    

class EventPermissions(permissions.BasePermission):
    
    def has_permission(self, request, view):
        user = request.user
        if user.role == "Vente" and view.action in ['list', 'create', 'retrieve', 'update', 'destroy']:
            return True
        elif user.role == "Support" and view.action in ['list', 'create', 'retrieve', 'update', 'destroy']:
            return True
        elif user.role == "Gestion" and view.action in ['list', 'retrieve']:
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


class EventStatusPermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if user.role == "Vente" and view.action in ['list', 'create', 'retrieve', 'update', 'destroy']:
            return True
        elif user.role == "Support" and view.action in ['list', 'create', 'retrieve', 'update', 'destroy']:
            return True
        elif user.role == "Gestion" and view.action in ['list', 'retrieve']:
            return True
        else:
            return False
        
    def has_object_permission(self, request, view, obj):
        if obj.creator == request.user:
            return True
            
