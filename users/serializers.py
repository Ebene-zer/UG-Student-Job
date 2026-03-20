from rest_framework import serializers
from .models import User, StudentProfile, Employer, Role

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        user = super().create(validated_data)
        if password:
            user.set_password(password)
            user.save()
        return user

    #Used to update already existing user, but not currently used in the project. Kept for future use.
    # def update(self, instance, validated_data):
    #     password = validated_data.pop('password', None)
    #     user = super().update(instance, validated_data)
    #     if password:
    #         user.set_password(password)
    #         user.save()
    #     return user

class StudentProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentProfile
        fields = "__all__"
        read_only_fields = ['user']

class EmployerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employer
        fields = "__all__"
        read_only_fields = ['user']

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = "__all__"


class RegisterSerializer(serializers.ModelSerializer):

    role = serializers.PrimaryKeyRelatedField(
        queryset=Role.objects.all(),
        required=True
    )

    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "email",
            "password",
            "role",
        )

    def create(self, validated_data):

        role = validated_data.pop("role")
        password = validated_data.pop("password")

        user = User(**validated_data)
        user.role = role
        user.set_password(password)
        user.save()

        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=False, allow_blank=True)
    email = serializers.EmailField(required=False, allow_blank=True)
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        username = attrs.get('username')
        email = attrs.get('email')
        password = attrs.get('password')

        if not password:
            raise serializers.ValidationError('Password is required')

        if not username and not email:
            raise serializers.ValidationError('Either username or email is required')

        return attrs


class MeSerialzer(serializers.ModelSerializer):
    role = serializers.CharField(source='role.name', read_only=True)

    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "email",
            "role",
        )