from rest_framework import permissions

class CanMoveEmployeePermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role in ['watcher', 'admin']
