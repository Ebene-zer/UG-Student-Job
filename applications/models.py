from django.db import models
from users.models import User, StudentProfile
from jobs.models import Job, Skill

# Create your models here.
class CV(models.Model):
    student = models.ForeignKey(
        StudentProfile, 
        on_delete=models.CASCADE,
        related_name='cvs'
    )

    file = models.FileField(upload_to='cvs/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"CV - {self.student.full_name}"
    

class StudentSkill(models.Model):
    student = models.ForeignKey(
        StudentProfile, 
        on_delete=models.CASCADE,
        related_name='skills'
    )
    skill = models.ForeignKey(
        Skill, 
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f"{self.student.full_name} - {self.skill.name}"
    

class Application(models.Model):
    student = models.ForeignKey(
        StudentProfile, 
        on_delete=models.CASCADE,
        related_name='applications'
    )
    job = models.ForeignKey(
        Job, 
        on_delete=models.CASCADE,
        related_name='applications'
    )
    cv = models.ForeignKey(
        CV, 
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    status = models.CharField(
        max_length=50,
        default='pending',
    )
    
    applied_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.full_name} - {self.job.title}"
    

class ApplicationStatusHistory(models.Model):
    application = models.ForeignKey(
        Application, 
        on_delete=models.CASCADE,
        related_name='status_history'
    )
    status = models.CharField(max_length=50)

    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.application} - {self.status}"
    
class InterviewSchedule(models.Model):
    application = models.OneToOneField(
        Application,
        on_delete=models.CASCADE,
        related_name="interview"
    )

    interview_date = models.DateTimeField()
    location = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f"Interview for {self.application} on {self.interview_date}"