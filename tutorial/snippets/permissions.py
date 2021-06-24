from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    '''
    Custom Permissions to only allow owners of an object to edit it.
    '''
    def has_object_permission(self, request, view, obj):
        # allow GET, HEAD or OPTIONS requests only.
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # write permissions are only allowed to the owner of the snippet.
        return obj.owner == request.user