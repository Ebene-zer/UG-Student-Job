from rest_framework import serializers
from .models import Job, JobCategory, JobLocation, Skill

class JobCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = JobCategory
        fields = "__all__"

class JobLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobLocation
        fields = "__all__"

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = "__all__"

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = "__all__"