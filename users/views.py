from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from django.contrib.auth import authenticate

from rest_framework_simplejwt.tokens import RefreshToken

from .models import User
from .serializers import UserSerializer, RegisterSerializer, LoginSerializer



# User list (Admin only)
class UserListView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]



# Register
class RegisterView(generics.CreateAPIView):
    """Register a new user"""
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]



# Login with JWT
class LoginView(APIView):

    permission_classes = [AllowAny]
    throttle_classes = [AnonRateThrottle, UserRateThrottle]

    def post(self, request, *args, **kwargs):

        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        data = serializer.validated_data

        username = data.get("username") # type: ignore
        email = data.get("email") # type: ignore
        password = data.get("password") # type: ignore

        # Allow login with email
        if not username and email:
            try:
                user_obj = User.objects.get(email=email)
                username = user_obj.username
            except User.DoesNotExist:
                return Response(
                    {"detail": "Invalid credentials"},
                    status=status.HTTP_400_BAD_REQUEST,
                )

        user = authenticate(
            request,
            username=username,
            password=password,
        )

        if user is None:
            return Response(
                {"detail": "Invalid credentials"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        
        # Safe response (no password)
        resp = {
            "id": user.id, # type: ignore
            "username": user.username,
            "email": user.email,
            "role": user.role.name if hasattr(user, "role") and user.role else None, # type: ignore
        }

        
        # JWT tokens
        refresh = RefreshToken.for_user(user)

        resp["access"] = str(refresh.access_token)
        resp["refresh"] = str(refresh)

        return Response(resp, status=status.HTTP_200_OK)