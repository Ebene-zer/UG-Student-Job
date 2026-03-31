from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [

    path('token/refresh/', TokenRefreshView.as_view()),
    path('me/', MeView.as_view()),
    path('users/', UserListView.as_view()),
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('student-profile/', StudentProfileView.as_view()),
    path('employer-profile/', EmployerProfileView.as_view()),

]