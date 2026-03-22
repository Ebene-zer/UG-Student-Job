from drf_spectacular.utils import extend_schema
from .serializers import ApplicationSerializer

# Application list schema
application_list_schema = extend_schema(
    tags=['Applications'],
    summary="List and create job applications",
    description="Retrieve a list of job applications or submit a new application.",
    request=ApplicationSerializer,
    responses={
        200: ApplicationSerializer(many=True),
        201: ApplicationSerializer,
    },
)