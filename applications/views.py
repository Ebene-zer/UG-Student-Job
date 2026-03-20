from rest_framework import generics
from .models import Application
from .serializers import ApplicationSerializer

# Create your views here.
class ApplicationListView(generics.ListCreateAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
