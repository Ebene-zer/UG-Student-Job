from django.urls import path
from .views import JobListView
from core.views import placeholder

urlpatterns = [
    path('', lambda request: placeholder(request, "Jobs"), name='jobs-placeholder'),
    # path('jobs/', JobListView.as_view()),
]