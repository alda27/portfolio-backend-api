from rest_framework import serializers
from .models import Project, Tags


class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    tags = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='tags_detail')  # Serializer
    # relations

    class Meta:
        model = Project
        fields = '__all__'
