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

class EmployerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employer
        fields = "__all__"

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = "__all__"


class RegisterSerializer(serializers.ModelSerializer):
    student_profile = StudentProfileSerializer(required=False)
    employer_profile = EmployerSerializer(required=False)
    role = serializers.PrimaryKeyRelatedField(queryset=Role.objects.all(), many=True, required=False)

    class Meta:
        model = User
        fields = (
            'id', 'username', 'email', 'password', 'is_student', 'is_employer',
            'role', 'student_profile', 'employer_profile',
        )
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        roles = validated_data.pop('role', [])
        student_data = validated_data.pop('student_profile', None)
        employer_data = validated_data.pop('employer_profile', None)
        password = validated_data.pop('password', None)

        user = User(**validated_data)
        if password:
            user.set_password(password)
        else:
            user.set_unusable_password()
        user.save()

        if roles:
            user.role.set(roles)

        # create related profiles when indicated
        if user.is_student and student_data:
            # remove any nested user/id keys that may have been sent
            student_data.pop('user', None)
            student_data.pop('id', None)
            StudentProfile.objects.create(user=user, **student_data)

        if user.is_employer and employer_data:
            # remove any nested user/id keys that may have been sent
            employer_data.pop('user', None)
            employer_data.pop('id', None)
            Employer.objects.create(user=user, **employer_data)

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