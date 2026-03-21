from django.shortcuts import render
from rest_framework import generics
from jobs.models import Job
from .serializers import JobSerializer
from .schemas import job_list_schema

# Create your views here.
@job_list_schema
class JobListView(generics.ListCreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer