from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    """
    Delete only owner's todos
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user
