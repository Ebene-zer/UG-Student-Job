from django.shortcuts import render
from rest_framework import generics
from .models import Notification
from .serializers import NotificationSerializer
from django.http import HttpResponse
from .schemas import notification_list_schema

# Create your views here.
def placeholder(request, app_name="This app"):
    return HttpResponse(f"{app_name} feature is under development. Stay tuned!")

@notification_list_schema
class NotificationListView(generics.ListCreateAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer



