from django.contrib import admin
from .models import Notification, SavedJob, Report, AuditLog

# Register your models here.
admin.site.register(Notification)
admin.site.register(SavedJob)
admin.site.register(Report)
admin.site.register(AuditLog)
