from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):

    # checks if the user is the owner of the company
    def has_object_permission(self, request, view, obj):
        return request.user == obj.user
