from django.shortcuts import render
from rest_framework import generics
from jobs.models import Job
from .serializers import JobSerializer

# Create your views here.
class JobListView(generics.ListCreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer