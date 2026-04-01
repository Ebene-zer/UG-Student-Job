from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import Role, StudentProfile, Employer, EmployerVerification

# Use get_user_model to avoid direct import of the concrete User model
User = get_user_model()

# Register your models here.
admin.site.register(User)
admin.site.register(Role)
admin.site.register(StudentProfile)
admin.site.register(Employer)
admin.site.register(EmployerVerification)