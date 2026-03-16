import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    email = models.EmailField(unique=True)

    is_student = models.BooleanField(default=False)
    is_employer = models.BooleanField(default=False)

    #link role to user
    role = models.ManyToManyField('Role', blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username

class Role(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
    

class StudentProfile(models.Model):
    user = models.OneToOneField(
        User, 
        on_delete=models.CASCADE, related_name='student_profile'
    )

    full_name = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=20, blank=True,)
    date_of_birth = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.full_name
    
class Employer(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="employer_profile"
    )

    company_name = models.CharField(max_length=150)
    contact_email = models.EmailField()
    contact_phone = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.company_name
    

class EmployerVerification(models.Model):
    employer = models.OneToOneField(
        Employer,
        on_delete=models.CASCADE,
        related_name="verification"
    )

    is_verified = models.BooleanField(default=False)
    verification_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"Verification for {self.employer.company_name} - Verified: {self.is_verified}"
