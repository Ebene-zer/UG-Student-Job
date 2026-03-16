from django.contrib import admin
from .models import Application, CV, StudentSkill, ApplicationStatusHistory, InterviewSchedule

# Register your models here.
admin.site.register(Application)
admin.site.register(CV)
admin.site.register(StudentSkill)
admin.site.register(ApplicationStatusHistory)
admin.site.register(InterviewSchedule)
