from django.urls import path
from .views import NotificationListView, placeholder

urlpatterns = [
    path('', lambda request: placeholder(request, "Core"), name='core-placeholder'),
    path('notifications/', NotificationListView.as_view()),
]