
# CLIENT
class ClientPermissions():
    def has_view_permission(self, request, obj=None):
        if request.user.role in ["Vente", "Support", "Gestion"]:
            return True

    def has_add_permission(self, request):
        if request.user.role in ["Vente", "Gestion"]:
            return True

    def has_change_permission(self, request, obj=None):
        if (obj and obj.sales_contact == request.user) or request.user.role == "Gestion":
            return True

    def has_delete_permission(self, request, obj=None):
        if (obj and obj.sales_contact == request.user) or request.user.role == "Gestion":
            return True


# LEAD
class LeadPermissions():
    def has_view_permission(self, request, obj=None):
            if request.user.role in ["Vente", "Support", "Gestion"]:
                return True

    def has_add_permission(self, request):
        if request.user.role in ["Vente", "Gestion"]:
            return True

    def has_change_permission(self, request, obj=None):
        if (obj and obj.sales_contact == request.user) or request.user.role == "Gestion":
            return True

    def has_delete_permission(self, request, obj=None):
        if (obj and obj.sales_contact == request.user) or request.user.role == "Gestion":
            return True


# CONTRACT
class ContractPermissions():
    def has_view_permission(self, request, obj=None):
        if request.user.role in ["Vente", "Support", "Gestion"]:
            return True
           
    def has_add_permission(self, request):
        if request.user.role in ["Vente", "Gestion"]:
            return True

    def has_change_permission(self, request, obj=None):
        if (obj and obj.sales_contact == request.user) or request.user.role in ["Gestion"]:
            return True
    
    def has_delete_permission(self, request, obj=None):
        if (obj and obj.sales_contact == request.user) or request.user.role in ["Gestion"]:
            return True


# EVENT
class EventPermissions():     
    def has_view_permission(self, request, obj=None):
        if request.user.role in ["Vente", "Support", "Gestion"]:
            return True
           
    def has_add_permission(self, request):
        if request.user.role in ["Vente", "Gestion"]:
            return True
        
    def has_change_permission(self, request, obj=None):
        if request.user.role in ["Gestion"]:
            return True
        if obj and obj.client and obj.client.sales_contact == request.user:
            return True
        if obj and obj.support_contact == request.user:
            return True
    
    def has_delete_permission(self, request, obj=None):
        if request.user.role in ["Gestion"]:
            return True
        if obj and obj.client and obj.client.sales_contact == request.user:
            return True
        if obj and obj.support_contact == request.user:
            return True


# EVENT STATUS PERMISSION
class EventStatusPermissions():
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