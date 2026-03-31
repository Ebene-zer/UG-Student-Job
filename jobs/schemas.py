from drf_spectacular.utils import extend_schema
from .serializers import JobSerializer

# Job list schema
job_list_schema = extend_schema(
    tags=['Jobs'],
    summary="List and create jobs",
    description="Retrieve a list of all job postings or create a new job posting.",
    request=JobSerializer,
    responses={
        200: JobSerializer(many=True),
        201: JobSerializer,
    },
)