from rest_framework.permissions import BasePermission
# TODO:
class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_active if request.user.is_active else "Иди нахуй")