from django.urls import path
from .views import ApplicationListView
from core.views import placeholder

urlpatterns = [
    path('', lambda request: placeholder(request, "Applications"), name='applications-placeholder'),  # Placeholder view for the base URL
    # path('applications/', ApplicationListView.as_view()),
]