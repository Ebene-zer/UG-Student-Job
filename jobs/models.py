from django.db import models
from users.models import User, Employer

# Create your models here.
class JobCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
    

class JobLocation(models.Model):
    name = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return self.name
    
class Skill(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
    

class Job(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    employer = models.ForeignKey(
        Employer,
        on_delete=models.CASCADE, 
        related_name='jobs'
    )
    
    categories = models.ManyToManyField(
        JobCategory, 
        blank=True
    )
    
    location = models.ForeignKey(
        JobLocation,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    skills = models.ManyToManyField(
        Skill,
        blank=True
    )

    deadline = models.DateTimeField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title