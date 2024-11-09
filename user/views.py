from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth import authenticate, login, logout
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
@api_view(['POST'])
@permission_classes([AllowAny])
def UserCreateApi(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = User.objects.create(username=username) 
    user.set_password(password)
    user.save()
    return Response(
        {
            'messages': 'User Created'
        }
    )


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def protectedview(request):
        return Response({
            'message':'I am already authenticated',
            'username': request.user.username
        })

        