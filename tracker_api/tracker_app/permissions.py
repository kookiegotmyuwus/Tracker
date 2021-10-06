from rest_framework import permissions
from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework.response import Response
from .serializers import *
from .models import *

class UserPermissions(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return request.user.is_authenticated
        return request.user.is_admin or request.user.is_superuser

class ProjectPermissions(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return request.user in obj.members.all() or request.user==obj.creator
        return request.user.is_admin or request.user.is_superuser or request.user==obj.creator

class ListPermissions(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return request.user in obj.project_list.members.all() or request.user==obj.project_list.creator or request.user.is_admin or request.user.is_superuser
        return request.user.is_admin or request.user.is_superuser or request.user==obj.project_list.creator

class CardPermissions(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated
        # change
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return request.user in obj.assignee.all() or request.user==obj.project_card.creator or request.user.is_admin or request.user.is_superuser
        return request.user.is_admin or request.user.is_superuser or request.user==obj.project_card.creator 

class ChecklistPermissions(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user==obj.assignee_card.assignee

class CardCommentPermissions(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user==obj.assignee_card.assignee