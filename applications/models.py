import uuid
from django.db import models
from users.models import Employer, StudentProfile

class JobCategory(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = 'Job Categories'

    def __str__(self):
        return self.name

class JobPosting(models.Model):
    class JobTypeChoice(models.TextChoices):
        FULL_TIME = 'FULL_TIME', 'Full Time'
        PART_TIME = 'PART_TIME', 'Part Time'
        INTERNSHIP = 'INTERNSHIP', 'Internship'
        CONTRACT = 'CONTRACT', 'Contract'

    class StatusChoice(models.TextChoices):
        OPEN = 'OPEN', 'Open'
        CLOSED = 'CLOSED', 'Closed'
        DRAFT = 'DRAFT', 'Draft'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    employer = models.ForeignKey(Employer, on_delete=models.CASCADE, related_name='job_postings')
    category = models.ForeignKey(JobCategory, on_delete=models.SET_NULL, null=True, related_name='jobs')
    
    title = models.CharField(max_length=255)
    description = models.TextField()
    requirements = models.TextField()
    location = models.CharField(max_length=255)
    job_type = models.CharField(max_length=20, choices=JobTypeChoice.choices, default=JobTypeChoice.FULL_TIME)
    
    salary_range = models.CharField(max_length=100, blank=True)
    application_deadline = models.DateTimeField()
    
    status = models.CharField(max_length=20, choices=StatusChoice.choices, default=StatusChoice.DRAFT)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} at {self.employer.company_name}"

class Application(models.Model):
    class StatusChoice(models.TextChoices):
        PENDING = 'PENDING', 'Pending Review'
        REVIEWING = 'REVIEWING', 'Under Review'
        ACCEPTED = 'ACCEPTED', 'Accepted'
        REJECTED = 'REJECTED', 'Rejected'
        WITHDRAWN = 'WITHDRAWN', 'Withdrawn'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    job = models.ForeignKey(JobPosting, on_delete=models.CASCADE, related_name='applications')
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE, related_name='applications')
    
    cover_letter = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=StatusChoice.choices, default=StatusChoice.PENDING)
    
    # We could link the exact CV used for this application, or let the student provide a specific one
    cv_url = models.URLField(blank=True, help_text="Link to the specific CV used for this application")
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('job', 'student') # Prevent multiple applications by same student for same job

    def __str__(self):
        return f"{self.student.user.username}'s application for {self.job.title}"

class Interview(models.Model):
    class StatusChoice(models.TextChoices):
        SCHEDULED = 'SCHEDULED', 'Scheduled'
        COMPLETED = 'COMPLETED', 'Completed'
        CANCELED = 'CANCELED', 'Canceled'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    application = models.OneToOneField(Application, on_delete=models.CASCADE, related_name='interview')
    
    scheduled_at = models.DateTimeField()
    location = models.CharField(max_length=255, help_text="Physical location or meeting link/URL")
    notes = models.TextField(blank=True)
    
    status = models.CharField(max_length=20, choices=StatusChoice.choices, default=StatusChoice.SCHEDULED)
    
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Interview for {self.application.student.user.username} - {self.application.job.title}"
