
# Group Admin
class GroupAdminPermissions():
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
        

# Custom User
class CustomUserPermissions():
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