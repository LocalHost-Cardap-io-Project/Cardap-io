from rest_framework.permissions import BasePermission

class IsOrganizationUser(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_organization)

class IsClientUser(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_client)