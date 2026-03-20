from django.shortcuts import render
from rest_framework import generics
from .models import Notification
from .serializers import NotificationSerializer
from django.http import HttpResponse

# Create your views here.
def placeholder(request, app_name="This app"):
    return HttpResponse(f"{app_name} feature is under development. Stay tuned!")

class NotificationListView(generics.ListCreateAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer



