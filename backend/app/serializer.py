from rest_framework import serializers
from .models import User, UserRole

class UserRoleSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserRole
        fields = ['role']

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'fullName', 'email', 'password', 'role']

    