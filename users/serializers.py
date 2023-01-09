from rest_framework import serializers
from django.contrib.auth.models import User

class UserValidateSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

class UserCreateSerializer(UserValidateSerializer):
    def validate_username(self, username):
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise ValueError('User with this username already exist')






