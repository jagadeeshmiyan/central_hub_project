from rest_framework import permissions


class IsTeacher(permissions.BasePermission):
    def has_permission(self, request, view):
        # Allow access only if the user is authenticated and is a teacher
        return request.user and request.user.is_authenticated and request.user.is_teacher