from rest_framework import serializers
from .models import *
from rest_framework_jwt.settings import api_settings

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields = ['username', 'fullname','email','is_admin']

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model=project
        fields='__all__'

class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model=lists
        fields='__all__'

class ChecklistSerializer(serializers.ModelSerializer):
    class Meta:
        model=checklist
        fields='__all__'

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model=card
        fields='__all__'

class CardCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model=card_comment
        fields='__all__'