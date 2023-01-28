from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    """
    For model User
    """
    def has_object_permission(self, request, view, obj):
        return request.user.id == obj.id
