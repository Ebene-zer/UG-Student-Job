from django.shortcuts import render
from rest_framework import generics
from users.models import User
from .serializers import UserSerializer, RegisterSerializer

# Create your views here.
class UserListView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class RegisterView(generics.CreateAPIView):
    """Register a new user. Supports creating student or employer profiles when
    `is_student`/`is_employer` are set and corresponding nested profile data
    is provided.
    """
    serializer_class = RegisterSerializer