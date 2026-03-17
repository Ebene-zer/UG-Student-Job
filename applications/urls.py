from django.urls import path
from .views import ApplicationListView

urlpatterns = [
    path('applications/', ApplicationListView.as_view()),
]