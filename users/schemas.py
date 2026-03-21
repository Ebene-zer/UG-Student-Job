from drf_spectacular.utils import extend_schema, OpenApiExample, OpenApiResponse
from .serializers import *

# Register schema
register_schema = extend_schema(
    tags=['Authentication'],
    summary="Register a new user",
    description="Create a new user account. Choose a role (student or employer) and provide required details.",
    request=RegisterSerializer,
    responses={
        201: UserSerializer,
        400: OpenApiResponse(description="Validation errors"),
    },
    examples=[
        OpenApiExample(
            "Register as student",
            request_only=True,
            value={
                "username": "john_doe",
                "email": "john@example.com",
                "password": "securepassword123",
                "role": "student",
                "first_name": "John",
                "last_name": "Doe",
            },
        ),
        OpenApiExample(
            "Register as employer",
            request_only=True,
            value={
                "username": "acme_corp",
                "email": "hr@acme.com",
                "password": "securepassword123",
                "role": "employer",
                "first_name": "Jane",
                "last_name": "Smith",
            },
        ),
    ],
)

# Login schema
login_schema = extend_schema(
    tags=['Authentication'],
    summary="User login",
    description="Authenticate a user and return JWT access and refresh tokens. Login with username/email and password.",
    request=LoginSerializer,
    responses={
        200: OpenApiResponse(
            description="Login successful",
            response={
                "type": "object",
                "properties": {
                    "access": {"type": "string", "description": "JWT access token"},
                    "refresh": {"type": "string", "description": "JWT refresh token"},
                    "user": {"$ref": "#/components/schemas/User"},
                },
            },
        ),
        401: OpenApiResponse(description="Invalid credentials"),
    },
    examples=[
        OpenApiExample(
            "Login with username",
            request_only=True,
            value={
                "username": "john_doe",
                "password": "securepassword123",
            },
        ),
        OpenApiExample(
            "Login with email",
            request_only=True,
            value={
                "email": "john@example.com",
                "password": "securepassword123",
            },
        ),
    ],
)

# User list schema
user_list_schema = extend_schema(
    tags=['Users'],
    summary="List and create users (Admin only)",
    description="Retrieve a list of all users or create a new user. Requires admin privileges.",
    request=UserSerializer,
    responses={
        200: UserSerializer(many=True),
        201: UserSerializer,
        403: OpenApiResponse(description="Admin access required"),
    },
)

# Me schema
me_schema = extend_schema(
    tags=['Users'],
    summary="Get current user details",
    description="Retrieve details of the currently authenticated user.",
    responses={
        200: MeSerialzer,
        401: OpenApiResponse(description="Unauthorized"),
    },
)

# Student profile schemas
student_profile_get_schema = extend_schema(
    tags=['Profile'],
    summary="Get student profile",
    description="Retrieve the student profile for the authenticated user.",
    methods=['GET'],
    responses={
        200: StudentProfileSerializer,
        404: OpenApiResponse(description="Profile not found"),
    },
)

student_profile_post_schema = extend_schema(
    tags=['Profile'],
    summary="Create student profile",
    description="Create a new student profile if one doesn't exist.",
    methods=['POST'],
    request=StudentProfileSerializer,
    responses={
        201: StudentProfileSerializer,
        400: OpenApiResponse(description="Profile already exists or validation error"),
    },
)

student_profile_put_schema = extend_schema(
    tags=['Profile'],
    summary="Update student profile",
    description="Update the existing student profile.",
    methods=['PUT'],
    request=StudentProfileSerializer,
    responses={
        200: StudentProfileSerializer,
        400: OpenApiResponse(description="Validation error"),
        404: OpenApiResponse(description="Profile not found"),
    },
)

# Employer profile schemas
employer_profile_get_schema = extend_schema(
    tags=['Profile'],
    summary="Get employer profile",
    description="Retrieve the employer profile for the authenticated user.",
    methods=['GET'],
    responses={
        200: EmployerSerializer,
        404: OpenApiResponse(description="Profile not found"),
    },
)

employer_profile_post_schema = extend_schema(
    tags=['Profile'],
    summary="Create employer profile",
    description="Create a new employer profile if one doesn't exist.",
    methods=['POST'],
    request=EmployerSerializer,
    responses={
        201: EmployerSerializer,
        400: OpenApiResponse(description="Profile already exists or validation error"),
    },
)

employer_profile_put_schema = extend_schema(
    tags=['Profile'],
    summary="Update employer profile",
    description="Update the existing employer profile.",
    methods=['PUT'],
    request=EmployerSerializer,
    responses={
        200: EmployerSerializer,
        400: OpenApiResponse(description="Validation error"),
        404: OpenApiResponse(description="Profile not found"),
    },
)