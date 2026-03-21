from drf_spectacular.utils import extend_schema
from .serializers import NotificationSerializer

# Notification list schema
notification_list_schema = extend_schema(
    tags=['Notifications'],
    summary="List and create notifications",
    description="Retrieve user notifications or create a new notification.",
    request=NotificationSerializer,
    responses={
        200: NotificationSerializer(many=True),
        201: NotificationSerializer,
    },
)