from rest_framework import permissions


class IsAdminUserOrReadonly(permissions.BasePermission):
    """
    Object-level permission to only allow admin/staff of an object to edit it.
    Assumes the model instance has an `user` attribute.
    """

    def has_permission(self, request, view):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user.is_staff
