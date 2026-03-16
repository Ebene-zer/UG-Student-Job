from django.contrib import admin
from .models import Job, JobCategory, JobLocation, Skill

# Register your models here.
admin.site.register(Job)
admin.site.register(JobCategory)
admin.site.register(JobLocation)
admin.site.register(Skill)
