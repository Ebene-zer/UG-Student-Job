from django.contrib import admin
from .models import User, Role, StudentProfile, Employer, EmployerVerification

# Register your models here.
admin.site.register(User)
admin.site.register(Role)
admin.site.register(StudentProfile)
admin.site.register(Employer)
admin.site.register(EmployerVerification)