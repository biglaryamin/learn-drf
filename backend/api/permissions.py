from rest_framework.permissions import BasePermission
from blog.models import Article


SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')




class IsSuperUser(BasePermission):
    """
    Allows access only to superuser user.
    """
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_superuser)




class IsStafforReadOnly(BasePermission):
    """
    Allows access only to superuser user and staff[s].
    """
    def has_permission(self, request, view):
        return bool(request.method in SAFE_METHODS or request.user and request.user.is_staff)



class IsAuthororReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True

        return bool(obj.author == request.user and request.user.is_staff or request.user.is_superuser)





class IsSuperuserOrStaff(BasePermission):
    def has_permission(self, request, view):
        
        return bool(request.method in SAFE_METHODS and request.user.is_staff and request.user.is_authenticated and request.user or
        request.user and request.user.is_superuser)