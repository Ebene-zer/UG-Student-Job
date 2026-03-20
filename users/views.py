from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken

from .models import User, StudentProfile, Employer
from .serializers import *
from .permissions import *


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
                {"detail": "Invalid credentials. User may not exist."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        
         # JWT tokens
        refresh = RefreshToken.for_user(user)

        resp = {
            "access": str(refresh.access_token),
            "refresh": str(refresh),
        }


        return Response(resp, status=status.HTTP_200_OK)
    

class MeView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = MeSerialzer(request.user)
        return Response(serializer.data)


class StudentProfileView(APIView):
    permission_classes = [IsStudent]

    def get(self, request):
        profile = StudentProfile.objects.filter(user=request.user).first()

        if not profile:
            return Response(
                {"detail": "Profile not found"},
                status=404,
            )

        serializer = StudentProfileSerializer(profile)
        return Response(serializer.data)


    def post(self, request):
        if StudentProfile.objects.filter(user=request.user).exists():
            return Response(
                {"detail": "Profile already exists"},
                status=400,
            )

        serializer = StudentProfileSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=201)

        return Response(serializer.errors, status=400)


    def put(self, request):
        profile = StudentProfile.objects.filter(user=request.user).first()

        if not profile:
            return Response(
                {"detail": "Profile not found"},
                status=404,
            )

        serializer = StudentProfileSerializer(
            profile,
            data=request.data,
            partial=True,
        )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=400)
    

class EmployerProfileView(APIView):
    permission_classes = [IsEmployer]

    def get(self, request):
        profile = Employer.objects.filter(user=request.user).first()

        if not profile:
            return Response(
                {"detail": "Profile not found"},
                status=404,
            )

        serializer = EmployerSerializer(profile)
        return Response(serializer.data)


    def post(self, request):
        if Employer.objects.filter(user=request.user).exists():
            return Response(
                {"detail": "Profile already exists"},
                status=400,
            )

        serializer = EmployerSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=201)

        return Response(serializer.errors, status=400)


    def put(self, request):
        profile = Employer.objects.filter(user=request.user).first()

        if not profile:
            return Response(
                {"detail": "Profile not found"},
                status=404,
            )

        serializer = EmployerSerializer(
            profile,
            data=request.data,
            partial=True,
        )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=400)