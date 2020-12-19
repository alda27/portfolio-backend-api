# from django.shortcuts import render

from rest_framework import generics

from .models import Project, Tags
from .serializers import ProjectSerializer, TagsSerializer


# Create your views here.


class ListTags(generics.ListCreateAPIView):
    queryset = Tags.objects.all()
    serializer_class = TagsSerializer
    name = 'tags_list'


class DetailTags(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tags.objects.all()
    serializer_class = TagsSerializer
    name = 'tags_detail'


class ListProject(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    name = 'projects_list'


class DetailProject(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    name = 'project_detail'
