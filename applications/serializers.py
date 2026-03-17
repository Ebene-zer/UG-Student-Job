from rest_framework import serializers
from .models import Application, CV, StudentSkill, ApplicationStatusHistory, InterviewSchedule

class CVSerializer(serializers.ModelSerializer):
    class Meta:
        model = CV
        fields = "__all__"

class StudentSkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentSkill
        fields = "__all__"

class ApplicationStatusHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplicationStatusHistory
        fields = "__all__"

class InterviewScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = InterviewSchedule
        fields = "__all__"

class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = "__all__"