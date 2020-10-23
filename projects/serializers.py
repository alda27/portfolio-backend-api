from rest_framework import serializers
from .models import Project, Tags


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'
