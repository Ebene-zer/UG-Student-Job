from rest_framework import generics
from .models import Application
from .serializers import ApplicationSerializer
from .schemas import application_list_schema

# Create your views here.
@application_list_schema
class ApplicationListView(generics.ListCreateAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
