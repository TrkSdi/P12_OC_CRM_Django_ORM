from rest_framework import permissions


class ReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return super().has_permission(request, view)

class IsSales(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if user.role == "Vente":
            return True

    def has_object_permission(self, request, view, obj):
        return obj.sales_contact == request.user


class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if user.role == "Gestion":
            return True

    def has_object_permission(self, request, view, obj):
        return self.has_permission
