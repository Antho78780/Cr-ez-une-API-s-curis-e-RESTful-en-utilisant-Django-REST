from rest_framework import permissions
from authentification.models import Contributor


class IsContributorProjectAuthenticated(permissions.BasePermission):
    message = "Vous n'êtes pas autorisé à faire cette action"
    
    def has_object_permission(self, request, view, obj):
        if obj.author_user == request.user:
            return True
        else:
            return Contributor.objects.filter(project=obj, user=request.user).exists()