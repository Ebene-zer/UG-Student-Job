from django.db import models
from django.conf import settings

# Create your models here.
class Notification(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='notifications'
    )

    message = models.TextField()

    is_read = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Notification for {self.user.username}"
    

class SavedJob(models.Model):
    student = models.ForeignKey(
        'users.StudentProfile',
        on_delete=models.CASCADE,
        related_name="saved_jobs"
    )

    job = models.ForeignKey(
        'jobs.Job',
        on_delete=models.CASCADE,
        related_name='saved_by_students'
    )

    saved_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.user.username} saved {self.job.title}"
    

class Report(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='reports'
    )

    description = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    resolved = models.BooleanField(default=False)

    def __str__(self):
        return f"Report by {self.user.username}"
    

class AuditLog(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='audit_logs'
    )

    action = models.CharField(max_length=255)

    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"AuditLog: {self.user.username} - {self.action}"