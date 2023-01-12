from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework import status
from .serializers import UserValidateSerializer, UserCreateSerializer
from django.contrib.auth.models import User
from rest_framework.views import APIView


class AuthorizationAPIView(APIView):
    def post(self, request):
        serializer = UserValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(**serializer.validated_data)
        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response(data={'token': token.key})
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED, data={'error_message': 'error, user not found'})

class RegistrationAPIView(APIView):
    def post(self, request):
        serializer = UserCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        User.objects.create_user(**serializer.validated_data)
        return Response(status=status.HTTP_201_CREATED, data={'message': 'user was created!'})